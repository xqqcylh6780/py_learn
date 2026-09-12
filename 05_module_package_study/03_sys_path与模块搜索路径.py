# -*- coding: utf-8 -*-
"""
03 sys.path 与模块搜索路径
=========================

import 一个名字时，Python 必须知道“去哪里找”。
对普通文件系统模块来说，sys.path 是最重要的搜索路径列表之一。

注意：sys.path[0] 的具体值取决于启动方式：
- python script.py
- python -m package.module
- python -c ...
- 交互式解释器
它不是永远等于“当前工作目录”。
"""

import os
import sys
from pathlib import Path


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 当前工作目录和脚本目录不是一回事")
print("cwd:", os.getcwd())
print("__file__:", __file__)
print("脚本目录:", Path(__file__).resolve().parent)

show("2. sys.path")
for i, item in enumerate(sys.path[:8]):
    print(f"[{i}] {item!r}")

show("3. 常见来源")
print("sys.path 可能受到启动方式、环境变量、虚拟环境、site 包、.pth 等影响。")

show("4. 不推荐的临时补路径")
print("业务代码里到处 sys.path.append(...) 往往是在掩盖包结构问题。")
print("更好的做法是：正确组织包、从项目根使用 -m、或安装项目。")

show("5. 排查 ModuleNotFoundError")
print("先打印：模块名、sys.path、cwd、__file__，再确认是不是运行入口错了。")
