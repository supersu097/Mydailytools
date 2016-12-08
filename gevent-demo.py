#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-09-02
import time
import multiprocessing
import gevent
from gevent.queue import Queue

tasks = Queue()

print dir(tasks)
def demo():
    i = 0
    while True:
        res = range(1024)[i * 10:(i + 1) * 10]
        if not res:
            break
        tasks.put_nowait(res)
        i += 1

# jobs=[]
# for i in range(10):
#    p=multiprocessing.Process(target=demo)
#    jobs.append(p)
#    p.start()
# work=[gevent.spawn(demo)]#for i in range(3)]
# gevent.joinall(work)

def worker(n):
    for i in tasks:
        task = tasks.get()
        print('Worker %s got task %s' % (n, str(task)))  # + 'type: ' + str(type(task)))
        # time.sleep(1)

        # print('Quitting time!')
"""
gevent.spawn(demo).join()
print len(tasks)

gevent.joinall([
    gevent.spawn(worker, 'jack'),
    gevent.spawn(worker, 'mike'),
    gevent.spawn(worker, 'bob'),
])
"""