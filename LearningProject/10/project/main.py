import random

import pymysql
import requests
from setting import MYSQL_CONF
from search import parse_douban_result
from run_clock import run_clock
from threading import Thread
from multiprocessing import Process

#持久化结果
def saver(content):
    mysql_con = pymysql.connect(**MYSQL_CONF)
    SQL=f"INSERT INTO douban_search (type,name,info,text_area) values (%s,%s,%s,%s)"
    cursor=mysql_con.cursor()
    rows=cursor.executemany(SQL,content)
    mysql_con.commit()
    cursor.close()
    return rows

#请求网址
def downloader(keyword):
    url="https://www.douban.com/search"
    params= {
        "q":keyword,
    }
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    req=requests.request("GET",url,params=params,headers=headers)
    return req.text

def nextMain(task):
    result_html = downloader(task)
    result_set = parse_douban_result(result_html)
    result_rows = saver(result_set)
    print(f"{task}：affected {result_rows} rows")
    #return result_rows

#主函数，任务调度
@run_clock
def main(task_array):
    threads=[]
    for task in task_array:
        t=Thread(target=nextMain,args=(task,))
        threads.append(t)
        t.start()

    #for t in threads:
       # t.start()

    for t in threads:
        t.join()





if __name__=="__main__":
    #用来代替生产者

        task_list=['你好李焕英','羞羞的铁拳','西虹市首富','夏洛特烦恼']
        main(task_list)