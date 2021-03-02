"""
线程的理解及使用；
多任务编程，多线程
队列queue的使用
"""
# 　阿里面试题（多线程）
# 创建两个线程，其中一个输出1-26，另外一个输出A-Z。输出格式要求：1A 2B 3C 4D

import os, random, time
import string
from threading import Thread
from threading import Lock
from queue import Queue

thread_lock = Lock()
work_queue = Queue(26)
num = list(range(1, 27))
letters = string.ascii_uppercase

flag = 0
wait = 1


def print_some(obj, q):
    global flag, wait
    while not flag:
        import time
        # thread_lock.acquire()
        time.sleep(0.01)
        if not wait:
            continue
        if q.empty():
            index = 0
            # print('empty')
        else:
            index = q.get()
        if index >= 26:
            flag = 1
            break
        print(obj[index], sep=' ', end=' ')
        work_queue.put(index)
        # print('put_old',index)
        wait = 0
        # thread_lock.release()


def print_some_(obj, q):
    global flag, wait
    while not flag:
        # thread_lock.acquire()
        import time
        time.sleep(0.01)
        # thread_lock.acquire()
        if q.empty():
            # print('-,empty')
            break
        else:
            if wait:
                continue
            index = q.get()
        if index >= 26:
            flag = 1
            break
        print(obj[index])
        new_index = index + 1
        work_queue.put(new_index)
        wait = 1
        # print('put_new',new_index)
        # thread_lock.release()


class MyThread(Thread):
    def __init__(self, func, *args, **kwargs):
        Thread.__init__(self, target=func, args=args, kwargs=kwargs)

    def run(self) -> None:
        # print('start')
        # thread_lock.acquire()
        # print(self.getName())
        Thread.run(self)
        # thread_lock.release()
        # print(self.getName(), self.is_alive())
        # print('end')
        return


# t1 = MyThread(print_some, num, work_queue)
# t2 = MyThread(print_some_, letters, work_queue)
# t1.start()
# t2.start()
# t1.join()
# t2.join()


def eat_something(people):
    print(F'{people} eat')
    time.sleep(0.5)
    print(F'{people} 洗手')
    time.sleep(1)
    print(F'{people} drink')
    return


class NewThread(Thread):
    def __init__(self, name, people):
        Thread.__init__(self)
        self.name = name
        self.people = people

    def run(self) -> None:
        print(F'{self.name}落座')
        eat_something(self.people)
        print(F'{self.name}离席')
        return


t1 = NewThread('thread-1', '张三')
t2 = NewThread('thread-2', '李四')
# # TODO 还没吃完，结账人先走了
# t1.start()
# t2.start()
# time.sleep(0.1)
# print('请客人结账走人')
#
# # TODO 吃好还没喝好
# t1.setDaemon(True)
# t2.setDaemon(True)
# t1.start()
# t2.start()
# time.sleep(0.1)
# print('请客人结账走人')


# TODO 等人吃饱喝足，结账走人
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
# t1.join(0.2)  # 子线程超时时间，默认无,若超时未结束则进行下一步
t1.join()
print('1')
# t2.join(0.2)
t2.join()
print('2')
time.sleep(0.6)
print('请客人结账走人')
