# -*- coding: utf-8 -*-
"""05 seek/tell：文件对象有当前位置；文本模式和二进制模式细节不同。"""
from io import BytesIO, StringIO

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. 二进制流随机访问')
f=BytesIO(b'abcdef')
print('初始:', f.tell())
print(f.read(2), '位置:', f.tell())
f.seek(4)
print(f.read(), '位置:', f.tell())
f.seek(-2, 2)
print('距末尾2字节:', f.read())

show('2. 文本流 seek 不应拿字符索引想当然')
s=StringIO('中文abc')
print(s.read(2), s.tell())
print('真实磁盘文本文件中 tell() 返回的是可供 seek() 恢复的位置 cookie，不保证等于字符数。')

show('3. 什么时候适合随机访问')
print('固定记录、索引文件、大型二进制容器；普通文本通常逐行流式处理更简单。')
print('\n练习：ex9~ex10')
