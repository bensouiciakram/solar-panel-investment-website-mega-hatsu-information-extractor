# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd 
import sqlalchemy
from scrapy.exceptions import DropItem

class MegaHatsuPipeline:

    def __init__(self, postgres_uri):
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

        if not (item['property_number'] and item['total_panel_capacity'] and item['Map']): 
            raise DropItem
            
        if item['identifier'] in self.ids : 
            item['status'] = 'still available'
            self.ids.remove(item['identifier'])
        else : 
            item['status'] = 'new'
        self.df = self.df.append(dict(item),ignore_index=True)
        #print(self.df)
        return item


    def close_spider(self,spider):
        for identifier in self.ids : 
            self.df.loc[df['identifier']==identifier,'status'] = 'deleted'
        self.df.drop_duplicates(subset=['identifier'],keep='last',inplace= True)
        self.df.to_sql(con=self.engine,name='articles',if_exists='append',index=False)
        self.conn.execute('delete from articles where ctid not in (select * from (select max(ctid) from articles group by identifier) it);')
        self.conn.close()
        self.engine.dispose()