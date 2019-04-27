import gevent

def foo(a,b):
    print(a,b)
    gevent.sleep(2)
    print("dasjas")

def bar():
    print("akdljd")
    gevent.sleep(2)
    print("sadhhs")

f=gevent.spawn(foo,1,2)
g=gevent.spawn(bar)

gevent.joinall([f,g])
print("==========")
