# -*- coding: utf-8 -*-
"""
10 python -m 与包内可执行模块
============================

`python some/path/tool.py` 与 `python -m package.tool` 不是同一启动方式。

-m 的关键优势：
- 按模块名定位；
- 保留正确的包语境；
- 包内相对导入更可靠；
- 更接近“这个模块属于整个包”的事实。

包还可以提供 __main__.py，使：
    python -m package
成为合法入口。
"""

import subprocess
import sys


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 当前解释器")
print(sys.executable)

show("2. 常用 -m 命令")
print(f"{sys.executable} -m pip --version")
print(f"{sys.executable} -m compileall .")
print(f"{sys.executable} -m package.module")

show("3. 为什么推荐 sys.executable -m pip")
print("这样 pip 明确属于当前这个 Python 解释器，减少多 Python 环境装错位置。")

show("4. 包入口结构")
print("package/__main__.py 存在时，`python -m package` 会执行它。")
print("通常 __main__.py 很薄，只负责调用真正的 main()。")
