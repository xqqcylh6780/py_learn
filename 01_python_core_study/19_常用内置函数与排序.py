# -*- coding: utf-8 -*-
"""
19 常用内置函数与排序
====================
"""

from operator import itemgetter


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. sorted 返回新 list，list.sort 原地修改")
data = [3, 1, 2]
print(sorted(data))
print("original:", data)
data.sort(reverse=True)
print("after sort:", data)

section("2. key 决定排序依据")
users = [("Alice", 30), ("Bob", 20), ("Carol", 25)]
print(sorted(users, key=lambda x: x[1]))
print(sorted(users, key=itemgetter(1)))

section("3. Python 排序是稳定的")
records = [("A", 2), ("B", 1), ("C", 2)]
print(sorted(records, key=lambda x: x[1]))
print("同 key 的 A/C 保持原相对顺序。")

section("4. min/max 也支持 key")
print(min(users, key=lambda x: x[1]))
print(max(users, key=lambda x: x[1]))

section("5. sum/any/all")
nums = [1, 2, 3]
print(sum(nums))
print(any(n > 2 for n in nums))
print(all(n > 0 for n in nums))

section("6. map/filter 通常可被推导式替代")
print(list(map(str, nums)))
print(list(filter(lambda n: n % 2, nums)))
print([str(n) for n in nums])
print([n for n in nums if n % 2])
