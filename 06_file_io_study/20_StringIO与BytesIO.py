# -*- coding: utf-8 -*-
"""20 io.StringIO / BytesIO：内存里的文件接口。"""
from io import StringIO, BytesIO
import csv

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. StringIO')
s=StringIO(); s.write('hello'); s.write('\nworld'); s.seek(0); print(s.read())

show('2. BytesIO')
b=BytesIO(); b.write(b'abc'); print(b.getvalue())

show('3. 测试很有用')
buf=StringIO(newline='')
csv.writer(buf).writerow(['a','b,c'])
print(repr(buf.getvalue()))
print('可以在不碰真实磁盘的情况下测试许多接受 file-like object 的函数。')
print('\n练习：ex39~ex40')
