#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2017-01-08
import os
import argparse
import subprocess

# Assume that you already installed the dependency of GNU-gettext, or you need to
# resolve this using your system package management tool such as `sudo apt
# install gettext`


# main process of resloving the problem
def process(new_po):
    # find the untranslated part
    subprocess.check_call('msgattrib --untranslated new_fr_django.po > '
                          'new_untrans.po', shell=True)
    # find the translated part
    subprocess.check_call('msgattrib --translated old_fr_django.po '
                          '> old_trans.po', shell=True)
    # find the common part of above
    subprocess.check_call('msgcomm old_trans.po new_untrans.po -o '
                          'new2old_trans.po', shell=True)
    # start to merge and generate new .PO file we want
    subprocess.check_call('msgmerge -N new2old_trans.po new_fr_django.po '
                          '-o {}'.format(new_po), shell=True)


# clean the unneeded intermediate file
def clean():
    for f in ['new_untrans.po', 'old_trans.po', 'new2old_trans.po']:
        os.remove(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A tool that help you generate new translaton .PO file from '
                    'old!')
    parser.add_argument(
        '-n', '--new',
        default='fr_django.po',
        type=str,
        help='The new translation .PO filename you want, by default is'
                ' fr_django.po')
    args = parser.parse_args()
    print('Now we start to process, wait~')
    process(args.new)
    clean()
    print('\nThe new .PO translation file of {} is already in your '
          'current directory, please check!'.format(args.new))
