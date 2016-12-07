#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-08-15

import argparse
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
    description='remove the domain name in a URL',
    epilog="""
Sample:
$ cat t.txt
map.google.com
mail.google.com

$ ./suffix_clear.py t.txt
map
mail
    """)
parser.add_argument(
    'filename',
    help='The file which include a series of URL you wanna process.',
    type=file)
args = parser.parse_args()
if __name__ == '__main__':
    with open(args.filename.name) as f:
        contents=f.readlines()
        for line in contents:
            print(line.split()[0].split('.')[0])
