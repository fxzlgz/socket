from select import select
from socket import *

#创建套接字作为关注IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)

#添加到关注列表
rlist=[s]
wlist=[]
xlist=[]



while True:
    #监控IO
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
           c,addr=r.accept()
           print("Connect from",addr)
           #客户端套接字加入到列表
           rlist.append(c)
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            #r.send(b'ok')
            #将r放到wlist中希望主动处理
            wlist.append(r)

    for w in ws:
       w.send(b'OK')
       wlist.remove(w)

    for x in xs:
        pass
    

