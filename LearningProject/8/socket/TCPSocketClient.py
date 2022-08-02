import socket
#1.创建套接字
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.连接服务器
client_socket.connect(("127.0.0.1",6666))
#3.向服务器发送数据，接收返回
input_data=input("输入:")
client_socket.send(input_data.encode("GBK"))

rec_data=client_socket.recv(1024)
print(rec_data.decode("GBK"))
#4.断开连接
client_socket.close()