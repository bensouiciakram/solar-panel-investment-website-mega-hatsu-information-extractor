# Scrapy settings for mega_hatsu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mega_hatsu'

SPIDER_MODULES = ['mega_hatsu.spiders']
NEWSPIDER_MODULE = 'mega_hatsu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mega_hatsu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mega_hatsu.middlewares.MegaHatsuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'mega_hatsu.middlewares.MegaHatsuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'mega_hatsu.pipelines.MegaHatsuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'


FEED_EXPORTERS = {
    'xlsx': 'scrapy_xlsx.XlsxItemExporter',
}


POSTGRES_USER = 'bensouici'
POSTGRES_PASS = '1993'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_DB = 'test_db'
POSTGRES_TABLE = 'articles'


FEED_EXPORT_FIELDS = [
    'property_number',
    'unit_price_per_unit_of_electricity_sold',
    'total_capacity_of_power_conditioner',
    'total_panel_capacity',
    'Map',
    'Type',
    'Yield',
    'assumed_investement_surface_yield',
    'carbon_dioxid_emission_reduction',
    'construction_costs',
    'consumption_tax',
    'conversion_efficiency',
    'conversion_to_cedar_tree',
    'estimated_annual_power_generation',
    'estimated_electricity_sales_income',
    'estimated_electricity_sales_revenue',
    'fence',
    'geodetic_point',
    'guarantee',
    'identifier',
    'installation_location',
    'insurrance_cost',
    'interconnection_price',
    'irr_notes',
    'land_developpement',
    'land_price_or_rent',
    'land_registration',
    'manufacturer',
    'manufacturer2',
    'maximum_output',
    'model',
    'number_of_lots_sold',
    'other_costs_and_features',
    'output_guarantee',
    'price_notes',
    'product_warranty',
    'property_number',
    'remote_monitoring',

    'sales_price2',
    'sign',
    'status',
    'subtitle',
    'system_price',
    'title',

    'url',
    'weed_prevention_sheet'
]