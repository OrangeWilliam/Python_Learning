#coding=gbk
import multiprocessing
import os
#
import random
import time


def copy(dir_name,file_name,q):
    #print("正在复制文件"+dir_name+"/"+file_name)
    time.sleep(random.randint(1,5))
    with open(dir_name+"/"+file_name,"rb") as rf:
        content=""
        os
        while content!=b"":
            content=rf.read(4096)
            with open(dir_name + "_new/" + file_name, "ab+") as wf:
                wf.write(content)

        q.put(file_name)





if __name__=="__main__":
    # 1.获取需要复制的文件夹名称
    # 2.获取指定文件夹下所有文件名
    # 3.创建进程池
    # 4.循环方式向进程池中添加任务
    # 5.进程池关闭
    # 6.等待进程池中进程结束
    dir_name="socket_task"
    os.system("mkdir " + dir_name + "_new")
    file_name=os.listdir(dir_name)

    pool=multiprocessing.Pool(2)
    q=multiprocessing.Manager().Queue()
    for i in file_name:
        pool.apply_async(copy,(dir_name,i,q))

    count=0
    for i in range(len(file_name)):
        q.get()
        print("\r已完成：%.2f %%" % ((i+1)*100/len(file_name)),end="")


    pool.close()
    #回到主进程并释放资源

    pool.join()