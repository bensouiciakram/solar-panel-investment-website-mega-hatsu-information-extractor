import scrapy


class InfosSpider(scrapy.Spider):
    name = 'infos'
    allowed_domains = ['mega-hatsu.com']
    start_urls = ['http://mega-hatsu.com/']

    def parse(self, response):
        pass
