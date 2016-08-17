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
