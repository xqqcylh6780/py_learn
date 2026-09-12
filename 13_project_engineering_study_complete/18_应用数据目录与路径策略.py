# -*- coding: utf-8 -*-
"""
18 应用数据目录与路径策略
==============

源码目录、cwd、配置目录、缓存目录、用户数据目录不是一回事。

不同数据有不同的权限、备份和清理策略：配置要可审计，缓存应可删除，用户数据需持久化。
路径应在程序边界解析为明确的绝对路径，再传给业务层使用。
把可变数据写进安装目录会在只读部署、容器和普通用户权限下失败。
"""

from pathlib import Path
import tempfile
with tempfile.TemporaryDirectory() as d:
    root=Path(d)
    for name in ['config','data','cache']:
        p=root/name; p.mkdir(); print(name, '=>', p)
print('\n不要默认“程序启动目录 = 项目目录”。')
print('服务、计划任务、IDE、PyInstaller 程序的 cwd 都可能不同。')
