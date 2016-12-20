# Created by sharp.gan at 2016-10-11
alias veact="source .venv/bin/activate"
function veinit(){
    pyversion=$1
    if [ $# -eq 0 ];then
        virtualenv -p python2 .venv
    else
        virtualenv -p python$pyversion .venv
    fi
    if [ $? -ne 0 ];then
        echo -e "Creating py virtual env failed,exit!"
        return 1
    fi
    veact
}
