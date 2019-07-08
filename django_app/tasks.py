from __future__ import absolute_import, unicode_literals

import os
import subprocess
from celery import task, shared_task


@shared_task
def mul(x, y):
    print("Multiply x and y")
    return x * y

# @task
# def crawl():
#     os.environ['SCRAPY_SETTINGS_MODULE'] = 'crawler.hackernews.settings'
#     return subprocess.call(['scrapy', 'crawl', 'hnews'])