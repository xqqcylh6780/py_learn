# -*- coding: utf-8 -*-
"""02 文本模式、encoding、errors 与 newline。"""
from pathlib import Path
from tempfile import TemporaryDirectory

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. 文本文件本质仍是 bytes')
text='中文🙂 café'
raw=text.encode('utf-8')
print(text)
print(raw)
print(raw.decode('utf-8'))

show('2. 显式指定 encoding')
with TemporaryDirectory() as d:
    p=Path(d)/'a.txt'
    p.write_text(text, encoding='utf-8')
    print(p.read_text(encoding='utf-8'))

show('3. errors 策略')
bad=b'abc\xffdef'
for mode in ['replace','ignore','backslashreplace']:
    print(mode, '=>', bad.decode('utf-8', errors=mode))
print('业务数据默认应优先 strict，不要静默 ignore 掉损坏内容。')

show('4. newline')
print("文本模式会处理换行转换。需要精确观察原始换行时可 open(..., newline='')。")
print('CSV 模块写文件时通常也推荐 newline=""。')

show('5. UTF-8 BOM')
print("有些 Windows/Excel 文本会带 BOM；读取可用 encoding='utf-8-sig' 自动去掉 UTF-8 BOM。")
print('\n练习：ex3~ex4')
