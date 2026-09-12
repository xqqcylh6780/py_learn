# -*- coding: utf-8 -*-
"""17 sys.excepthook / threading.excepthook / unraisablehook。"""
import sys
import threading

print("sys.excepthook 处理主线程未捕获异常。当前对象:", sys.excepthook)
print("threading.excepthook 处理 Thread.run 未捕获异常。当前对象:", threading.excepthook)
print("sys.unraisablehook 处理无法正常传播的异常，例如某些 __del__ 场景。")

# 不真正制造未捕获异常，避免教程执行失败。
def custom_excepthook(exc_type, exc_value, tb):
    print("CUSTOM:", exc_type.__name__, exc_value)

old = sys.excepthook
sys.excepthook = custom_excepthook
print("已临时安装 custom_excepthook（教程结束前恢复）")
sys.excepthook = old

print("\n服务框架通常已有自己的顶层异常处理，不要无脑覆盖全局 hook。")
