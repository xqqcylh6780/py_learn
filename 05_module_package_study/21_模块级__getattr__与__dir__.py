# -*- coding: utf-8 -*-
"""
21 模块级 __getattr__ 与 __dir__（PEP 562）
===========================================

模块也可以定义：
    def __getattr__(name): ...
    def __dir__(): ...

它可用于：
- 延迟导入某些可选对象；
- 兼容旧 API 并发出弃用警告；
- 动态暴露少量属性。

但滥用会让 IDE、静态分析和读代码的人难以知道名字从哪里来。
"""

import types


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 概念示例")
example = '''\n# some_module.py\ndef __getattr__(name):\n    if name == "expensive":\n        from .heavy import expensive\n        return expensive\n    raise AttributeError(name)\n'''
print(example.strip())

show("2. __getattr__ 只在普通属性查找失败后介入")
print("已经真实存在于模块字典里的属性会直接返回。")

show("3. 弃用兼容")
print("旧属性访问可以在 __getattr__ 中 warnings.warn(..., DeprecationWarning)。")

show("4. 原则")
print("公共 API 能静态明确就静态明确。惰性技巧只在启动成本/兼容性确有价值时使用。")
