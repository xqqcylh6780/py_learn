# -*- coding: utf-8 -*-
"""
05 raise 与重新抛出
==================
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 主动抛异常")

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age 必须是 int")
    if age < 0:
        raise ValueError("age 不能小于 0")
    return age

for value in (20, -1, "20"):
    try:
        print("set_age", value, "->", set_age(value))
    except Exception as exc:
        print(type(exc).__name__, exc)


show("2. bare raise：保留原异常和 traceback")

def parse(text):
    try:
        return int(text)
    except ValueError:
        print("记录上下文后继续抛给上层")
        raise

try:
    parse("x")
except ValueError:
    print("上层仍收到原始 ValueError")


show("3. `raise exc` 与 `raise` 不完全等价")
print("在 except 中想原样继续传播，优先写 `raise`。")
print("它最准确地保留当前异常上下文和 traceback 语义。")


show("4. 不要用异常表达函数正常返回")
print("例如查找未命中有时应该返回 None；是否抛异常取决于 API 契约。")


show("5. NotImplemented 和 NotImplementedError 不一样")
print("NotImplemented 是特殊返回值，主要给二元运算协议。")
print("NotImplementedError 是异常，用于明确表示功能/接口尚未实现。")

print("\n练习：99_exercises.py -> ex09 ~ ex10")
