# -*- coding: utf-8 -*-
"""
08 sys.modules —— 模块缓存与“只执行一次”
========================================

sys.modules 是进程内已加载模块的核心缓存映射：模块全名 -> 模块对象。
普通 import 会优先检查这里。

“模块只执行一次”更准确地说是：
在常规 import 流程中，同一个完全限定模块名已经成功加载并缓存后，后续 import 通常直接复用对象。
"""

import sys
import demo_pkg.math_tools as first


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 缓存存在")
name = "demo_pkg.math_tools"
print(name in sys.modules)
print(sys.modules[name] is first)

show("2. 再 import")
import demo_pkg.math_tools as second
print(first is second)

show("3. 模块对象也可以有运行期状态")
first.runtime_demo = 123
print(second.runtime_demo)
del first.runtime_demo

show("4. 不要把删 sys.modules 当正常重载方案")
print("手工删除缓存可能留下其他地方持有的旧对象引用，状态会变得很难推理。")
print("开发期若真要重载，了解 importlib.reload；生产逻辑一般不依赖热重载。")
