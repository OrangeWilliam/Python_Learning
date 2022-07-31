import threading

mutex=threading.Lock()

mutex.acquire()

print("hahah")

mutex.release()