# -*- coding: utf-8 -*-
"""
15 函数参数完整规则
==================

参数顺序：仅位置参数 / 普通参数 / *args / 仅关键字参数 / **kwargs
"""

import inspect


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. 普通参数与默认值")
def greet(name, age=18):
    return f"{name}:{age}"

print(greet("A"))
print(greet(name="A", age=20))

section("2. / 左侧参数只能按位置传")
def divide(a, b, /):
    return a / b

print(divide(8, 2))
try:
    divide(a=8, b=2)
except TypeError as exc:
    print(exc)

section("3. * 后参数只能按关键字传")
def connect(host, *, timeout=5, retry=3):
    return host, timeout, retry

print(connect("example.com", timeout=10))

section("4. *args 收集额外位置参数")
def total(*numbers):
    print(type(numbers).__name__, numbers)
    return sum(numbers)

print(total(1, 2, 3))

section("5. **kwargs 收集额外关键字参数")
def options(**kwargs):
    print(type(kwargs).__name__, kwargs)

options(debug=True, port=8000)

section("6. 完整签名")
def demo(a, b, /, c=0, *args, d, **kwargs):
    return a, b, c, args, d, kwargs

print(demo(1, 2, 3, 4, 5, d=6, x=7))
print(inspect.signature(demo))

section("7. 调用时 * / ** 展开")
pos = (1, 2)
kw = {"c": 3, "d": 4}
print(demo(*pos, **kw))
