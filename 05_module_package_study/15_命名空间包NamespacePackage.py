# -*- coding: utf-8 -*-
"""
15 Namespace Package（命名空间包）
================================

现代 Python 支持没有 __init__.py 的命名空间包（PEP 420）。
同一个顶层包名甚至可以跨多个 sys.path 目录组合子包。

它适合大型发行体系/插件分拆，但普通小项目不必为了“高级”而去掉 __init__.py。
"""

import importlib
import sys
import tempfile
from pathlib import Path


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
    p1, p2 = Path(d1), Path(d2)
    (p1 / "shared_ns").mkdir()
    (p2 / "shared_ns").mkdir()
    (p1 / "shared_ns" / "a.py").write_text("VALUE = 'A'\n", encoding="utf-8")
    (p2 / "shared_ns" / "b.py").write_text("VALUE = 'B'\n", encoding="utf-8")

    sys.path[:0] = [str(p1), str(p2)]
    try:
        import shared_ns
        a = importlib.import_module("shared_ns.a")
        b = importlib.import_module("shared_ns.b")

        show("1. 没有 __init__.py 仍形成 namespace package")
        print(shared_ns)
        print("__file__:", getattr(shared_ns, "__file__", None))
        print("__path__:", list(shared_ns.__path__))
        print(a.VALUE, b.VALUE)
    finally:
        sys.path.remove(str(p1))
        sys.path.remove(str(p2))
        for name in ["shared_ns.a", "shared_ns.b", "shared_ns"]:
            sys.modules.pop(name, None)

show("2. 什么时候用")
print("当同一逻辑命名空间确实需要由多个独立分发包共同提供时很有价值。")
print("普通应用项目继续使用显式 __init__.py 往往更直观。")
