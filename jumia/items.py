# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JumiaSnItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    #langage = scrapy.Field()
    #fiche_technique = scrapy.Field()
    images_url = scrapy.Field()
    #date = scrapy.Field()
    #pass
