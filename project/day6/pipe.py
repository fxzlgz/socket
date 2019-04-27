from multiprocessing import Process,Pipe 
import time,os

#创建管道
fd1,fd2=Pipe()

def fun(name):
    time.sleep(3)
    #写入管道
    fd1.send({name:os.getpid()})

jobs=[]
for i in range(5):
    p=Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    #读取管道
    data=fd2.recv()
    print(data)

for i in jobs:
    i.join()


 

