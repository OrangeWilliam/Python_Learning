import multiprocessing
import os
import random
import time

def worker(num):
    #for i in range(5):
    print("pid----%d---num----%d"%(os.getpid(),num))
    time.sleep(1)

if __name__=="__main__":
    pool=multiprocessing.Pool(3)

    for i in range(10):
        print(i)
        #向进程中添加任务
        #注意：如果日安家的任务数量超过了进程池中的个数，那么就不会接着往进程池中添加，
        #   如果还没有执行，会等待前面的进程结束然后再添加新进程
        pool.apply_async(worker,(i,))

    pool.close()
    #回到主进程并释放资源
    pool.join()