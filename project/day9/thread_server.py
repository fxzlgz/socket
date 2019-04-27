from socket import *
from threading import Thread
import sys


ADDR = ('0.0.0.0', 8888)
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(ADDR)
sockfd.listen(5)


def handle_request(connfd):
    print("Connect from", connfd.getpeername())
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        connfd.send(b"Receive your message")
    connfd.close()


while True:
    try:
        c, addr = sockfd.accept()
    except KeyboardInterrupt:
        sockfd.close()
        sys.exit("系统退出")
    except Exception as e:
        print(e)
        continue

    t = Thread(target=handle_request, args=(c ,))
    t.start()
    t.setDaemon(True)
