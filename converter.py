#!/usr/bin/env python
# coding=utf-8
import sys

if __name__ == '__main__':
    args=sys.argv[1:]
    if len(args) == 0:
        sys.exit("You need to pass at least one arg!\n")
    for arg in args:
        basestr=arg.split('-')
        prefix='-'.join(basestr[:-2])
        range_li=basestr[-2:]
        start_num=int(range_li[0][1:])
        end_num=int(range_li[1][:-1])
        for i in range(start_num,end_num+1):
            print prefix + '-' + str(i)
