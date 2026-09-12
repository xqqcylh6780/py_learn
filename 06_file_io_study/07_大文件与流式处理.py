# -*- coding: utf-8 -*-
"""07 大文件：不要默认 read() 全塞进内存。"""
from io import StringIO, BytesIO

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. 文本逐行')
f=StringIO('a\nb\nc\n')
for line in f:
    print('line=',repr(line.rstrip('\n')))

show('2. 二进制分块')
f=BytesIO(b'0123456789')
while chunk := f.read(4):
    print(chunk)

show('3. iter(callable, sentinel)')
f=BytesIO(b'abcdefgh')
for chunk in iter(lambda: f.read(3), b''):
    print(chunk)

show('4. chunk size 没有万能值')
print('常见几十 KB 到数 MB；应根据存储、网络、算法和内存测量。')
print('流式算法的关键是：状态可增量更新，而不是先把全部输入读完。')
print('\n练习：ex13~ex14')
