# -*- coding: utf-8 -*-
"""08 目录遍历：iterdir、glob、rglob、os.walk。"""
from pathlib import Path
from tempfile import TemporaryDirectory
import os

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

with TemporaryDirectory() as d:
    root=Path(d)
    (root/'a').mkdir(); (root/'b').mkdir()
    (root/'a'/'x.txt').write_text('x', encoding='utf-8')
    (root/'a'/'y.py').write_text('y', encoding='utf-8')
    (root/'b'/'z.txt').write_text('z', encoding='utf-8')

    show('1. iterdir 一层')
    print(sorted(p.name for p in root.iterdir()))

    show('2. glob/rglob')
    print(sorted(p.name for p in root.rglob('*.txt')))

    show('3. os.walk 可剪枝')
    for dirpath, dirnames, filenames in os.walk(root):
        print(Path(dirpath).name, dirnames, filenames)

show('4. 顺序不要想当然')
print('文件系统枚举顺序不是业务排序；需要稳定结果就显式 sorted()。')
print('\n练习：ex15~ex16')
