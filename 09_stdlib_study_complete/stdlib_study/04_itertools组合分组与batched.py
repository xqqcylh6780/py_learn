# -*- coding: utf-8 -*-
"""04 itertools：product、permutations、combinations、groupby、pairwise、batched"""
from itertools import (
    product, permutations, combinations, combinations_with_replacement,
    groupby, pairwise, batched,
)

print("=== 笛卡尔积 ===")
print(list(product("AB", [1, 2])))

print("\n=== 排列 / 组合 ===")
print("P:", list(permutations("ABC", 2)))
print("C:", list(combinations("ABC", 2)))
print("CR:", list(combinations_with_replacement("AB", 2)))

print("\n=== pairwise ===")
print(list(pairwise([10, 15, 9, 20])))

print("\n=== batched（Python 3.12+）===")
print(list(batched(range(10), 3)))

print("\n=== groupby 最重要的坑：只分连续组 ===")
records = [("A", 1), ("B", 2), ("A", 3)]
print([(k, list(g)) for k, g in groupby(records, key=lambda x: x[0])])
print("如果想把所有相同 key 放一起，要先按相同 key 排序，或使用 defaultdict。")
records.sort(key=lambda x: x[0])
print([(k, list(g)) for k, g in groupby(records, key=lambda x: x[0])])
