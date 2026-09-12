# -*- coding: utf-8 -*-
"""
27 sys.settrace：调试器和覆盖率工具的基础机制之一
=================================================

trace 函数会收到 call / line / return / exception 等事件。
它非常强，但运行开销明显，不应随便在生产热路径长期开启。
"""
import sys

events = []

def tracer(frame, event, arg):
    if frame.f_code.co_name == "demo" and event in {"call", "line", "return"}:
        events.append((event, frame.f_lineno))
    return tracer

def demo(x):
    y = x + 1
    return y * 2

old = sys.gettrace()
sys.settrace(tracer)
try:
    result = demo(3)
finally:
    sys.settrace(old)

print("result:", result)
print("trace events:", events)
print("\npdb、IDE 调试器、覆盖率工具会使用类似的解释器追踪/监控能力。")
print("不要在 trace 回调里做复杂工作，否则会严重拖慢程序。")
