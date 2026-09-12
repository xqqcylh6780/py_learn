# -*- coding: utf-8 -*-
"""
07 真值、None 与短路逻辑
=======================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. 常见假值")
values = [False, None, 0, 0.0, 0j, "", [], (), {}, set(), range(0)]
for value in values:
    print(f"{repr(value):>12} -> {bool(value)}")

section("2. and/or 返回操作数，不强制返回 bool")
print("" or "default")
print("hello" and 123)
print(None or [] or "last")

section("3. 短路求值")
def expensive():
    print("expensive() 被调用")
    return True

print(False and expensive())
print(True or expensive())

section("4. None 判断优先 is None")
value = None
print(value is None)
print("None 是单例语义，is 更准确。")

section("5. `x or default` 会吞掉合法假值")
def bad_default(value):
    return value or 100


def good_default(value):
    return 100 if value is None else value

print("bad_default(0):", bad_default(0))
print("good_default(0):", good_default(0))

section("6. any/all")
print(any([0, "", 5]))
print(all([1, "x", True]))
print("all([]):", all([]))
print("any([]):", any([]))
