# -*- coding: utf-8 -*-
"""
18 lambda、闭包与延迟绑定
========================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. lambda 是匿名表达式函数")
square = lambda x: x * x
print(square(5))

section("2. 最常见用途：key 函数")
items = [("A", 3), ("B", 1), ("C", 2)]
print(sorted(items, key=lambda item: item[1]))

section("3. 复杂逻辑不要硬塞 lambda")
print("需要多步逻辑、文档、类型说明、调试时用 def。")

section("4. 闭包延迟绑定")
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs], "<- 调用时 i 已经是最后的 2")

section("5. 用默认参数做定义时绑定")
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])

section("6. 更清楚的工厂函数")
def make_fn(value):
    def fn():
        return value
    return fn

funcs = [make_fn(i) for i in range(3)]
print([f() for f in funcs])
