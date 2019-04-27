from socket import *
import os, sys
import signal

HOST = '0.0.0.0'
PROT = 8888
ADDR = (HOST, PROT)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 8888....")


def cilent_handle():
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("\n服务器退出")
    except Exception as e:
        print(e)
        continue

    pid = os.fork()
    if pid == 0:
        s.close()
        cilent_handle()
        os._exit(0)
    else:
        c.close()
        continue



