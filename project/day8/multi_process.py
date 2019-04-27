from test import*
import multiprocessing as mp
import time 

jobs=[]
t=time.time()
for i in range(10):
    p=mp.Process(target=io)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()(),args=(1,1
print(time.time()-t)