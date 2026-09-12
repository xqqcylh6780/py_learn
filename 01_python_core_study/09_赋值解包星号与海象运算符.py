# -*- coding: utf-8 -*-
"""
09 赋值、解包、星号与海象运算符
==============================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. 多目标赋值与交换")
a, b = 1, 2
a, b = b, a
print(a, b)

section("2. 星号解包")
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)

section("3. 嵌套解包")
name, (x, y) = ("P", (3, 4))
print(name, x, y)

section("4. 构造容器时展开")
left = [1, 2]
right = [3, 4]
print([0, *left, *right, 5])
print({**{"a": 1}, **{"a": 2, "b": 3}})

section("5. 海象运算符 := 在表达式中绑定名字")
text = "hello world"
if (n := len(text)) > 5:
    print("length:", n)

section("6. 海象适合避免重复计算")
items = ["10", "x", "20"]
def parse_int(s):
    try:
        return int(s)
    except ValueError:
        return None

parsed = [n for s in items if (n := parse_int(s)) is not None]
print(parsed)
print("不要为了少写一行而把复杂逻辑都塞进 :=。")
