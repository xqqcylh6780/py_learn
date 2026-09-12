# -*- coding: utf-8 -*-
"""17 覆盖前备份：版本化文件最简单可靠的保险。"""
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

def backup_before_replace(path: Path):
    path=Path(path)
    if not path.exists(): return None
    backup=path.with_suffix(path.suffix+'.bak')
    shutil.copy2(path, backup)
    return backup

with TemporaryDirectory() as d:
    p=Path(d)/'settings.toml'; p.write_text('v=1\n', encoding='utf-8')
    b=backup_before_replace(p)
    p.write_text('v=2\n', encoding='utf-8')
    print('current:',p.read_text(encoding='utf-8').strip())
    print('backup :',b.read_text(encoding='utf-8').strip())

print('生产系统可进一步采用时间戳/世代号、保留 N 份、校验后再删除旧备份。')
print('注意：备份敏感文件会复制敏感数据，权限与生命周期也要一起设计。')
print('\n练习：ex33~ex34')
