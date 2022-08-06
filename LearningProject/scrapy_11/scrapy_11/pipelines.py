# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy_11.settings import MYSQL_CONF
import pymysql


class Scrapy11Pipeline:
    def __init__(self):
        self.mysql_con=pymysql.connect(**MYSQL_CONF)

    def process_item(self, item, spider):
        if not self.mysql_con:
            self.mysql_conpy = pymysql.connect(spider.settings["MYSQL_CONF"])

        print("数据库连接成功")
        cursor=self.mysql_con.cursor()
        sql=f"""INSERT INTO douban_search (type, name, info, text_area) VALUES ("{item['type']}", "{item['name']}", "{item['rate']}","{item['text_area']}");"""
        try:
            cursor.execute(sql)
            #print(sql)
            self.mysql_con.commit()
        except Exception as e:
            print(sql)
        return item
