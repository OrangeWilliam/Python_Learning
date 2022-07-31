# 多线程
import random
import time
from threading import Thread
# 多进程
from multiprocessing import Queue,Process

def task1(q):
    for i in ["A","B","C"]:
        print("put %s" % i)
        q.put(i)
        #time.sleep(random.randint(0,10))

def task2(q):
    while True:
        if not q.empty():
            print("get %s" % q.get())
            time.sleep(random.randint(0, 10))
        else:
            print("finish")
            break


if __name__=="__main__":
    q=Queue(3)

    p1=Process(target=task1,args=(q,))
    p2 = Process(target=task2, args=(q,))

    p1.start()
    p2.start()