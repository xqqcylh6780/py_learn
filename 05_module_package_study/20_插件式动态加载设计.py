# -*- coding: utf-8 -*-
"""
20 插件式动态加载设计
====================

动态 import 最常见的合理用途之一是插件：
配置写模块名 -> importlib.import_module -> 获取约定入口 -> 校验 -> 调用。

真正成熟的可安装插件生态还会用 distribution metadata / entry points；那属于后面的工程化专题。
这里先掌握模块级插件协议。
"""

import importlib


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def load_callable(module_name, attr):
    module = importlib.import_module(module_name)
    value = getattr(module, attr)
    if not callable(value):
        raise TypeError(f"{module_name}.{attr} 不是 callable")
    return value


show("1. 从字符串加载插件")
plugin = load_callable("demo_pkg.greeter", "greet")
print(plugin("Plugin"))

show("2. 为什么要校验协议")
print("动态导入成功 ≠ 插件一定符合你的业务接口。")
print("至少验证必须属性、callable、版本/能力；复杂项目可配合 Protocol/ABC。")

show("3. 安全边界")
print("不要把不可信用户输入直接当成可 import 模块名。")
print("导入 Python 模块本质上可以执行代码，不是安全的数据解析操作。")
