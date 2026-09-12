# -*- coding: utf-8 -*-
"""19 inspect：运行时检查对象、签名和调用栈。"""
import inspect


def target(a: int, b: str = "x") -> str:
    return f"{a}:{b}"

print("signature:", inspect.signature(target))
print("isfunction:", inspect.isfunction(target))
print("module:", inspect.getmodule(target).__name__)


def who_called_me():
    frame = inspect.currentframe()
    try:
        caller = frame.f_back
        print("caller function:", caller.f_code.co_name)
    finally:
        # frame 对象会形成引用环，长期保存时尤其要谨慎。
        del frame


def caller():
    who_called_me()

caller()
print("\ninspect.stack() 很方便但成本较高；热路径不要频繁调用。")
