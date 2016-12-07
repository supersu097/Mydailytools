#!/usr/bin/env python
# coding=utf-8
import sys
import argparse
parser = argparse.ArgumentParser(
    description='Convert a given string with a constant pattern to a human '
    'readable status',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Sample:
$ ./converter.py  xxx-xxx-\[1-3\]
xxx-xxx-1
xxx-xxx-2
xxx-xxx-3

Tips: You can pass many args behind the command    
    
    """)
parser.add_argument(
    'hostname_pattern',
    help='',
    type=str,
    nargs='+')
args = parser.parse_args()
if __name__ == '__main__':
    for arg in args.hostname_pattern:
        basestr=arg.split('-')
        prefix='-'.join(basestr[:-2])
        range_li=basestr[-2:]
        start_num=int(range_li[0][1:])
        end_num=int(range_li[1][:-1])
        for i in range(start_num,end_num+1):
            print prefix + '-' + str(i)
