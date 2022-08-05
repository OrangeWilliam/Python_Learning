from scrapy import cmdline
import os,sys

command="scrapy crawl douban".split()
cmdline.execute(command)