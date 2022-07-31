import socket

# 1.创建套接字
# 2.绑定信息
# 3.功能选择：
#     1.发送；输入ip，port；输入发送内容；sendto
#     2.接收：receivefrom

#IPV4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定信息
s.bind(("",6666))

#最大接收1024byte=1kb
data,info=(b"",())

while True:
    func_choice = input("请输入想要选择的功能(1/2/3)：")
    if func_choice == "1":
        ip_input = input("请输入ip：")
        port_input = input("请输入port：")
        data_input = input("请输入内容：")

        s.sendto(data_input.encode("utf-8"),(ip_input,int(port_input)))
    elif func_choice == "2":
        # 元组的拆包
        rev_data,rev_info = s.recvfrom(1024)
        try:
            rev_data_str = rev_data.decode('gbk')
        except Exception as e:
            print(e.args)
            rev_data_str = rev_data.decode('utf-8')
        finally:
            print(f"{rev_info[0]}:{rev_info[1]}-->{rev_data_str}")
    elif func_choice == '3':
        break;
    else:
        print("输入错误请重试！")


s.close()