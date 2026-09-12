# -*- coding: utf-8 -*-
"""
14 函数是一等对象
================

函数可以赋值、传参、返回、放进容器。
"""

from functools import partial


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def add(a, b):
    """返回两个数之和。"""
    return a + b


section("1. 函数本身是对象")
print(add)
f = add
print(f(2, 3))
print(add.__name__)
print(add.__doc__)

section("2. 高阶函数：函数作为参数")
def apply(fn, value):
    return fn(value)

print(apply(abs, -5))

section("3. 函数作为返回值")
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

triple = multiplier(3)
print(triple(10))

section("4. partial 预绑定部分参数")
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(5))

section("5. 函数对象可以进容器")
operations = {"add": add, "abs": abs}
print(operations["add"](3, 4))
