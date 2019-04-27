#broad.cast_send,py
from socket import*
from time import sleep

#目标地址
dest=('176.234.11.255',8888)

s=socket(AF_INET,SOCK_DGRAM)

#设置可以发送接手广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,True)
data='''
***************************
4.4 清明前
四月末扶杨柳絮

春风十里不如你
***************************
'''

while True:
    sleep(2)
    s.sendto(data.encode(),dest)

