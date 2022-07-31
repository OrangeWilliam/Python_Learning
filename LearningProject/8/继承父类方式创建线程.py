import threading
import socket
import time


class UDP(threading.Thread):
    def run(self):
        while True:
            print(self.name )
            print("1111")
            time.sleep(1)
            self.xx()

    def xx(self):
        pass

if __name__=='__main__':
    t_udp=UDP()
    t_udp.start()

    while True:
        print("main")
        time.sleep(1)