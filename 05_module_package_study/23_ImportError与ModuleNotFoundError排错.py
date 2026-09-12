# -*- coding: utf-8 -*-
"""
23 ImportError / ModuleNotFoundError 系统排错
===========================================

不要看到“导入失败”就立刻 pip install。
常见根因完全不同：
1. 包确实没安装；
2. 装到了另一个 Python；
3. 当前入口让 sys.path 不对；
4. 文件名遮蔽标准库/第三方包；
5. 循环导入；
6. 包存在，但目标名字不存在；
7. 扩展模块底层 DLL/so 依赖失败；
8. 安装包名和 import 名不同。
"""

import importlib.util
import os
import sys


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 先确定你到底在用哪个 Python")
print("sys.executable:", sys.executable)
print("version:", sys.version.split()[0])
print("cwd:", os.getcwd())

show("2. 查 spec")
for name in ["json", "demo_pkg", "definitely_not_a_real_module_xyz"]:
    spec = importlib.util.find_spec(name)
    print(name, "->", spec.origin if spec else None)

show("3. 查模块实际来源")
import json
print("json.__file__:", getattr(json, "__file__", None))
print("如果它指向项目里的 json.py，那你可能遮蔽了标准库。")

show("4. 区分错误")
print("ModuleNotFoundError 是 ImportError 的子类，通常强调模块解析失败。")
print("`cannot import name X from Y` 往往是 Y 找到了，但 X 不存在或 Y 尚未初始化完成。")

show("5. pip 对齐")
print(f"推荐检查：{sys.executable} -m pip show <distribution-name>")
