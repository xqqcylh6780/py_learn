# -*- coding: utf-8 -*-
"""
09 资源清理与上下文管理器
========================

本节不重复 OOP 的上下文管理器实现细节，重点放在“异常安全”。
"""

from contextlib import contextmanager


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. with 保证退出逻辑被调用")
with open(__file__, "r", encoding="utf-8") as f:
    first_line = f.readline().strip()
print("文件已关闭:", f.closed)
print("第一行:", first_line)


show("2. contextmanager 必须把 yield 放在 try/finally 中")
@contextmanager
def managed_state():
    print("进入：占用资源")
    try:
        yield "resource"
    finally:
        print("退出：释放资源")

try:
    with managed_state() as resource:
        print("使用", resource)
        raise ValueError("模拟失败")
except ValueError:
    print("异常继续传播，但资源已经释放")


show("3. __exit__ / contextmanager 可以选择压制异常")
@contextmanager
def suppress_value_error():
    try:
        yield
    except ValueError as exc:
        print("明确处理并压制:", exc)

with suppress_value_error():
    raise ValueError("这个错误被上下文管理器处理")
print("程序继续")


show("4. 压制异常必须是明确设计，不要无意吞掉")
print("清理资源 != 吞掉异常。绝大多数清理型上下文管理器应该让异常继续传播。")


show("5. ExitStack 适合动态数量资源")
from contextlib import ExitStack
with ExitStack() as stack:
    f1 = stack.enter_context(open(__file__, "r", encoding="utf-8"))
    f2 = stack.enter_context(open(__file__, "r", encoding="utf-8"))
    print("两个文件都打开:", not f1.closed and not f2.closed)
print("退出后:", f1.closed and f2.closed)

print("\n练习：99_exercises.py -> ex17 ~ ex18")
