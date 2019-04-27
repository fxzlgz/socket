import os
from time import sleep

pid=os.fork()#子进程id

if pid<0:
    print("Error")
elif pid==0:
    sleep(2)
    print(os.getpid(),os.getppid())
else:
    print(os.getpid(),pid)
