# -*- coding: utf-8 -*-
"""18 gzip/bz2/lzma：压缩流也可以像文件一样读写。"""
import gzip, bz2, lzma
from tempfile import TemporaryDirectory
from pathlib import Path

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

text=('hello 世界\n'*1000)
with TemporaryDirectory() as d:
    root=Path(d)
    for mod, ext in [(gzip,'.gz'),(bz2,'.bz2'),(lzma,'.xz')]:
        p=root/('data'+ext)
        with mod.open(p, 'wt', encoding='utf-8') as f: f.write(text)
        with mod.open(p, 'rt', encoding='utf-8') as f: ok=(f.read()==text)
        print(ext, p.stat().st_size, 'roundtrip=',ok)

show('选择')
print('gzip 兼容性/速度常较好；bz2/lzma 常压得更小但更慢。真正选择要根据数据和场景基准测试。')
print('\n练习：ex35~ex36')
