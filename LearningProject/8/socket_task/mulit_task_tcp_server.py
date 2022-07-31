import threading
import socket
import time


class HandleData(threading.Thread):
    def __init__(self, new_s):
        super().__init__()
        self.new_s = new_s

    def run(self):
        while True:
            content = self.new_s.recv(4096)
            if content != b"":
                print(content)
                self.new_s.send(content)
            else:
                self.new_s.close()
                break

class TCPSever(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(("", self.port))
        self.s.listen(128)

    def run(self):
        while True:
            new_socket, ipinfo = self.s.accept()
            print(ipinfo)
            hd = HandleData(new_socket)
            hd.start()

    def __del__(self):
        self.s.close()


if __name__ == '__main__':
    tcp_s = TCPSever(6666)
    tcp_s.start()
    while True:
        print(threading.enumerate())
        time.sleep(1)
