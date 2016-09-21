#!/usr/bin/env python
# coding=utf-8
import json
li=['你','好']
di={'你':'好'}


def list_dict_proc(item):
    # print含有中文的列表和字典对象有以下四种方法
    item_1= ','.join(item)
    item_2=json.dumps(item).decode('unicode-escape').encode('utf-8')
    item_3=json.dumps(item, ensure_ascii=False,encoding="UTF-8").encode('utf-8')
    item_4=str(item).decode('string_escape')
    for i in item_1,item_2,item_3,item_4:
        print type(i),i

list_dict_proc(li)


