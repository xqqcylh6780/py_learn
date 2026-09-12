# -*- coding: utf-8 -*-
"""
14 sys.meta_path、Finder 与 Loader
=================================

import 是可扩展协议。
粗略流程：
- finder：回答“这个模块我能不能找到？它的 spec 是什么？”
- loader：回答“怎么创建/执行这个模块？”

sys.meta_path 保存顶层 finder 链。
普通项目很少需要自己写 importer，但理解它能解释很多魔法：测试框架、插件系统、zipimport、冻结程序等。
"""

import sys
import importlib.util


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 当前 meta_path")
for finder in sys.meta_path:
    print(type(finder).__name__, "->", finder)

show("2. 不执行模块也可以查 spec")
spec = importlib.util.find_spec("demo_pkg.math_tools")
print("name:", spec.name)
print("origin:", spec.origin)
print("loader:", spec.loader)

show("3. find_spec 的用途")
print("可以用于探测一个可选依赖是否可被导入，但不要把它误当版本/功能完整性检查。")

show("4. 自定义 importer")
print("高级框架可以把模块从数据库、网络、压缩包等非普通路径加载。")
print("业务代码没有明确需求时，不要随便修改 sys.meta_path。")
