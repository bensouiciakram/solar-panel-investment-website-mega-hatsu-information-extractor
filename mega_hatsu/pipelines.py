"""
Scrapy pipeline for processing and storing Mega Hatsu scraped items.

This pipeline handles:
- Connecting to a PostgreSQL database
- Tracking item existence to mark new, still available, or deleted items
- Appending new items or updates to a Pandas DataFrame
- Writing final data to the 'articles' table in PostgreSQL
- Deduplicating entries by 'identifier' at the end of the crawl
"""

from itemadapter import ItemAdapter
import pandas as pd 
import sqlalchemy
from scrapy.exceptions import DropItem

class MegaHatsuPipeline:
    """
    Pipeline for cleaning, validating, and persisting items scraped from mega-hatsu.com.

    Attributes:
        postgres_uri (str): Database connection URI.
        engine (sqlalchemy.Engine): SQLAlchemy engine for PostgreSQL connection.
        conn (sqlalchemy.Connection): Open SQLAlchemy connection.
        df (pd.DataFrame): In-memory data store for collected items.
        ids (set): Set of previously stored item identifiers.
    """

    def __init__(self, postgres_uri):
        """
        Initializes the pipeline and loads existing data from the PostgreSQL database.

        Args:
            postgres_uri (str): The database URI used for connecting to PostgreSQL.
        """
        self.postgres_uri = postgres_uri
        self.engine = sqlalchemy.create_engine(self.postgres_uri)
        try : 
            self.df = pd.read_sql_query('select * from articles',con=self.engine)
        except sqlalchemy.exc.ProgrammingError :
            self.df = pd.DataFrame()
        self.conn = self.engine.connect()
        try :
            results = self.conn.execute('select identifier from articles ;')
            self.ids = {result[0] for result in results}
        except sqlalchemy.exc.ProgrammingError : 
            self.ids = set()

    @classmethod
    def from_crawler(cls, crawler):
        """
        Instantiates the pipeline using project settings from the Scrapy crawler.

        Args:
            crawler (scrapy.crawler.Crawler): The crawler with access to settings.

        Returns:
            MegaHatsuPipeline: An instance of this pipeline class.
        """
        return cls(
            # mongo_uri=crawler.settings.get('MONGO_URI'), 
            postgres_uri= "postgresql://{}:{}@{}:{}/{}".format(
                crawler.settings.get('POSTGRES_USER'),
                crawler.settings.get('POSTGRES_PASS'), 
                crawler.settings.get('POSTGRES_HOST'),
                crawler.settings.get('POSTGRES_PORT'),
                crawler.settings.get('POSTGRES_DB')
                ),
          
        )    
        


    def process_item(self, item, spider):
        """
        Processes each scraped item. Filters invalid items, tags new/existing status,
        and adds the item to the internal DataFrame.

        Args:
            item (scrapy.Item): The scraped item.
            spider (scrapy.Spider): The spider that scraped the item.

        Returns:
            scrapy.Item: The validated and tagged item.

        Raises:
            DropItem: If required fields are missing.
        """
        if not (item['property_number'] and item['total_panel_capacity'] and item['Map']): 
            raise DropItem
            
        if item['identifier'] in self.ids : 
            item['status'] = 'still available'
            self.ids.remove(item['identifier'])
        else : 
            item['status'] = 'new'
        self.df = self.df.append(dict(item),ignore_index=True)
        return item


    def close_spider(self,spider):
        """
        Called when the spider closes. Marks missing items as deleted, removes duplicates,
        writes the final DataFrame to PostgreSQL, and cleans up the connection.
        
        Args:
            spider (scrapy.Spider): The spider instance.
        """
        for identifier in self.ids : 
            self.df.loc[self.df['identifier']==identifier,'status'] = 'deleted'
        self.df.drop_duplicates(subset=['identifier'],keep='last',inplace= True)
        self.df.to_sql(con=self.engine,name='articles',if_exists='append',index=False)
        self.conn.execute('delete from articles where ctid not in (select * from (select max(ctid) from articles group by identifier) it);')
        self.conn.close()
        self.engine.dispose()