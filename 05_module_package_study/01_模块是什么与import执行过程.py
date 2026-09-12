# -*- coding: utf-8 -*-
"""
01 模块是什么，以及 import 到底做了什么
========================================

模块（module）最常见的形态就是一个 .py 文件，但“模块”这个概念比文件更广：
内建模块、扩展模块、包中的模块、动态创建的模块都属于 module。

一次普通 import 大致经历：
1. 看 sys.modules 缓存里有没有。
2. 根据 sys.meta_path 上的 finder 查找模块。
3. 得到 ModuleSpec。
4. 创建模块对象，并先放进 sys.modules。
5. 执行模块顶层代码，填充模块命名空间。
6. 把模块对象绑定到当前作用域里的名字。

最重要的认识：import 不是“把另一个文件复制进来”，而是“获得一个模块对象”。
"""

import sys
import types
import demo_pkg.math_tools as math_tools


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. import 得到的是模块对象")
print(math_tools)
print("type:", type(math_tools))
print("是不是 ModuleType:", isinstance(math_tools, types.ModuleType))
print("模块名:", math_tools.__name__)
print("PI:", math_tools.PI)
print("add(2, 3):", math_tools.add(2, 3))

show("2. 模块有自己的命名空间")
print("PI 在模块字典里吗:", "PI" in math_tools.__dict__)
print("模块前几个名字:", sorted(k for k in math_tools.__dict__ if not k.startswith("__")))

show("3. 导入后通常会进入 sys.modules")
print("demo_pkg.math_tools" in sys.modules)
print(sys.modules["demo_pkg.math_tools"] is math_tools)

show("4. 再次 import 通常复用同一个模块对象")
import demo_pkg.math_tools as math_tools_again
print("同一个对象:", math_tools_again is math_tools)

show("5. 顶层代码的含义")
print("模块第一次真正加载时会执行顶层代码。")
print("因此 import 阶段不应该偷偷连数据库、发网络请求、启动线程等昂贵副作用。")

show("结论")
print("import 的核心对象是模块，不是源文件文本。")
print("后面会继续拆 sys.modules、sys.path、ModuleSpec 和 importlib。")
