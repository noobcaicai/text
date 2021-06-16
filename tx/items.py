# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TxItem(scrapy.Item):
    # define the fields for your item here like:
    images_url = scrapy.Field()
    name=scrapy.Field()
    heroId=scrapy.Field()
    images = scrapy.Field()