# -*- coding: utf-8 -*-
"""
11 traceback 与异常诊断
======================
"""

import traceback


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


def level_b():
    return 1 / 0


def level_a():
    return level_b()


show("1. traceback 告诉你调用路径")
try:
    level_a()
except ZeroDivisionError as exc:
    print("异常类型:", type(exc).__name__)
    print("异常消息:", exc)
    tb = traceback.format_exc()
    print("格式化 traceback（截取末几行）:")
    print("\n".join(tb.strip().splitlines()[-5:]))


show("2. traceback.format_exception")
try:
    int("bad")
except ValueError as exc:
    lines = traceback.format_exception(exc)
    print("".join(lines).strip())


show("3. traceback.print_exc")
print("它会把当前正在处理的异常打印到 stderr，适合临时诊断；正式项目更常交给 logging.exception。")


show("4. sys.exception() / sys.exc_info()")
import sys
try:
    {}["missing"]
except KeyError:
    current = sys.exception()  # Python 3.11+
    print("sys.exception():", type(current).__name__, current)
    exc_type, exc, tb = sys.exc_info()
    print("sys.exc_info()[0]:", exc_type.__name__)


show("5. traceback 是诊断信息，不应直接完整暴露给终端用户")
print("Web/API 通常对外返回稳定错误信息，对内日志保存完整 traceback。")

print("\n练习：99_exercises.py -> ex21 ~ ex22")
