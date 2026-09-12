# -*- coding: utf-8 -*-
"""
04 包（package）与 __init__.py
============================

传统 Python 包通常是带 __init__.py 的目录。
包本身也是模块对象，只是它还能包含子模块/子包。

__init__.py 常见用途：
- 提供包级 API；
- 定义版本、常量等轻量信息；
- 控制 from package import * 的 __all__；
- 做极少量、安全、快速的初始化。

不要把昂贵初始化塞进 __init__.py，否则任何导入子模块的人都要付出代价。
"""

import demo_pkg
import demo_pkg.greeter
import demo_pkg.subpkg.formatter


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 包本身也是模块")
print(demo_pkg)
print("name:", demo_pkg.__name__)
print("package:", demo_pkg.__package__)
print("path:", list(demo_pkg.__path__))

show("2. __init__.py 可以暴露稳定入口")
print(demo_pkg.greet("Alice"))
print("调用者不必知道 greet 实际定义在哪个内部文件。")

show("3. 子模块有完整限定名")
print(demo_pkg.greeter.__name__)
print(demo_pkg.subpkg.formatter.__name__)
print(demo_pkg.subpkg.formatter.excited("Bob"))

show("4. 设计原则")
print("包级 API 可以简化使用，但不要无脑把所有内部名字重新导出。")
print("否则启动慢、循环导入增加、内部重构边界也会变差。")
