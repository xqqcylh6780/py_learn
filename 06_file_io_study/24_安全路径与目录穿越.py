# -*- coding: utf-8 -*-
"""24 路径安全：用户给的文件名不能直接拼到服务器目录。"""
from pathlib import Path
from tempfile import TemporaryDirectory

def safe_join(base: Path, user_path: str) -> Path:
    base=Path(base).resolve()
    candidate=(base/user_path).resolve()
    try:
        candidate.relative_to(base)
    except ValueError:
        raise ValueError('path escapes base directory')
    return candidate

with TemporaryDirectory() as d:
    base=Path(d)
    print(safe_join(base, 'a/b.txt'))
    try:
        print(safe_join(base, '../outside.txt'))
    except ValueError as e:
        print('blocked:', e)

print('注意：真实安全场景还要考虑符号链接竞态、文件创建时机、权限边界以及平台路径规则。')
print('只做字符串 startswith(base) 是错误的：/safe2 会以 /safe 开头但并不在 /safe 内。')
print('\n练习：ex47~ex48')
