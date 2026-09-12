# -*- coding: utf-8 -*-
"""
11 循环导入为什么发生，以及怎么解决
====================================

典型：
    a.py import b
    b.py import a

Python 为了支持递归导入，会在模块顶层代码执行完成之前，就把“正在初始化的模块对象”放进 sys.modules。
所以循环导入时，另一边可能拿到的是 partially initialized module。

真正的问题通常不是“Python 不支持两个模块互相认识”，而是：
两个模块在 import 阶段就急着访问对方尚未定义完成的名字。
"""


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 常见症状")
print("ImportError: cannot import name ... from partially initialized module ...")
print("或 AttributeError：某模块对象存在，但目标属性此刻还没定义。")

show("2. 优先解决架构耦合")
print("方案 A：把双方共享的类型/常量/协议抽到第三个低层模块。")
print("方案 B：依赖倒置，让高层依赖接口而不是互相依赖具体实现。")
print("方案 C：如果只是类型注解，用 TYPE_CHECKING + 延迟注解。")

show("3. 局部 import 是工具，不是万能药")
print("把 import 放函数内部可以延迟依赖解析，有时合理。")
print("但如果两个模块职责本来就缠在一起，只是把问题藏晚一点。")

show("4. 少在 __init__.py 里做大规模重新导出")
print("包级 re-export 越多，循环依赖图越难看清。")
