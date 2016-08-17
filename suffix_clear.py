#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-08-15

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
    description='')
    parser.add_argument(
    'filename',
    help='The file you wanna clear.',
    type=file)
    args = parser.parse_args()
    with open(args.filename.name) as f:
        contents=f.readlines()
        for line in contents:
            print(line.split()[0].split('.')[0])
