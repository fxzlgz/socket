import os
from time import sleep

pid=os.fork()

if pid==0:
    print(os.getpid())
    os._exit(0)
else:
    print("长点心")
    while True:
        pass
