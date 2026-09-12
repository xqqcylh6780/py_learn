# -*- coding: utf-8 -*-
"""12 fractions：精确有理数"""
from fractions import Fraction
from decimal import Decimal

print("=== 精确分数 ===")
a = Fraction(1, 3)
b = Fraction(1, 6)
print(a + b)
print(float(a))

print("\n=== 字符串与 Decimal ===")
print(Fraction("0.125"))
print(Fraction(Decimal("0.125")))

print("\n=== float 转分数 ===")
print(Fraction(0.1))
print(Fraction(0.1).limit_denominator(10))

print("\n=== 自动约分 ===")
print(Fraction(20, 30))

print("\n适用：比例、概率、音乐节拍、精确有理计算。大量数值计算通常还是用专门数值库。")
