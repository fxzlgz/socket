from socket import*
from select import select

f=open('mvc.jpg')

s=socket()
s.bind(('127.0.0.1',8888))
s.listen(3)
print("监控IO")
rs,ws,xs=select([s],[],[f],3)
print(rs)
print(ws)
print(xs)
