#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-09-21

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A little tools to help me extract the words '
        'which exported from youdao vocabulary notebook'
        ' with txt format...') 
    parser.add_argument(
        'filename',
        help='The file you wanna process.',
        type=file)
    args = parser.parse_args()
    data=[]
    with open(args.filename.name) as r:
        for i in r:
            line=i.split(',')[1]
            if '[' in line:
                data.append((line.split('[')[0].strip()))
            elif '\n' in line:
                data.append((line.split('\n')[0].strip()))
    with open('words.txt','w') as w:
        for j in data:
            w.write(j + '\n')
