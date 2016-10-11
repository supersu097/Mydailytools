#!/usr/bin/env bash
# Created by sharp.gan at 2016-10-11
projectname=$1
if [ $# -eq 0 -o $# -gt 1 ];then
    echo -e "The args of project name you passed can not be 0 or greater than 1!\n"
    exit 1
fi
mkdir $projectname
cd $projectname
virtualenv venv
. venv/bin/activate
