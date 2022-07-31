import socket
import threading
import time
#UDP连接
#s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#设置UDP套接字允许广播
#dest_addr = ("<broadcast>", 2425)
dest_addr = ("16.24.33.208", 2425)
#不写ip会自动指定网卡（不同的本地ip）

#版本：消息序号：用户名：电脑名：功能（32表示发送消息）：发送的内容
USERNAME="小明"
PCNAME="水果电脑"
def send_msg(s):
    while True:
        id=123456798
        msg_input = input(f"{USERNAME}({PCNAME})：\n")
        id = str(id + 1)
        msg = "1:" + id + ":小明:水果电脑:32:"
        s.sendto((msg + msg_input).encode("GBK"), dest_addr)

def recive_msg(s):
    while True:
        data, info = s.recvfrom(1024)
        rec_data_list = data.decode("GBK").split(":")
        #print("rec", rec_data_list, info)
        if (rec_data_list[4] == "288"):
            # 版本：消息序号：用户名：电脑名：功能（32表示发送消息）：发送的内容
            version = rec_data_list[0]
            id = rec_data_list[1]
            username = rec_data_list[2]
            pcname = rec_data_list[3]
            func = rec_data_list[4]
            content = rec_data_list[5]
            print(f"{username}({pcname}):\n{content}")
            retMsg = (version + ":" + id + ":" + username + ":" + pcname + ":33:" + id).encode("gbk") + b'\x00'
            # s.sendto(data, dest_addr)
            s.sendto(retMsg, dest_addr)
            # print("send",data)
            # print("send",retMsg)


if __name__=="__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(("", 2425))
    t1 = threading.Thread(target=send_msg,args=(s,))
    t2 = threading.Thread(target=recive_msg,args=(s,))
    t1.start()
    t2.start()