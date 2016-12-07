#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-12-01
import time
def freak_func(func):
    def wrapper():
        first=time.time()
        func()
        second=time.time()
        diff=second - first
        if diff > 1:
            print "Warning: The func of {0} run too fucking long.".format(func.func_name)
    return wrapper

@freak_func
def normal_func():
    li=[_ for _ in range(10000)]
    time.sleep(1)

if __name__ == '__main__':
    normal_func()
