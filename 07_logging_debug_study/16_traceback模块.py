# -*- coding: utf-8 -*-
"""16 traceback：捕获、格式化、保留异常诊断信息。"""
import traceback


def level2():
    return 1 / 0

def level1():
    return level2()

try:
    level1()
except Exception as exc:
    print("format_exc():")
    text = traceback.format_exc()
    print(text)

    print("TracebackException：")
    tb = traceback.TracebackException.from_exception(exc)
    for line in tb.format():
        print(line, end="")

print("\n不要只记录 str(exc)：那会丢失调用栈。生产排错通常需要异常类型 + traceback。")
