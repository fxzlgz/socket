import os
from time import sleep

pid=os.fork()

if pid<0:
    print("Error")
elif pid==0:
    sleep(3)
    print("Child %d process exit"%os.getpid())
    os._exit(1)
else:
    #pid,status=os.wait()
    pid,status=os.waitpid(-1,os.WNOHANG)#非阻塞模式
    print("pid:",pid)
    print("status:",status)
    while True:
        sleep(100)


