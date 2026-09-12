# -*- coding: utf-8 -*-
"""15 权限、符号链接、硬链接：路径不一定直接指向普通文件。"""
from pathlib import Path
from tempfile import TemporaryDirectory
import os

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. symlink 与 resolve')
with TemporaryDirectory() as d:
    root=Path(d); target=root/'target.txt'; target.write_text('data', encoding='utf-8')
    link=root/'link.txt'
    try:
        link.symlink_to(target.name)
        print('is_symlink=',link.is_symlink())
        print('resolve=',link.resolve())
        print('read=',link.read_text(encoding='utf-8'))
    except (OSError, NotImplementedError) as e:
        print('当前环境无法创建符号链接:', type(e).__name__)

show('2. lstat vs stat')
print('stat() 通常跟随链接；lstat() 查看链接本身。')

show('3. 权限模型')
print('Unix 权限位与 Windows ACL 不是同一模型。os.access() 也不应当当成绝对安全授权检查。')
print('\n练习：ex29~ex30')
