# -*- coding: utf-8 -*-
"""
21 迭代协议基础
==============

这里只讲核心语义；更深入的生成器协议放在 03_oop_study。
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. iter(obj) 得到迭代器")
items = [10, 20, 30]
it = iter(items)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
    next(it)
except StopIteration:
    print("迭代结束 -> StopIteration")

section("2. for 会自动处理迭代器")
for x in [1, 2, 3]:
    print(x)

section("3. 容器通常可重复迭代；迭代器通常一次性")
container = [1, 2]
print(list(container), list(container))
it = iter(container)
print(list(it))
print(list(it), "<- 已耗尽")

section("4. 判断是否可迭代的直接方式")
def is_iterable(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    return True

print(is_iterable([1, 2]))
print(is_iterable(123))

section("5. generator expression 本身就是迭代器")
gen = (x * 2 for x in range(3))
print(iter(gen) is gen)
print(list(gen))
