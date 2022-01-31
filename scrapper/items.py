# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
     items_name= scrapy.Field()
     #items_description= scrapy.Field()
     items_price= scrapy.Field()
     items_old_price= scrapy.Field()
     items_manufacturer= scrapy.Field()
     #items_weight= scrapy.Field()
     items_availability= scrapy.Field()

    

    

