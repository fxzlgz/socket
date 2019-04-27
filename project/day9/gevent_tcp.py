import gevent
from gevent import monkey
monkey.patch_all()

from socket import *

ADDR=('0.0.0.0',8888)
s=socket()
s.bind(ADDR)
s.listen(3)
while True:
    c,addr=s._accept()
    print("Connect from",addr)
    gevent.spawn(handler,c)
s.close()

def handler(c):
    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"ok")
    c.close()
