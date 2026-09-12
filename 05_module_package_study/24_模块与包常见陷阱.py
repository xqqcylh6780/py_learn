# -*- coding: utf-8 -*-
"""
24 模块与包常见陷阱 —— 错题本
==============================
"""


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("坑 1：文件名遮蔽标准库")
print("项目里写 json.py、typing.py、asyncio.py、email.py，可能让 import 导到自己文件。")

show("坑 2：包内模块直接按文件运行")
print("相对导入失败时，先检查是不是应该 `python -m package.module`。")

show("坑 3：到处 sys.path.append")
print("这通常让项目在某台机器/某个 cwd 下偶然能跑，却破坏可重复性。")

show("坑 4：from x import *")
print("来源不透明、容易覆盖名字，也让静态分析更差。")

show("坑 5：__init__.py 太重")
print("任何子模块导入都可能先触发包初始化，昂贵副作用会被放大。")

show("坑 6：把循环导入只靠局部 import 糊住")
print("能跑不等于依赖结构健康。优先考虑抽共享层、依赖倒置。")

show("坑 7：认为 reload 会更新所有引用")
print("外部已绑定函数、旧类实例等不会自动全换。")

show("坑 8：模块级全局可变状态")
print("它在进程内会被复用，测试之间、请求之间可能互相污染。")

show("坑 9：把 __all__ 当 private")
print("它表达导出意图，不是权限系统。")

show("坑 10：假设所有模块都有 __file__")
print("内建模块、namespace package、特殊 loader 不一定满足。")

show("坑 11：import 名和 pip 安装名一定一样")
print("distribution name 与 import package name 是两个概念。")

show("坑 12：不可信字符串直接动态 import")
print("导入会执行代码，不能当安全配置数据解析。")

show("最终原则")
print("导入路径要稳定、入口要明确、副作用要少、依赖方向要清楚。")
