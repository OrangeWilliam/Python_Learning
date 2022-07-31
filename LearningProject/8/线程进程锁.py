import threading

g_num=0

def task1(num,m):
    global g_num
    for i in range(num):
        m.acquire()
        g_num += 1
        m.release()
    print(f"task2:{g_num}")

def task2(num,m):
    global g_num

    #with lock:
    for i in range(num):
        m.acquire()
        g_num+=1
        m.release()
    print(f"task2:{g_num}")

mutex=threading.Lock()

t1=threading.Thread(target=task1,args=(10000000,mutex))
t2=threading.Thread(target=task2,args=(10000000,mutex))

t1.start()
t2.start()