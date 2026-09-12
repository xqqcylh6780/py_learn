# -*- coding: utf-8 -*-
"""
10 if 与 match/case 结构化模式匹配
=================================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. if/elif 适合条件判断")
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:
        return "PASS"
    return "FAIL"

print(grade(95), grade(70), grade(30))

section("2. match 是模式匹配，不只是 switch")
def describe(value):
    match value:
        case [0, 0]:
            return "origin"
        case [x, 0]:
            return f"x-axis({x})"
        case [0, y]:
            return f"y-axis({y})"
        case [x, y]:
            return f"point({x},{y})"
        case _:
            return "other"

for value in ([0, 0], [3, 0], [1, 2], [1, 2, 3]):
    print(value, "->", describe(value))

section("3. 映射模式只要求指定 key 存在")
def handle(msg):
    match msg:
        case {"type": "login", "user": user}:
            return f"login:{user}"
        case {"type": "logout", "user": user}:
            return f"logout:{user}"
        case _:
            return "unknown"

print(handle({"type": "login", "user": "Alice", "extra": 123}))

section("4. 守卫条件")
def classify(value):
    match value:
        case int() as n if n > 0:
            return "positive int"
        case int():
            return "non-positive int"
        case _:
            return "other"

print(classify(3), classify(0), classify("3"))

section("5. 注意捕获模式")
print("case name: 会把值绑定给 name；匹配常量应使用字面量、Enum 成员或限定名。")
