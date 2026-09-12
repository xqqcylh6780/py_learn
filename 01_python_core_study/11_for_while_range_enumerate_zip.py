# -*- coding: utf-8 -*-
"""
11 循环：for、while、range、enumerate、zip
========================================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. for 遍历可迭代对象")
for ch in "abc":
    print(ch)

section("2. range 适合次数/整数范围")
print(list(range(5)))
print(list(range(2, 10, 2)))

section("3. enumerate 比手写索引更清楚")
for index, name in enumerate(["A", "B", "C"], start=1):
    print(index, name)

section("4. zip 并行遍历")
names = ["A", "B", "C"]
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print(name, score)

section("5. zip 默认按最短输入停止")
print(list(zip([1, 2, 3], ["a"])))
print("需要检测长度不一致时，Python 3.10+ 可用 zip(..., strict=True)。")
try:
    print(list(zip([1, 2], ["a"], strict=True)))
except ValueError as exc:
    print("strict 检测到长度不一致:", exc)

section("6. while 适合由条件驱动的循环")
n = 3
while n > 0:
    print(n)
    n -= 1
