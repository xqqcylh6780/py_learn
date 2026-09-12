# -*- coding: utf-8 -*-
"""21 mmap：把文件的一段映射进虚拟内存。"""
from pathlib import Path
from tempfile import TemporaryDirectory
import mmap

with TemporaryDirectory() as d:
    p=Path(d)/'data.bin'; p.write_bytes(b'hello\nworld\n')
    with p.open('r+b') as f:
        with mmap.mmap(f.fileno(), 0) as mm:
            print(mm[:5])
            print('world at', mm.find(b'world'))
            mm[0:5]=b'HELLO'
    print(p.read_bytes())

print('mmap 适合随机访问、搜索大型文件、共享映射等；它不是“把所有文件 I/O 自动变快”的魔法。')
print('空文件不能直接做长度 0 的常规映射；映射后也要注意底层文件尺寸变化。')
print('修改映射后可用 flush 请求写回，但持久性仍受操作系统缓存和存储设备语义影响。')
print('映射对象关闭前，基于它创建的 memoryview 等导出视图也必须先释放。')
print('\n练习：ex41~ex42')
