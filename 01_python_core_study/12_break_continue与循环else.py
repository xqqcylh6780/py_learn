# -*- coding: utf-8 -*-
"""
12 break、continue 与循环 else
=============================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. continue 跳过本轮剩余部分")
for n in range(6):
    if n % 2:
        continue
    print("even:", n)

section("2. break 立即结束最近一层循环")
for n in range(10):
    if n == 3:
        break
    print(n)

section("3. 循环 else：没有被 break 才执行")
def contains_factor(n):
    for d in range(2, n):
        if n % d == 0:
            print(n, "factor:", d)
            break
    else:
        print(n, "没有找到因子")

contains_factor(7)
contains_factor(8)

section("4. while 也可以有 else")
n = 2
while n:
    n -= 1
else:
    print("正常耗尽条件，所以执行 else")

section("5. 多层循环的 break 只跳一层")
print("复杂多层退出通常用函数 return、状态变量或拆函数，避免晦涩控制流。")
