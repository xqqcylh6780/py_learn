# -*- coding: utf-8 -*-
"""
13 推导式与生成器表达式
======================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. list comprehension")
squares = [x * x for x in range(8)]
print(squares)

section("2. 过滤条件")
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

section("3. 条件表达式位于 for 前面")
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)

section("4. dict/set comprehension")
print({x: x * x for x in range(4)})
print({x % 3 for x in range(10)})

section("5. 嵌套推导式的阅读顺序与 for 一致")
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]
print(flat)

section("6. generator expression 惰性产生值")
gen = (x * x for x in range(4))
print(gen)
print(next(gen))
print(list(gen))

section("7. 不要为了炫技堆复杂推导式")
print("超过两层、分支复杂、需要副作用时，普通 for 往往更清楚。")
