"""
进程的理解及使用；
多任务编程，多进程
"""

import os, random, time
from multiprocessing import Process

a = 1


def add_1(obj: int):
    print('hello')
    time.sleep(2)
    print('world')
    return obj + 1


p = Process(target=add_1, args=(1,), kwargs=dict())
p.start()
print(a)
print(p.name)
print(p.pid)
print(p.is_alive())
time.sleep(1)
print(p.join())
print(p.__dict__)
print(dir(p))
print(p.is_alive())

