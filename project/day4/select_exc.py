from select import select
from socket import*
import sys
from time import ctime

f=open('log.txt','a')

s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

rlist=[s,sys.stdin]
wlist=[]
xlist=[]

while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is rs:
            c,addr=r.accept()
            rlist.append(c)
        elif r is sys.stdin:
            name='Server'
            time=ctime()
            mag=r.readline()
            f.write("%s %s %s\n"%(name,ctime,msg))
            f.flush()
        else:
            addr=r.getpeername()
            time=ctime()
            msg=r.recv(1024).decode()
            f.write("%s %s %s\n"%(addr,time,msg))
            f.flush()
f.close()
s.close()