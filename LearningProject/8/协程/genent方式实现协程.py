import gevent
from gevent import monkey

#打补丁，配合time.sleep()使用，替代gevent.sleep(1)实现延时并切换任务
monkey.patch_all()

def func(a,b):
    for i in range(a,b):
        print(gevent.getcurrent(),i)
        # 遇到gevent所认为的耗时操作时，会把时间拿出来做另外的任务，以实现多任务
        gevent.sleep(1)

# g1=gevent.spawn(func,0,5)
# g2=gevent.spawn(func,5,10)
# g3=gevent.spawn(func,10,15)
# g1.join()
# g2.join()
# g3.join()

gevent.joinall([
    gevent.spawn(func,0,5),
    gevent.spawn(func,5,10),
    gevent.spawn(func,11,15),
])