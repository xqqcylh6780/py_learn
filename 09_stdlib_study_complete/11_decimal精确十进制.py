# -*- coding: utf-8 -*-
"""11 decimal：精确十进制、上下文、舍入与财务计算"""
from decimal import Decimal, localcontext, ROUND_HALF_UP

print("=== float 的十进制表示误差 ===")
print(0.1 + 0.2)

print("\n=== Decimal 从字符串构造 ===")
a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)
print("不推荐 Decimal(0.1):", Decimal(0.1))

print("\n=== quantize 舍入 ===")
price = Decimal("12.345")
print(price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

print("\n=== localcontext ===")
with localcontext() as ctx:
    ctx.prec = 6
    print(Decimal(1) / Decimal(7))

print("\n=== Decimal 特殊值 ===")
for s in ["NaN", "Infinity", "-0"]:
    x = Decimal(s)
    print(s, x.is_nan(), x.is_infinite(), x.is_zero())

print("\n规则：涉及金额/十进制业务规则时，明确精度和舍入策略，不要只写 round(float)。")
