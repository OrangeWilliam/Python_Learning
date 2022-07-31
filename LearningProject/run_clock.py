import time

def run_clock(func):
    def wapper(*args, **kwargs):
        startTime = time.time()
        result=func(*args, **kwargs)
        endTime=time.time()
        run_time=format(endTime-startTime,".2f")
        print(f"执行时间：{run_time}s")
        return result
    return wapper