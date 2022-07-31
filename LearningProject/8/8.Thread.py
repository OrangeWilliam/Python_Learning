import threading

result=0
lock=threading.Lock()

def foo(index):
    global result;
    for i in range(10**6):
        with lock:
            result+=index

if __name__=="__main__":
    threads=[]
    for i in range(10):
        t1 = threading.Thread(target=lambda : foo(-1))
        threads.append(t1)
        t2 = threading.Thread(target=lambda: foo(1))
        threads.append(t2)

    for i in threads:
        i.start()
    for i in threads:
        i.join()

    print(result)