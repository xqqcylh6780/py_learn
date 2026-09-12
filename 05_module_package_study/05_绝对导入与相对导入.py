# -*- coding: utf-8 -*-
"""
05 绝对导入与相对导入
=====================

绝对导入：
    from demo_pkg.greeter import greet

相对导入（只能在包语境中正确解释）：
    from .greeter import greet
    from ..greeter import greet

`.` 表示当前包，`..` 表示父包。
相对导入依据的是模块的 package/spec 信息，而不是“相对磁盘文件路径”。
"""

from demo_pkg.greeter import greet
from demo_pkg.subpkg.formatter import excited
import demo_pkg.subpkg.formatter as formatter


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 绝对导入")
print(greet("Alice"))

show("2. demo_pkg/subpkg/formatter.py 内部使用了相对导入")
print(excited("Bob"))
print("formatter.__package__ =", formatter.__package__)
print("formatter.__spec__.parent =", formatter.__spec__.parent)

show("3. 为什么包内文件直接运行经常炸")
print("如果直接执行 subpkg/formatter.py，它可能失去正常的包语境。")
print("这时 `from ..greeter import greet` 往往出现 attempted relative import 错误。")

show("4. 推荐")
print("包内部引用：按项目风格选择绝对/相对导入并保持一致。")
print("包中的可执行模块：通常从项目根用 `python -m 包.模块` 运行。")
