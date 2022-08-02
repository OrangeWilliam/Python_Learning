import time
from greenlet import greenlet

def work1():
    while True:
        print("----work1----")
        gr2.switch()
        time.sleep(2)

def work2():
    while True:
        print("----work2----")
        gr1.switch()
        time.sleep(2)


gr1=greenlet(work1)
gr2=greenlet(work2)
gr1.switch()