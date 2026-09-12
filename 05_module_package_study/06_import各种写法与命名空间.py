# -*- coding: utf-8 -*-
"""
06 import 各种写法与命名空间
============================

不同 import 写法影响的是“当前命名空间绑定什么名字”，不是模块内部内容被复制了几份。
"""

import demo_pkg.math_tools
import demo_pkg.math_tools as mt
from demo_pkg import math_tools
from demo_pkg.math_tools import add
from demo_pkg.math_tools import add as plus


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. import package.module")
print(demo_pkg.math_tools.add(1, 2))

show("2. as 给当前绑定起别名")
print(mt.add(2, 3))

show("3. from package import module")
print(math_tools.add(3, 4))

show("4. from module import name")
print(add(4, 5))
print(plus(5, 6))

show("5. 一个重要区别")
print("`from x import y` 把当时解析到的 y 直接绑定到当前命名空间。")
print("之后 x.y 被重新绑定，不代表你本地的 y 自动跟着重新绑定。")

show("6. 可读性")
print("公共模块名尽量保留来源，例如 `json.loads` 往往比导入一堆裸函数更清楚。")
print("别名应当稳定且有行业惯例，避免 cryptic alias。")
