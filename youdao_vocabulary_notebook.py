#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-09-21

import argparse
from bs4 import BeautifulSoup

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A little tool to help me extract the words list in a xml'
        'format file which exported from youdao vocabulary notebook,notice'
        'that the file itself must be with the xml format...') 
    parser.add_argument(
        'filename',
        help='The file you wanna process.',
        type=file)
    args = parser.parse_args()
    soup=BeautifulSoup(open(args.filename.name),'html5lib')
    with open('words.txt','w') as w:
        for j in soup.find_all('word'):
            w.write(j.get_text() + '\n')

