# -*- coding: utf-8 -*-
"""20 faulthandler：死锁/崩溃/卡住时的低级诊断工具。"""
import faulthandler
import sys

print("faulthandler 是否已启用:", faulthandler.is_enabled())
faulthandler.enable()
print("启用后:", faulthandler.is_enabled())

print("\n常用能力：")
print("- faulthandler.dump_traceback()：立即打印所有线程的 Python 栈")
print("- dump_traceback_later(seconds)：超时后自动打印栈，可定位卡死")
print("- cancel_dump_traceback_later()：取消定时 dump")
print("- 可通过 PYTHONFAULTHANDLER=1 或 -X faulthandler 启用")

print("\n演示当前线程栈：")
faulthandler.dump_traceback(file=sys.stdout)

print("不会在教程里故意 segfault。")
print("生产环境应把输出写到可长期保存的文件描述符，并考虑多进程日志归属。")
print("栈信息可能包含路径、函数名和业务上下文，收集与共享时仍需遵守敏感信息规则。")
