# -*- coding: utf-8 -*-
"""
13 ModuleSpec、__spec__、__loader__、__package__
===============================================

现代 import 系统不只是“搜索文件”。查找器（finder）会产生 ModuleSpec，加载器（loader）依据 spec 创建/执行模块。

常见元数据：
- __name__：模块完全限定名；
- __package__：相对导入解析上下文；
- __spec__：ModuleSpec；
- __loader__：加载器；
- __file__：如果有文件来源，通常是来源路径；
- __cached__：可能指向字节码缓存；
- package.__path__：包的子模块搜索位置。

不是所有模块都有 __file__。
"""

import sys
import demo_pkg.math_tools as mod


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 普通模块元数据")
for name in ("__name__", "__package__", "__file__", "__cached__", "__loader__", "__spec__"):
    print(name, "=", getattr(mod, name, None))

show("2. spec")
spec = mod.__spec__
print("spec.name:", spec.name)
print("spec.parent:", spec.parent)
print("spec.origin:", spec.origin)
print("spec.submodule_search_locations:", spec.submodule_search_locations)

show("3. 内建模块不一定有磁盘源文件")
print("sys.__file__:", getattr(sys, "__file__", None))
print("sys.__spec__.origin:", sys.__spec__.origin)

show("4. 不要假设模块 == .py 文件")
print("内建模块、扩展模块、namespace package、zip 中模块等都可能由不同 loader 提供。")
