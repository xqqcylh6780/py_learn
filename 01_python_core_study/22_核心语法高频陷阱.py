# -*- coding: utf-8 -*-
"""
22 核心语法高频陷阱
==================

把前面最容易在真实项目里造成 bug 的点集中复习。
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("坑 1：可变默认参数")
def bad(x, bucket=[]):
    bucket.append(x)
    return bucket
print(bad(1), bad(2))

section("坑 2：二维 list 乘法共享行")
grid = [[0] * 2] * 3
grid[0][0] = 9
print(grid)

section("坑 3：is 当 ==")
print("值比较用 ==；身份比较用 is；None 常用 is None。")

section("坑 4：0/空字符串被 or 当作缺失值")
value = 0
print(value or 100)
print(100 if value is None else value)

section("坑 5：闭包延迟绑定")
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])

section("坑 6：浅复制没有复制内部对象")
a = [[1], [2]]
b = a.copy()
b[0].append(9)
print("a:", a)
print("b:", b)

section("坑 7：修改正在遍历的容器")
items = [1, 2, 3, 4]
for x in items[:]:
    if x % 2 == 0:
        items.remove(x)
print(items)
print("若确实要删除，常用新容器、切片副本或反向索引等明确策略。")

section("坑 8：把 dict.get 与 [] 当成完全等价")
print("需要区分“键缺失”和“值为 None”时，要显式设计。")

section("坑 9：float 精确相等")
import math
print(math.isclose(0.1 + 0.2, 0.3))

section("坑 10：过度压缩表达式")
print("可读性优先。复杂推导式、lambda、海象、链式表达式应该主动拆开。")
