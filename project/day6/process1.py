import multiprocessing as mp 
from time import sleep
a=1

#编写进程函数
def fun():
    sleep(3)
    global a
    print(a)
    a=100
    print("子进程执行事件")

#创建进程对象
p=mp.Process(target=fun)
#启动进程
p.start()
sleep(2)
print("父进程执行时间")

#回收进程
p.join()
print("***********")
print(a)