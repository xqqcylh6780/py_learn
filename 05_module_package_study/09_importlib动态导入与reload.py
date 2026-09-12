# -*- coding: utf-8 -*-
"""
09 importlib：动态导入与 reload
==============================

当模块名来自配置、插件列表或运行时字符串时，importlib.import_module() 比拼接 __import__ 更清晰。

reload(module) 会重新执行模块代码，但不是“把整个程序状态恢复到刚启动”。
已经从旧模块导入出去的对象、已有实例、外部引用不会自动全部替换。
"""

import importlib
import demo_pkg.math_tools as math_tools


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 动态导入")
module_name = "demo_pkg.math_tools"
mod = importlib.import_module(module_name)
print(mod.add(2, 5))

show("2. 相对动态导入")
rel = importlib.import_module(".greeter", package="demo_pkg")
print(rel.greet("Dynamic"))

show("3. reload")
old_id = id(math_tools)
reloaded = importlib.reload(math_tools)
print("模块对象通常仍是同一个:", reloaded is math_tools)
print("id:", old_id, id(reloaded))

show("4. reload 的边界")
print("`from mod import func` 得到的旧 func 引用不会自动变成新定义。")
print("旧类创建出来的实例，也不会神奇地换成 reload 后的新类。")
print("因此 reload 更适合交互开发/工具场景，不应成为普通业务依赖。")
