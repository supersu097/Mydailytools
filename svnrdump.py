#!/usr/bin/env python2
# coding=utf-8

import os
import subprocess


def cmd_generator(option, path):
    return "svnrdump dump svn://106.14.248.127/projects {op} > {pa}/svn_backup.dump".format(op=option, pa=path)


DUMPED_PATH = "/home/internal-server/backup"
if not os.path.isfile(DUMPED_PATH + "svn_backup.dump"):
    subprocess.check_call(cmd_generator('', DUMPED_PATH), shell=True)
else:
    subprocess.check_call(cmd_generator('--incremental', DUMPED_PATH), shell=True)
