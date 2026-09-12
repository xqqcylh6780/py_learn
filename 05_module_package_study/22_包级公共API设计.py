# -*- coding: utf-8 -*-
"""
22 包级公共 API 设计与 re-export
===============================

库的内部文件布局可以变化，但用户希望 import 路径尽量稳定。
因此 __init__.py 可以把少量正式 API 重新导出：

    from .client import Client
    from .errors import MyError
    __all__ = ["Client", "MyError"]

这叫 re-export。
"""

import demo_pkg
from demo_pkg import greet


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 用户看到的 API")
print(greet("API"))
print("用户不需要知道 greet 实际在 demo_pkg.greeter。")

show("2. 稳定性")
print("内部 greeter.py 将来可拆分，只要 demo_pkg.greet 契约保持，调用方不用全改。")

show("3. 不要全量 re-export")
print("把整个内部实现树都搬到顶层会造成命名冲突、启动变慢、循环依赖和维护负担。")

show("4. 内部模块")
print("常见约定 `_internal.py` / `_impl/` 表示非稳定公共 API，但仍不是安全隐藏机制。")
