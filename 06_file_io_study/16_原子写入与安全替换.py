# -*- coding: utf-8 -*-
"""16 原子写入：避免写到一半进程崩溃留下半文件。"""
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
import os

def atomic_write_text(path: Path, text: str):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile('w', encoding='utf-8', dir=path.parent, delete=False) as f:
        tmp=Path(f.name)
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    try:
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)

with TemporaryDirectory() as d:
    p=Path(d)/'config.json'
    atomic_write_text(p, '{"ok": true}\n')
    print(p.read_text(encoding='utf-8'))

print('os.replace 在同一文件系统上的替换通常具有原子语义；跨文件系统移动不应假设原子。')
print('fsync 文件后是否还需同步父目录取决于你要求的崩溃一致性级别和平台。')
print('\n练习：ex31~ex32')
