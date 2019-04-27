"""
udp_server.py
"""
from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
server_addr=("0.0.0.0",9999)
sockfd.bind(server_addr)
while True:
    try:
        data,addr=sockfd.recvfrom(1024)
    except KeyboardInterrupt:
        print("server exit")
        break
    print("Receive from %s:%s"%(addr,data.decode()))
    sockfd.sendto(b"Tanks for your msg",addr)

sockfd.close()