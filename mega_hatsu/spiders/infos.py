import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from mega_hatsu.items import MegaHatsuItem
from price_parser import Price

class InfosSpider(scrapy.Spider):
    name = 'infos'
    allowed_domains = ['mega-hatsu.com']
    start_urls = ['https://mega-hatsu.com/article-for-sale/']

    def __init__(self):
        self.listing_template = 'https://mega-hatsu.com/article-for-sale/page/{}/'
        

    def parse(self, response):
        total_pages = self.get_total_pages(response)
        for page in range(1,total_pages +1 ):
            yield Request(
                self.listing_template.format(page),
                callback = self.parse_individuals
            )

    
    def parse_individuals(self,response):
        individuals_urls = response.css('h5 a::attr(href)').getall()
        for url in individuals_urls :
            yield Request(
                url,
                callback= self.parse_individual
            )


    def parse_individual(self,response):
        loader = ItemLoader(MegaHatsuItem(),response)
        loader.add_value('url',response.url)
        loader.add_xpath('title','string(//h2)')
        loader.add_css('subtitle','div.store-head::text')
        loader.add_css('Map','img.property_img::attr(src)')
        try :
            loader.add_value('sales_price',self.get_price(response.xpath('(//th[contains(text(),"販売価格")]/following-sibling::td)[1]/text()').get()))
        except TypeError : 
            pass
        loader.add_xpath('Yield','(//th[contains(text(),"利回り")]/following-sibling::td)[1]',re='\d+\.\d*')
        loader.add_xpath('property_number','(//th[contains(text(),"物件番号")]/following-sibling::td)[1]/text()')
        loader.add_xpath('installation_location','//table[@class="property_sub_table"]//tr[1]/td/text()')
        loader.add_xpath('number_of_lots_sold','//table[@class="property_sub_table"]//tr[2]/td/text()')
        loader.add_xpath('guarantee','//table[@class="property_sub_table"]//tr[3]/td/text()')
        loader.add_value('system_price',int(bool(response.xpath('//div[@class="row plice_include"]/div[1]/span[@class="active"]'))))
        loader.add_value('land_price_or_rent',int(bool(response.xpath('//div[@class="row plice_include"]/div[2]/span[@class="active"]'))))
        loader.add_value('interconnection_price',int(bool(response.xpath('//div[@class="row plice_include"]/div[3]/span[@class="active"]'))))
        loader.add_value('consumption_tax',int(bool(response.xpath('//div[@class="row plice_include"]/div[4]/span[@class="active"]'))))
        loader.add_value('land_developpement',int(bool(response.xpath('//div[@class="row plice_include"]/div[5]/span[@class="active"]'))))
        loader.add_value('insurrance_cost',int(bool(response.xpath('//div[@class="row plice_include"]/div[6]/span[@class="active"]'))))
        loader.add_value('land_registration',int(bool(response.xpath('//div[@class="row plice_include"]/div[7]/span[@class="active"]'))))
        loader.add_value('weed_prevention_sheet',int(bool(response.xpath('//div[@class="row plice_include"]/div[8]/span[@class="active"]'))))
        loader.add_value('fence',int(bool(response.xpath('//div[@class="row plice_include"]/div[9]/span[@class="active"]'))))
        loader.add_value('sign',int(bool(response.xpath('//div[@class="row plice_include"]/div[10]/span[@class="active"]'))))
        loader.add_value('remote_monitoring',int(bool(response.xpath('//div[@class="row plice_include"]/div[11]/span[@class="active"]'))))
        loader.add_value('construction_costs',int(bool(response.xpath('//div[@class="row plice_include"]/div[12]/span[@class="active"]'))))
        loader.add_xpath('other_costs_and_features','//h3[contains(text(),"そのほかにかかる費用・特徴")]/following-sibling::p/text()')
        loader.add_xpath('manufacturer','//table[@class="property_detail_talbe"][1]//th[contains(text(),"メーカー")]/following-sibling::td/text()')
        loader.add_xpath('total_panel_capacity','//table[@class="property_detail_talbe"][1]//th[contains(text(),"パネル総容量")]/following-sibling::td/text()',re='\d+[,\.\d]*')
        loader.add_xpath('Type','//table[@class="property_detail_talbe"][1]//th[contains(text(),"型式")]/following-sibling::td/text()')
        loader.add_xpath('maximum_output','//table[@class="property_detail_talbe"][1]//th[contains(text(),"最大出力")]/following-sibling::td/text()')
        loader.add_xpath('conversion_efficiency','//table[@class="property_detail_talbe"][1]//th[contains(text(),"変換効率")]/following-sibling::td/text()',re='\d+\.\d*')
        loader.add_xpath('output_guarantee','//table[@class="property_detail_talbe"][1]//th[contains(text(),"出力保証")]/following-sibling::td/text()',re='\d+')
        loader.add_xpath('product_warranty','//table[@class="property_detail_talbe"][1]//th[contains(text(),"製品保証")]/following-sibling::td/text()',re='\d+')
        loader.add_xpath('assumed_investement_surface_yield','string(//p[@class="rate"])',re='\d*\.\d*')
        loader.add_xpath('irr_notes','string(//p[@class="rate_text"])')
        loader.add_xpath('geodetic_point','//th[contains(text(),"観測地点")]/following-sibling::td/text()')
        loader.add_xpath('estimated_annual_power_generation','//th[contains(text(),"年間想定発電量")]/following-sibling::td/text()',re='\d+,\d*')
        loader.add_xpath('unit_price_per_unit_of_electricity_sold','//th[contains(text(),"売電単価（税込）")]/following-sibling::td/text()',re='\d+\.\d*')
        loader.add_xpath('estimated_electricity_sales_revenue','//th[contains(text(),"想定売電収入(年間)")]/following-sibling::td/text()',re='[\d,]+')
        loader.add_xpath('estimated_electricity_sales_income','//th[contains(text(),"想定売電収入(20年)")]/following-sibling::td/text()',re='[\d,]+')
        loader.add_xpath('sales_price2','(//th[contains(text(),"販売価格")]/following-sibling::td/text())[2]',re='[\d,]+')
        loader.add_value('price_notes',' '.join(response.xpath('(//th[contains(text(),"販売価格")]/following-sibling::td/text())[2]').re('\D+')))
        loader.add_xpath('manufacturer2','(//th[contains(text(),"メーカー")]/following-sibling::td/text())[2]')
        loader.add_xpath('model','(//th[contains(text(),"型式")]/following-sibling::td/text())[2]')
        loader.add_xpath('total_capacity_of_power_conditioner','(//th[contains(text(),"パワコン総容量")]/following-sibling::td/text())',re='\d+\.\d*')
        loader.add_xpath('conversion_efficiency','(//th[contains(text(),"変換効率")]/following-sibling::td/text())[2]',re='\d+')
        loader.add_xpath('product_warranty','(//th[contains(text(),"製品保証")]/following-sibling::td/text())[2]')
        loader.add_xpath('carbon_dioxid_emission_reduction','//th[contains(text(),"二酸化炭素排出削減量")]/following-sibling::td/text()')
        loader.add_xpath('conversion_to_cedar_tree','//th[contains(text(),"杉の木に換算")]/following-sibling::td/text()')
        loader.add_value('identifier',response.url.split('/')[-2])
        yield loader.load_item()


    def get_total_pages(self,response):
        return int(max(response.css('span.pages::text').re('\d+')))


    def get_price(self,price_string):
        price = Price.fromstring(price_string).amount
        return float(price)*10**6