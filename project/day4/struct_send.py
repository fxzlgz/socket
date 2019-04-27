from socket import *
import struct

fmt='i32sif'


s=socket(AF_INET,SOCK_DGRAM)
HOST="127.0.0.1"
PORT=8888
ADDR=(HOST,PORT)


while True:
    print("\n***************")
    id=int(input("ID:"))
    name=input("name:")
    age=int(input("age:"))
    score=float(input("score:"))
    
    data=struct.pack(fmt,id,name.encode(),age,score)
    s.sendto(data,ADDR)
s.close()