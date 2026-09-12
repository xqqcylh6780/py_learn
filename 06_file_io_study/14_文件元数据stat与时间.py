# -*- coding: utf-8 -*-
"""14 stat：大小、时间、类型、权限。"""
from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime
import stat

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

with TemporaryDirectory() as d:
    p=Path(d)/'x.txt'; p.write_text('abc', encoding='utf-8')
    st=p.stat()
    show('1. 基本元数据')
    print('size=',st.st_size)
    print('mtime=',datetime.fromtimestamp(st.st_mtime))
    print('is_file=',p.is_file(),'is_dir=',p.is_dir())

    show('2. mode')
    print(oct(stat.S_IMODE(st.st_mode)))

show('3. 时间语义跨平台有差异')
print('mtime=内容修改；ctime 在 Unix 常是元数据变更时间，在 Windows 常表示创建时间。不要把 ctime 跨平台统一解释成 creation time。')
print('\n练习：ex27~ex28')
