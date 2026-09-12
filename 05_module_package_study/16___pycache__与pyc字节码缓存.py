# -*- coding: utf-8 -*-
"""
16 __pycache__ 与 .pyc 字节码缓存
================================

Python 导入源代码模块时，可能把编译后的字节码缓存到 __pycache__。
它的目标主要是减少后续启动时重新编译源码的成本，不等于把 Python 变成原生机器码程序。

不要：
- 把 .pyc 当源码加密；
- 假设有 .pyc 就完全不需要环境/依赖；
- 手工依赖某个具体缓存文件名。
"""

import importlib.util
import sys
from pathlib import Path


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 计算一个可能的缓存路径")
source = Path(__file__).resolve()
print("source:", source)
try:
    print("cache:", importlib.util.cache_from_source(str(source)))
except NotImplementedError as e:
    print("当前实现不支持这个转换:", e)

show("2. Python 标签")
print("cache_tag:", sys.implementation.cache_tag)

show("3. 缓存失效")
print("解释器会根据缓存方案判断 pyc 是否仍对应当前源码/解释器。")
print("通常让 Python 自己维护，不要业务代码手工管理 __pycache__。")

show("4. Git")
print("项目一般把 __pycache__/ 和 *.py[cod] 放入 .gitignore。")
