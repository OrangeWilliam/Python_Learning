import socket
#1.创建套接字
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.连接服务器
client_socket.connect(("127.0.0.1",6666))
#3.向服务器发送数据，接收返回
input_data=input("输入文件名:")
client_socket.send(input_data.encode("GBK"))
with open("copy_"+input_data,'wb') as f:
    count=0
    while True:
        rec_data=client_socket.recv(1024)
        #思路，如果读取到的文件内容为空，代表读取完成，还有一种思路通过判断文件大小
        if rec_data!=b'':
            f.write(rec_data)
            count+=1
            print(f"已经下载了：{count}次")
        else:
            break
#4.断开连接
client_socket.close()