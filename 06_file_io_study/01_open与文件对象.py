# -*- coding: utf-8 -*-
"""01 open() 与文件对象：先把最核心模型弄清楚。"""
from pathlib import Path
from tempfile import TemporaryDirectory

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. open() 返回文件对象')
with TemporaryDirectory() as d:
    p = Path(d) / 'demo.txt'
    with open(p, 'w', encoding='utf-8') as f:
        print('类型:', type(f).__name__)
        print('可读:', f.readable(), '可写:', f.writable())
        f.write('第一行\n第二行\n')

    with open(p, 'r', encoding='utf-8') as f:
        print('全部读取:', repr(f.read()))

show('2. 常见模式')
print('r 只读；w 覆盖写；a 追加；x 独占创建')
print('b 二进制；t 文本(默认)；+ 读写两用')
print("例如: 'rb', 'w+', 'a', 'xb'")

show('3. 为什么推荐 with')
print('with 离开代码块时会调用 close()，即使块内抛异常也能清理文件描述符。')

show('4. w 模式的危险点')
with TemporaryDirectory() as d:
    p = Path(d)/'important.txt'
    p.write_text('原内容', encoding='utf-8')
    with p.open('w', encoding='utf-8'):
        pass
    print('仅仅打开 w 就已经截断:', repr(p.read_text(encoding='utf-8')))

print('\n练习：99_exercises.py ex1~ex2')
