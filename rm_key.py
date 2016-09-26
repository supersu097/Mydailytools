#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-08-29
import random
import subprocess
import argparse
import pprint
import config
import datetime


def random_del(number):
    still_alive = subprocess.check_output(
        'find /home/ -name authorized_keys', shell=True).split()
    if len(still_alive) < number:
        exit('The amount of the existing pubkey is {0}, '
             'it is less than the number you wanna remove one time,\n'
             'Pls specify a new number passed with arg of -n|--number!'.format(len(still_alive)))
    try:
        for i in config.ignore_item:
            still_alive.remove('/home/{0}/.ssh/authorized_keys'.format(i))
    except ValueError:
        print 'Ignore...'

    if len(still_alive) ==0:
        exit("All users' perm  cleared except that need to be ignored!")

    try:
        with open('record.log', 'a+') as record:
            for i in range(number):
                random_path = random.choice(still_alive)
                random_user = random_path.split('/')[2]
                subprocess.check_call('mv -v {path} '
                                      '/root/keys/{user}'
                                      '_authorized_keys'.format(
                                          path=random_path, user=random_user),
                                      shell=True)
                record.write(str(datetime.date.today()) + ': '
                             + '[{0}]'.format(random_user) + ' pubkey removed...\n')
    except subprocess.CalledProcessError as e:
        print("Unkonwn error occured: " + str(e))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Remove random pubkey of user')
    parser.add_argument(
        '-n', '--number',
        help='The amount of pubkey you wanna remove one time,default is 10',
        default=10,
        type=int)
    args = parser.parse_args()
    random_del(args.number)
