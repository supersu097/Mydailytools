#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-12-01
import argparse
import time

def tail(fn, keyword):
    handler = open(fn)
    while True:
        new = handler.readline()
        if new:
            if keyword in new:
                yield (keyword, new)
            else:
                time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="The functionality of 'tail -f' cmd and search with a keyword ")
    parser.add_argument(
        '-f', '--filename',
        help='The file name you wanna detect.',
        type=file,
        required=True)
    parser.add_argument(
        '-k','--keyword',
        help='The keyword you wanna search',
        required=True
    )
    args = parser.parse_args()
    for keyword, line in tail(args.filename.name,args.keyword):
        print "Detect {0} in line: {1}".format(keyword,line.rstrip())
