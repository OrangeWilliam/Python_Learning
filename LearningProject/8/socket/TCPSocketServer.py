import socket
# 1.创建套接字
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.绑定本地信息
server_socket.bind(("",6667))
# 3.将套接字由默认的主动连接模式改为被动模式（监听模块）
server_socket.listen(128)
# 4.等待客户端连接,阻塞，连接后,accept返回一个新的套接字元组
new_sock,client_info=server_socket.accept()
print(client_info)
while True:
    # 5.接收/发送数据，阻塞，客户端接收到数据后
    rec=new_sock.recv(1024)
    #如果长度为0.表示客户端关闭了连接
    if(len(rec)!=0):
        print(rec.decode("GBK"))
        send_data='我收到了'
        send=new_sock.send(send_data.encode("GBK"))
    else:
        # 6.关闭连接
        new_sock.close()
        break
server_socket.close()



