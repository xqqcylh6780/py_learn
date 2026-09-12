# -*- coding: utf-8 -*-
"""
19 导入副作用与启动性能
======================

模块顶层代码会在加载时执行，所以 import 本身可能造成副作用。

危险例子：
- import 时连接数据库；
- import 时发 HTTP 请求；
- import 时启动后台线程；
- import 时读巨大模型；
- import 时写文件；
- import 时根据环境立即退出进程。

这会让测试、CLI 启动、工具扫描、自动补全和循环导入都更脆弱。
"""

import time


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 顶层适合做什么")
print("定义函数、类、常量、轻量不可变配置。")

show("2. 昂贵初始化应显式触发")
def create_client():
    print("这里才真正创建外部客户端")
    return object()

print("只 import 本模块时 create_client 不会被自动调用。")

show("3. 可测性")
print("显式工厂函数比隐藏在 import 中的副作用更容易 mock、替换和失败重试。")

show("4. 性能排查")
print("CPython 可用 `python -X importtime ...` 查看导入耗时；输出需结合版本和环境分析。")
