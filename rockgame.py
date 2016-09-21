#!/usr/bin/env python3
# coding=utf-8

import random

guess_list = ["石头", "剪刀", "布"]
guize = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]
computer = random.choice(guess_list)
while True:
    people = input('石头,剪刀,布,你要出啥: ')
    if people not in guess_list:
        print('你输的不对,要再输一次哦。。')
        continue
    elif computer == people:
        print("啪。。英雄所见略同呢。。。\n")
        break
    elif [computer, people] in guize:
        print("偶赢了,你个loser!\n")
        break
    else:
        print("你赢了,蒜泥走运。。\n")
        break
