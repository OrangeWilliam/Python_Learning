import time

def work1():
    while True:
        print("----work1----")
        yield
        time.sleep(5)
        print("----work1.1----")

def work2():
    while True:
        print("----work2----")
        yield
        time.sleep(5)
        print("----work2.1----")

if __name__=="__main__":
    w1=work1()#生成器返回对象，并不会执行函数
    w2=work2()
    while True:
        next(w1)#执行到yield为止，下一次执行从time.sleep()开始
        next(w2)