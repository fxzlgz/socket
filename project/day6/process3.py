from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I;m %s"%name)
        print("I'm working...")

p=Process(target=worker,args=(2,"wesa"))
p.start()
p.join()

