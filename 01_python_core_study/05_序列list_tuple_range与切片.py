# -*- coding: utf-8 -*-
"""
05 序列：list、tuple、range 与切片
================================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. list 是可变序列")
items = [10, 20, 30]
items.append(40)
items[0] = 99
print(items)

section("2. tuple 是不可变序列")
point = (3, 4)
print(point[0], point[1])
print("单元素 tuple 必须写 (1,)，不是 (1)。")
print(type((1,)).__name__, type((1)).__name__)

section("3. range 是惰性的整数序列")
r = range(1, 10, 2)
print(r)
print(list(r))
print(5 in r)

section("4. 切片 start:stop:step")
data = list(range(10))
print(data[2:7])
print(data[:4])
print(data[::2])
print(data[::-1])
print(data[-3:])

section("5. list 切片通常创建新 list")
a = [[1], [2]]
b = a[:]
b.append([3])
b[0].append(9)
print("a:", a)
print("b:", b)
print("外层不同，但内部元素仍共享引用。")

section("6. 切片赋值可以改变 list 长度")
nums = [1, 2, 3, 4]
nums[1:3] = [20, 30, 40]
print(nums)

section("7. 不要用乘法创建共享二维行")
bad = [[0] * 3] * 3
bad[0][0] = 1
print("bad:", bad)
good = [[0] * 3 for _ in range(3)]
good[0][0] = 1
print("good:", good)
