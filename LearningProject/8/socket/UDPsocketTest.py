import socket

#UDP连接
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("16.24.40.198",6666))#不写ip会自动指定网卡（不同的本地ip）
send_str=input("请输入：")

s.sendto(send_str.encode("gbk"),("16.24.33.208",8888))
rec=s.recvfrom(1024)
print(f"{rec[1][0]}:{rec[1][1]}>>>{rec[0].decode('gbk')}")
s.close()