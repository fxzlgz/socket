from multiprocessing import Process
from time import sleep,ctime

def fun():
    for i in range(3):
        sleep(2)
        print(ctime())
    

p=Process(target=fun)

#父进程退出，子进程随之退出
p.daemon=True

p.start()
print("Name:",p.name)
print("PID:",p.pid)
print("alive:",p.is_alive())

