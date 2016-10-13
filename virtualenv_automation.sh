# Created by sharp.gan at 2016-10-11
alias virtualenv="/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/bin/virtualenv"
alias veact="source venv/bin/activate"
function veinit(){
    projectname=$1
    if [ $# -eq 0 -o $# -gt 1 ];then
        echo -e "The args of project name you passed can not be 0 or greater than 1!\n"
        return 1
    fi
    mkdir $projectname
    cd $projectname
    virtualenv venv
    if [ $? -ne 0 ];then
        echo -e "Last comand failed,eixt!"
        return 1
    fi
    source venv/bin/activate
}
