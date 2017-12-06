#!/usr/bin/env python2
# coding=utf-8

"""
sudo: wangjian zhangyu jiangyongjian limingyuan
non-sudo: huangshihong ligeng chizheng tengyalong panqi zhangsihong wenxianchao jiayazhou caiwenduo wuhongzhen
          liangqian pengting

"""
import argparse
import subprocess

parser = argparse.ArgumentParser(
    description="""A tool which is used for Centos to create user account with a default password,
    currently it's 'dingfang8888', and additionally it'll ask the user to renew it for the first log-in.""")
parser.add_argument(
    '-u', '--users',
    required=True,
    nargs='+',
    type=str,
    help='The user(s) you wanna create.')
parser.add_argument(
    '-s', '--sudo',
    action='store_true',
    help="whether the user can prefix the command of 'sudo' to others.")

args = parser.parse_args()
BASE_CMD = "sudo useradd -s /bin/bash -m -d /home/"
for u in args.users:
    if args.sudo:
        subprocess.check_call(BASE_CMD + "{0} -G wheel {0}".format(u),
                              shell=True)
    else:
        subprocess.check_call(BASE_CMD + "{0} {0}".format(u),
                              shell=True)
    print("Created the user of {} successfully.".format(u))
    subprocess.check_call("echo 'dingfang8888' | sudo passwd --stdin {}".format(u),
                          shell=True)
    subprocess.check_call("sudo chage -d 0 " + u, shell=True)
    print("Expired the user's password successfully.")
