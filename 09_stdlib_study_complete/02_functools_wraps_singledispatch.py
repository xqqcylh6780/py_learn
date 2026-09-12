# -*- coding: utf-8 -*-
"""02 functools：wraps、singledispatch、reduce

重点：装饰器元数据、按“第一个参数类型”分派，以及 reduce 的取舍。
"""
from functools import wraps, singledispatch, reduce

print("=== 1. wraps 保留被装饰函数元数据 ===")
def trace(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("call", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@trace
def add(a: int, b: int) -> int:
    """两数相加。"""
    return a + b

print(add(2, 3), add.__name__, add.__doc__)
print("__wrapped__ ->", add.__wrapped__)

print("\n=== 2. singledispatch ===")
@singledispatch
def render(value):
    return f"object:{value!r}"

@render.register
def _(value: int):
    return f"int:{value}"

@render.register
def _(value: list):
    return "list:" + ",".join(map(str, value))

for x in [3, [1, 2], {"a": 1}]:
    print(render(x))

print("\n=== 3. singledispatch 只看第一个参数的运行时类型 ===")
print(render.dispatch(int))
print(render.registry)

print("\n=== 4. reduce ===")
print(reduce(lambda acc, x: acc * x, [1, 2, 3, 4], 1))
print("求和、最大值等已有 sum/max 时优先用专用函数；reduce 适合明确的累计折叠。")
