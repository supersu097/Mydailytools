# Mydailytools
Function as the repo name

## Intro
- converter.py ----- convert a given string with a constant pattern to a list
```
$ ./converter.py  xxx-xxx-\[1-3\]
xxx-xxx-1
xxx-xxx-2
xxx-xxx-3  

Tips: You can pass many args behind the command
``` 

- suffix_clear.py ---- remove the suffix of a given strinig with a constant pattern
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

- append-group4MU.sh.tmpl ----- 用来给产研添加sudo权限,支持多用户

- rm-user4MU.sh.tmpl ---------- 用来删除线上用户账户,支持多用户

- rm_key.py ------------------- 用来回收跳板机上的用户权限
```
usage: rm_key.py [-h] [-n NUMBER]

Remove random pubkey of user

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        The amount of pubkey you wanna remove one time,default
                        is 10.
```
