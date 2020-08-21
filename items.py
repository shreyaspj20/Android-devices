# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MobileItem(scrapy.Item):
     name = scrapy.Field()
     memory = scrapy.Field()
     display = scrapy.Field()
     camera = scrapy.Field()
     battery = scrapy.Field()
     processor = scrapy.Field()
     warranty = scrapy.Field()
     rating = scrapy.Field()
     reviews = scrapy.Field()
     price = scrapy.Field()
     pass
