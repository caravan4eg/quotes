# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/',
        'http://quotes.toscrape.com/page/4/',
        
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get(),
            item['author'] = quote.css('small.author::text').get(),
            item['tags'] = quote.css('div.tags a.tag::text').getall(),
            yield item
