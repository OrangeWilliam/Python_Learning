import queue
import threading
import socket

DEST_ADDR = ("127.0.0.1", 8888)


class saver(threading.Thread):
    def __init__(self, s_q):
        super().__init__()
        self.s_queue = s_q

    def run(self):
        while True:
            with open("r.txt", "ab") as f:
                f.write(self.s_queue.get()+'\n'.encode("GBK"))

class sender(threading.Thread):
    def __init__(self, s, s_q):
        super().__init__()
        self.s = s
        self.s_q = s_queue

    def run(self):
        while True:
            input_text = input("输入：")
            self.s.sendto(input_text.encode("GBK"), DEST_ADDR)
            self.s_q.put("send:".encode("GBK") + input_text.encode("GBK"))


class reciver(threading.Thread):
    def __init__(self, s, s_q):
        super().__init__()
        self.s = s
        self.s_q = s_queue

    def run(self):
        while True:
            recv_data, info = self.s.recvfrom(1024)
            print(recv_data)
            self.s_q.put("recv:".encode("GBK") + recv_data)


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 6666))
    s_queue = queue.Queue()
    r = reciver(s, s_queue)
    s = sender(s, s_queue)
    w = saver(s_queue)

    r.start()
    w.start()
    s.start()
