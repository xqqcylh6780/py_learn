# -*- coding: utf-8 -*-
"""10 CSV：不要手工 split(',')。"""
import csv
from io import StringIO

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. CSV 字段里可能本身有逗号/引号/换行')
buf=StringIO(newline='')
w=csv.writer(buf)
w.writerow(['name','note'])
w.writerow(['Alice','hello, world'])
w.writerow(['Bob','他说 "ok"'])
print(buf.getvalue())

show('2. reader 正确解析')
buf.seek(0)
print(list(csv.reader(buf)))

show('3. DictReader/DictWriter')
buf=StringIO('name,age\nAlice,20\nBob,30\n', newline='')
for row in csv.DictReader(buf): print(row, type(row['age']).__name__)
print('CSV 没有类型系统，20 读回来仍是字符串。')

show('4. 真文件通常 newline=""')
print('官方 csv 文档建议打开文件时 newline=""，让 csv 模块自己处理换行规则。')
print('\n练习：ex19~ex20')
