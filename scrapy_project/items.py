# scrapy_project/items.py
import scrapy


class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    tags = scrapy.Field()
    author = scrapy.Field()

