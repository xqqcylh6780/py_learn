# -*- coding: utf-8 -*-
"""
18 项目目录结构与导入边界
=========================

一个稳定项目应让“包结构”表达依赖边界，而不是依靠 sys.path 魔改。

常见应用结构：
    project/
        pyproject.toml
        src/
            myapp/
                __init__.py
                domain/
                services/
                infrastructure/
        tests/

简单学习项目也可以 flat layout；关键不是目录越多越专业，而是：
- 导入路径稳定；
- 顶层包名明确；
- 测试不会因为 cwd 巧合而成功；
- 包内依赖方向清楚。
"""


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 坏味道")
print("../../../../utils.py")
print("sys.path.append('../..')")
print("同一个模块有时 import utils，有时 import app.utils")

show("2. 好的目标")
print("统一完全限定名，例如 myapp.services.user。")
print("从明确入口启动，不依赖 IDE 恰好把某个目录塞进 sys.path。")

show("3. src layout 的价值")
print("它能减少‘因为仓库根恰好在 sys.path，未安装包也能 import’的假象。")
print("但学习小项目没必要机械照搬，理解问题比背目录模板重要。")

show("4. 依赖边界")
print("低层核心模块尽量不要反向 import 高层 Web/UI/数据库层。")
print("这样也能显著减少循环导入。")
