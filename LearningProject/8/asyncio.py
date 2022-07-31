import asyncio
import time

class Resp:
    status_code=200


def send_req(index):
    print("模拟发送请求：",index)
    resp=Resp()
    time.sleep(3)
    print(f"req index : {index},resp:{resp.status_code}")
    return resp.status_code

result=send_req(1)


