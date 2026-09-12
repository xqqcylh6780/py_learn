# -*- coding: utf-8 -*-
"""
02 类型、可变性与可哈希性
========================

重点：mutable、immutable、hashable 是不同概念。
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. 常见不可变类型")
examples = [1, 1.5, True, None, "abc", (1, 2), frozenset({1, 2}), b"abc"]
for value in examples:
    print(type(value).__name__, repr(value))

section("2. 常见可变类型")
for value in [[1], {"a": 1}, {1, 2}, bytearray(b"abc")]:
    print(type(value).__name__, repr(value))

section("3. tuple 不可变，但元素可以指向可变对象")
t = ([1, 2], "x")
t[0].append(3)
print(t)
print("不能替换 t[0]，但 t[0] 指向的 list 自己可以变化。")

section("4. hashable 才能当 dict key / set element")
for value in [1, "x", (1, 2), frozenset({1, 2})]:
    print(repr(value), "hash =", hash(value))

for value in [[1, 2], {"a": 1}, {1, 2}]:
    try:
        hash(value)
    except TypeError as exc:
        print(type(value).__name__, "不可哈希:", exc)

section("5. tuple 是否可哈希取决于其元素")
print("hash((1, 2)):", hash((1, 2)))
try:
    hash(([1], 2))
except TypeError as exc:
    print("包含 list 的 tuple 不可哈希:", exc)

section("结论")
print("不可变不自动意味着可哈希；容器能否哈希还取决于其成员和类型定义。")
