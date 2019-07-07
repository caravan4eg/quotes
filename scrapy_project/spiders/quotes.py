# -*- coding: utf-8 -*-
# TODO: Creating a new Scrapy project
# TODO: Writing a spider to crawl a site and extract data
# TODO: Exporting the scraped data using the command line
# TODO: Changing spider to recursively follow links
# TODO: Using spider arguments

import scrapy
from scrapy_project.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get(),
            item['author'] = quote.css('small.author::text').get(),
            item['tags'] = quote.css('div.tags a.tag::text').getall(),
            yield item
