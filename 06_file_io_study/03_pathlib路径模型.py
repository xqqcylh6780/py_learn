# -*- coding: utf-8 -*-
"""03 pathlib：现代 Python 路径操作主力。"""
from pathlib import Path, PureWindowsPath, PurePosixPath

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. 路径拼接不要手写斜杠')
base=Path('data')
p=base/'images'/'a.png'
print(p)
print('name=',p.name,'suffix=',p.suffix,'stem=',p.stem,'parent=',p.parent)

show('2. with_name / with_suffix')
print(p.with_suffix('.jpg'))
print(p.with_name('b.png'))

show('3. resolve 与 absolute')
print('absolute:', Path('.').absolute())
print('resolve :', Path('.').resolve())
print('resolve 会做规范化并通常解析符号链接；安全校验时要理解这一点。')

show('4. PurePath 只做语法处理')
print(PureWindowsPath(r'C:\Users\me')/'x.txt')
print(PurePosixPath('/tmp')/'x.txt')

show('5. exists 不是所有操作的必要前置')
print('先 exists 再 open 存在 TOCTOU 竞态；很多时候应直接执行操作并捕获 FileNotFoundError。')
print('\n练习：ex5~ex6')
