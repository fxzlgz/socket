from socket import *
import struct
import pymysql

db=pymysql.connect('localhost','root','123456','eshop')
cursor=db.cursor()

s=socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

st=struct.Struct('i32sif')

while True:
    data,addr=s.recvfrom(1024)
    data=st.unpack(data)
    id=data[0]
    name=data[1].decode()
    age=data[2]
    score=data[3]
    sql="insert into stud values \
        (%d,'%s',%d,%f)"%(id,name,age,score)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
s.close()
db.close()
