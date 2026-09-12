# -*- coding: utf-8 -*-
"""25 文件 I/O 异常与 TOCTOU 竞态。"""
from pathlib import Path
from tempfile import TemporaryDirectory

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. 精准异常')
with TemporaryDirectory() as d:
    p=Path(d)/'missing.txt'
    try:
        p.read_text(encoding='utf-8')
    except FileNotFoundError as e:
        print(type(e).__name__, e.filename)

show('2. 常见 OSError 子类')
print('FileNotFoundError, FileExistsError, PermissionError, IsADirectoryError, NotADirectoryError...')
print('它们大多属于 OSError 家族，能精确捕获时不要一上来 except OSError。')

show('3. TOCTOU')
print('错误思路：if path.exists(): path.unlink()，中间文件状态可能变化。')
print('更稳健：直接操作并处理预期异常，例如 path.unlink(missing_ok=True)。')

show('4. 重试')
print('只对明确的瞬时错误、有限次数、带退避地重试；PermissionError 不应无限重试。')
print('\n练习：ex49~ex50')
