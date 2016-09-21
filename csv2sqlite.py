#!/usr/bin/env python3
# coding=utf-8
import sqlite3
import codecs

conn = sqlite3.connect('contact.db')
with conn:
    curs = conn.cursor()
    curs.execute('''CREATE TABLE if not exists contact (
        name   TEXT    NOT NULL,
        class  TEXT    NOT NULL,
        phone1 INTEGER NOT NULL,
        note   TEXT,
        phone2 INTEGER,
        phone3 INTEGER)''')
conn.close()

with codecs.open('txl.csv', 'rb', 'utf16') as data:
    next(data)
    for line in data:
        line = line.strip().split(',')
        number_clean = line[6].replace('-', '')
        number_clean = number_clean.replace(' ', '')
        if len(number_clean) == 11:
            number_clean = number_clean[:3] + '-' + number_clean[3:]
            number_clean = number_clean[:8] + '-' + number_clean[8:]
        else:
            number_clean = number_clean[:4] + '-' + number_clean[4:]
            # 因为已经插入了一个字符，所以字符长度变为12+1=13
            if len(number_clean) == 13:
                number_clean = number_clean[:9] + '-' + number_clean[9:]

        conn = sqlite3.connect('contact.db')
        with conn:
            cur = conn.cursor()
            info = (line[0], line[4], number_clean, line[12])
            cur.execute("INSERT INTO contact (name,class,phone1,note)\
                VALUES ( ?, ?, ?, ?)", info)
        conn.close()



