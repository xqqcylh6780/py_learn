# -*- coding: utf-8 -*-
"""
03 数值模型与精度
================

覆盖 int、float、除法、取整、模运算，以及浮点精度陷阱。
"""

import math


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. Python int 是任意精度整数")
n = 10 ** 100
print("10**100 位数:", len(str(n)))

section("2. / 与 // 不同")
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("-7 // 2 =", -7 // 2, "<- 向负无穷方向取整")

section("3. % 与 // 满足恒等式")
for a, b in [(7, 3), (-7, 3), (7, -3)]:
    q, r = divmod(a, b)
    print(a, b, "=>", q, r, "check:", a == q * b + r)

section("4. float 是二进制浮点数")
x = 0.1 + 0.2
print("0.1 + 0.2 =", repr(x))
print("直接 == 0.3:", x == 0.3)
print("math.isclose:", math.isclose(x, 0.3))

section("5. round 不是金融十进制工具")
print("round(2.5) =", round(2.5))
print("round(3.5) =", round(3.5))
print("涉及货币精确十进制时应使用 decimal.Decimal。")

section("6. bool 是 int 的子类")
print(isinstance(True, int))
print(True + True + False)
print("业务代码里仍应把 bool 当逻辑类型使用。")
