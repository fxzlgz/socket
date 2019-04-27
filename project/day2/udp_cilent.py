"""
udp_cilent
"""
from socket import *
HOST="127.0.0.1"
PORT=9999
ADDR=(HOST,PORT)

sockfd=socket(AF_INET,SOCK_DGRAM)
while True:
    data=input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("From server:",msg.decode())
sockfd.close()