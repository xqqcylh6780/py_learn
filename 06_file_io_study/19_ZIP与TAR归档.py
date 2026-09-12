# -*- coding: utf-8 -*-
"""19 zipfile/tarfile：归档多个文件，以及最重要的解压安全。"""
from pathlib import Path
from tempfile import TemporaryDirectory
import zipfile
import tarfile

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

with TemporaryDirectory() as d:
    root=Path(d); src=root/'src'; src.mkdir()
    (src/'a.txt').write_text('A', encoding='utf-8')
    zpath=root/'demo.zip'
    with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED) as z:
        z.write(src/'a.txt', arcname='docs/a.txt')
    with zipfile.ZipFile(zpath) as z:
        print(z.namelist())
        print(z.read('docs/a.txt'))

    show('2. tarfile')
    tpath=root/'demo.tar.gz'
    with tarfile.open(tpath, 'w:gz') as t:
        t.add(src/'a.txt', arcname='docs/a.txt')
    with tarfile.open(tpath, 'r:gz') as t:
        print(t.getnames())

show('3. Zip Slip / Tar 路径穿越')
print('归档条目名可能是 ../../evil 或绝对路径。不要对不可信归档无脑 extractall；应验证解压后的 resolve() 仍在目标目录内。')
print('现代 tarfile 版本提供 extraction filters，但仍应了解你的 Python 版本和过滤策略。')
print('\n练习：ex37~ex38')
