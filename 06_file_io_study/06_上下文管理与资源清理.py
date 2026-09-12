# -*- coding: utf-8 -*-
"""06 文件资源清理：with、ExitStack、多文件。"""
from contextlib import ExitStack
from tempfile import TemporaryDirectory
from pathlib import Path

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. 多个 with')
with TemporaryDirectory() as d:
    a=Path(d)/'a.txt'; b=Path(d)/'b.txt'
    a.write_text('hello', encoding='utf-8')
    with a.open(encoding='utf-8') as src, b.open('w', encoding='utf-8') as dst:
        dst.write(src.read().upper())
    print(b.read_text(encoding='utf-8'))

show('2. 数量动态时用 ExitStack')
with TemporaryDirectory() as d:
    paths=[]
    for i in range(3):
        p=Path(d)/f'{i}.txt'; p.write_text(str(i), encoding='utf-8'); paths.append(p)
    with ExitStack() as stack:
        files=[stack.enter_context(p.open(encoding='utf-8')) for p in paths]
        print([f.read() for f in files])
    print('全部关闭:', all(f.closed for f in files))

print('\n练习：ex11~ex12')
