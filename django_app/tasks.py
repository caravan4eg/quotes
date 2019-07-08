from __future__ import absolute_import, unicode_literals

import os
import subprocess
from celery import task, shared_task


@shared_task
def mul(x, y):
    print("*** Multiply x and y ****")
    return x * y

# crawl1 
# --------------------------------------------------------------------
from django.core.management import call_command

@task
def crawl1():
    call_command('crawl')
# --------------------------------------------------------------------    

# crawl2
# --------------------------------------------------------------------
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_project.spiders.quotes import QuotesSpider

@shared_task
def crawl2():
    print('***** The crawl task executed *****')
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(QuotesSpider)
    process.start()
# --------------------------------------------------------------------


# # not work
# def crawl():
#     os.environ['SCRAPY_SETTINGS_MODULE'] = 'scrapy_project.settings'
#     return subprocess.call(['scrapy', 'crawl', 'quotes'])