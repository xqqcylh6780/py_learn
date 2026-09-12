# -*- coding: utf-8 -*-
"""03 itertools：无限迭代器与常用组合工具"""
from itertools import count, cycle, repeat, chain, islice, takewhile, dropwhile

print("=== count + islice：无限序列必须限制 ===")
print(list(islice(count(10, 3), 5)))

print("\n=== cycle ===")
print(list(islice(cycle("ABC"), 8)))

print("\n=== repeat ===")
print(list(repeat("x", 3)))

print("\n=== chain / chain.from_iterable ===")
print(list(chain([1, 2], [3], [4, 5])))
print(list(chain.from_iterable([[1, 2], [3], [4, 5]])))

print("\n=== takewhile / dropwhile ===")
data = [1, 2, 3, 0, 4, 5]
print("takewhile:", list(takewhile(lambda x: x > 0, data)))
print("dropwhile:", list(dropwhile(lambda x: x > 0, data)))
print("注意：它们只处理“前缀条件”，不是全局 filter。")

print("\n=== 惰性 ===")
print("itertools 大多返回迭代器；适合流式处理，但通常只能消费一次。")
