# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Untitled2Item(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    #product_price = scrapy.Field()
    product_reviews = scrapy.Field()
    product_ratings = scrapy.Field()
    pass
