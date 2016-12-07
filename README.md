# Mydailytools
A series of tools to make my daily workflow more smooth...  

## Overview and Intro
- `converter.py` &emsp;&emsp;&emsp; convert a given string with a constant pattern to a list
```
$ ./converter.py  xxx-xxx-\[1-3\]
xxx-xxx-1
xxx-xxx-2
xxx-xxx-3  

Tips: You can pass many args behind the command
```  

- `suffix_clear.py` &emsp;&emsp;&emsp; remove the suffix of a given strinig with a constant pattern
```
usage: suffix_clear.py [-h] filename

positional arguments:
  filename    The file you wanna clear.

optional arguments:
  -h, --help  show this help message and exit

$ cat t.txt
map.google.com
mail.google.com

$ ./suffix_clear.py t.txt
map
mail
```  

- `rm_key.py` &emsp;&emsp;&emsp; 用来回收跳板机上的用户权限  
```
usage: rm_key.py [-h] [-n NUMBER]

Remove random pubkey of user

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        The amount of pubkey you wanna remove one time,default
                        is 10.
```

- `youdao_vocabulary_notebook.py`
```
usage: youdao_vocabulary_notebook.py [-h] filename

A little tools to help me extract the words which exported from youdao
vocabulary notebook with txt format...

positional arguments:
  filename    The file you wanna process.

optional arguments:
  -h, --help  show this help message and exit
```

- `append-group4MU.sh.tmpl` &emsp;&emsp;&emsp; 用来给产研添加sudo权限,支持多用户  

- `rm-user4MU.sh.tmpl` &emsp;&emsp;&emsp; 用来删除线上用户账户,支持多用户  

- `user-add.sh.tmpl` &emsp;&emsp;&emsp; 用来给产研创建用户，支持多用户         

# Misc

## Overview and Intro
- `chinese_print_issue.py` &emsp;&emsp;&emsp; print含有中文的列表和字典对象的几种方法
- `rockgame.py` &emsp;&emsp;&emsp; 剪子布包锤的py实现
- `eg4multiprocessing.queues` &emsp;&emsp;&emsp; Function as the filename says
- `csv2sqlite.py` &emsp;&emsp;&emsp; Read contact csv file,then write into sqlite db
```
我之前的联系人托管在百度云上的联系人管理，但是该页面没有相应的移动端界面，
在手机上使用很不方便，现在借助Python的Sqlite3模块从csv文件中遍历每一行联
系人并按照自己喜欢的格式进行格式化，真的很方便！我的安卓手机上装了个SQLite
Editor,现在查看和编辑联系人信息就方便多了。手机本地只喜欢存储一些常用的联系人,  
原因国内的App你懂得
```
- `virtualenv_automation.sh` &emsp;&emsp;&emsp; a solution for virtualenv automation used in my zshrc  

- `py4tail.py` &emsp;&emsp;&emsp; The functionality of 'tail -f' cmd and search with a keyword implemented in python  

- `decorator_demo.py` &emsp;&emsp;&emsp; The simple implementation sample of
  decorator in python
