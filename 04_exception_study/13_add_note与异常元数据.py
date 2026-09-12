# -*- coding: utf-8 -*-
"""
13 Exception.add_note() 与异常元数据（Python 3.11+）
=================================================

当你想增加上下文，但又不想改变异常类型/因果链时，add_note 很有用。
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 给异常补充上下文")
try:
    exc = ValueError("CSV 字段无法解析")
    exc.add_note("文件: users.csv")
    exc.add_note("行号: 37")
    raise exc
except ValueError as exc:
    print("message:", exc)
    print("notes:", exc.__notes__)


show("2. 中间层可以追加上下文后原样 re-raise")
def parse_record(text, row_no):
    try:
        return int(text)
    except ValueError as exc:
        exc.add_note(f"row={row_no}")
        exc.add_note(f"raw={text!r}")
        raise

try:
    parse_record("bad", 8)
except ValueError as exc:
    print(exc)
    print(exc.__notes__)


show("3. add_note 与 raise ... from ... 的区别")
print("add_note: 还是同一个异常，只补充诊断信息。")
print("raise NewError from old: 改变抽象层/异常类型，并建立明确因果链。")


show("4. note 仍可能包含敏感信息")
print("不要把密码、token、医疗隐私等直接塞进 note。")

print("\n练习：99_exercises.py -> ex25 ~ ex26")
