# -*- coding: utf-8 -*-
"""09 创建、删除、移动、复制：pathlib + shutil。"""
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

with TemporaryDirectory() as d:
    root=Path(d)
    show('1. mkdir')
    p=root/'a'/'b'
    p.mkdir(parents=True, exist_ok=True)
    print(p.exists())

    show('2. touch/unlink/rmdir')
    f=p/'x.txt'; f.touch(); print(f.exists()); f.unlink(); print(f.exists())

    show('3. copy/copy2/copytree/move')
    src=root/'src.txt'; src.write_text('hello', encoding='utf-8')
    dst=root/'dst.txt'
    shutil.copy2(src, dst)
    print(dst.read_text(encoding='utf-8'))
    moved=root/'moved.txt'; shutil.move(dst, moved); print(moved.exists())

show('4. 删除目录树要谨慎')
print('shutil.rmtree() 是递归删除，不进回收站。路径来源必须可信且最好先做边界校验。')
print('\n练习：ex17~ex18')
