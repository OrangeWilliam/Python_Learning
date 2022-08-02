import socket
# 1.创建套接字
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.绑定本地信息
server_socket.bind(("",6666))
# 3.将套接字由默认的主动连接模式改为被动模式（监听模块）
server_socket.listen(128)
# 4.等待客户端连接,阻塞，连接后,accept返回一个新的套接字元组
new_sock,client_info=server_socket.accept()
print(client_info)
filename=new_sock.recv(1024)
print("要下载的文件名：",filename)
with open(filename,'rb') as f:
    count=0
    while True:
        content = f.read(1024)
        if content != b'':
            new_sock.send(content)
            count+=1
            print(f"正在传输：{count}次")
        else:
            new_sock.close()
            break;
server_socket.close()



