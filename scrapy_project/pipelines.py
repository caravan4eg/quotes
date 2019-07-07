# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error
from scrapy.exceptions import DropItem


class QuoteItemPipeline(object):
    """Save extracted data to database"""

    def open_spider(self, spider):
        # Connect to database
        try:    
            self.connection = sqlite3.connect("db.sqlite3")
                                        
            if self.connection:
                self.cur = self.connection.cursor()
                spider.log(f'Connection to database is OK!')
            else:
                spider.log('Error! Cursor not found!')
        except Exception as ex:
            print(ex)


    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()


    def process_item(self, item, spider):
        """ Checks and saves data to database """
 
        try:
            self.cur.execute("INSERT OR IGNORE INTO django_app_quote (tags, author, text)\
                VALUES (?, ?, ?)", (str(item['tags'][0]), item['author'][0], item['text'][0]))
                # self.cursor.execute(
                # "insert into myscrapedata (url, desc) values (?, ?)",
                #     (item['url'][0], item['desc'][0])
                            
            spider.log('Item added to db. OK!')
            
        except Exception as ex:
            # Returns back transaction if is there a problem with saving
            self.cur.execute("rollback")
            spider.log('Something went wrong!\
                            Error by saving to db: %s' % ex)
                
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        self.connection.commit()
        return item