# -*- coding: utf-8 -*-
"""
14 ExceptionGroup 与 except*（Python 3.11+）
===========================================

并发任务可能同时失败；一个异常对象不够表达多个独立错误。
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. ExceptionGroup 可以包含多个异常")
group = ExceptionGroup(
    "批处理失败",
    [ValueError("第1条格式错"), TypeError("第2条类型错")],
)
print(group)
print("子异常数:", len(group.exceptions))


show("2. except* 会按类型拆分异常组")
try:
    raise ExceptionGroup(
        "mixed",
        [ValueError("bad value"), TypeError("bad type"), ValueError("bad value 2")],
    )
except* ValueError as eg:
    print("处理 ValueError 子组:", len(eg.exceptions))
except* TypeError as eg:
    print("处理 TypeError 子组:", len(eg.exceptions))


show("3. except* 不是普通 except 的另一种拼写")
print("它是为了异常组的并行拆分处理；一个组中不同异常可分别命中不同 except*。")


show("4. BaseExceptionGroup")
print("ExceptionGroup 只能装 Exception 子类。")
print("需要包含 KeyboardInterrupt 等 BaseException 时，由 BaseExceptionGroup 表达。")


show("5. TaskGroup 是常见来源")
print("asyncio.TaskGroup 中多个任务失败时，退出上下文可能抛 ExceptionGroup。")

print("\n练习：99_exercises.py -> ex27 ~ ex28")
