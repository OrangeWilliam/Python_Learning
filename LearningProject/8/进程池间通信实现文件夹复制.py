#coding=gbk
import multiprocessing
import os
#
import random
import time


def copy(dir_name,file_name,q):
    #print("���ڸ����ļ�"+dir_name+"/"+file_name)
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
    # 1.��ȡ��Ҫ���Ƶ��ļ�������
    # 2.��ȡָ���ļ����������ļ���
    # 3.�������̳�
    # 4.ѭ����ʽ����̳����������
    # 5.���̳عر�
    # 6.�ȴ����̳��н��̽���
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
        print("\r����ɣ�%.2f %%" % ((i+1)*100/len(file_name)),end="")


    pool.close()
    #�ص������̲��ͷ���Դ

    pool.join()