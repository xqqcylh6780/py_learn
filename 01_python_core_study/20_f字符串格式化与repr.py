# -*- coding: utf-8 -*-
"""
20 f-string、格式化与 repr
=========================
"""

from datetime import datetime


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. f-string")
name = "Alice"
age = 20
print(f"{name} is {age}")

section("2. 常用数字格式")
value = 12345.6789
print(f"{value:.2f}")
print(f"{value:,.2f}")
print(f"{0.256:.1%}")
print(f"{255:#x}")

section("3. 对齐与宽度")
for item in ["A", "LongName"]:
    print(f"|{item:<10}|{item:^10}|{item:>10}|")

section("4. !r 用 repr 形式")
text = "a\nb"
print(f"normal={text}")
print(f"repr={text!r}")

section("5. 调试语法 =")
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")

section("6. 日期格式")
now = datetime(2026, 9, 12, 15, 30)
print(f"{now:%Y-%m-%d %H:%M}")

section("7. repr 与 str 的定位")
print("str 更面向用户；repr 更面向开发/调试。具体表现由类型定义决定。")
