import requests
import time
# 多线程
from threading import Thread
# 多进程
from multiprocessing import Process

result=[]

def request_name(index):
    url = "https://www.baidu.com"
    body = ""
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    resp=requests.get(url=url,headers=headers)
    print("%s : %s " % (index,resp.status_code))
    #result.append(resp)

def sim_cal():
    x=0
    while x<10000000:
        x+=1
    #print("sim_cal finish")

# 如果没有判断入口代码段，多进程程序会报错，windows和pycharm进程阻塞问题
if __name__=="__main__":
    start_time=time.time()
    thread_array=[]
    for i in range(0,10):
        #创建了对象,args是元组
        #t=Process(target=sim_cal,args=(i,))
        t = Thread(target=sim_cal)
        thread_array.append(t)
        #print(t)
        #启动线
        t.start()
    for t in thread_array:
        t.join()
    print("finish")
    end_time = time.time()
    print(end_time-start_time)