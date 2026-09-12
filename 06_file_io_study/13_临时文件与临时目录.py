# -*- coding: utf-8 -*-
"""13 tempfile：不要自己用随机文件名冒充安全临时文件。"""
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory
from pathlib import Path

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. TemporaryFile')
with TemporaryFile('w+t', encoding='utf-8') as f:
    f.write('hello'); f.seek(0); print(f.read())

show('2. NamedTemporaryFile')
with NamedTemporaryFile('w+t', encoding='utf-8', delete=True) as f:
    print('name=', f.name)

show('3. TemporaryDirectory')
with TemporaryDirectory() as d:
    p=Path(d)/'x.txt'; p.write_text('x', encoding='utf-8'); print(p.exists())
print('退出后目录已清理:', Path(d).exists())

show('4. Windows 细节')
print('临时文件被另一个程序重新打开时，Windows 的共享/删除语义与 POSIX 不同；跨平台代码要实测。')
print('\n练习：ex25~ex26')
