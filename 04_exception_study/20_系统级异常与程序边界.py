# -*- coding: utf-8 -*-
"""
20 系统级异常与程序边界
======================

本节处理那些“不应该被普通业务 except Exception 顺手吞掉”的信号。
"""

import asyncio


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. KeyboardInterrupt / SystemExit 不属于 Exception")
print("KeyboardInterrupt <: Exception:", issubclass(KeyboardInterrupt, Exception))
print("SystemExit <: Exception:", issubclass(SystemExit, Exception))
print("它们都直接继承 BaseException 分支，因此普通 except Exception 不会截住。")


show("2. asyncio.CancelledError 也需要特殊对待")
print("CancelledError <: BaseException:", issubclass(asyncio.CancelledError, BaseException))
print("CancelledError <: Exception:", issubclass(asyncio.CancelledError, Exception))
print("取消通常应在 finally 做清理，然后让取消继续传播。")


show("3. GeneratorExit")
print("生成器被 close() 时可收到 GeneratorExit。它表达生命周期终止，不是普通业务错误。")


show("4. 命令行顶层可以处理 Ctrl+C，转换退出码")
def cli_boundary(simulate_interrupt=False):
    try:
        if simulate_interrupt:
            raise KeyboardInterrupt
        return 0
    except KeyboardInterrupt:
        print("用户取消")
        return 130

print("模拟 Ctrl+C -> exit code", cli_boundary(True))


show("5. SyntaxError 的时间点")
print("当前 .py 文件本身语法错误时，代码通常还没开始执行，因此内部 try 无法救它。")
print("但动态 compile/eval/exec 的代码可以捕获 SyntaxError：")
try:
    compile("if : pass", "<demo>", "exec")
except SyntaxError as exc:
    print("捕获动态编译错误:", exc.msg)


show("6. 顶层边界的职责")
print("CLI/Web/worker 顶层可以：记录未处理异常、转换退出码/响应、执行最终清理。")
print("但不要把所有异常都变成‘成功’，否则监控和调用方会被误导。")

print("\n练习：99_exercises.py -> ex43 ~ ex44")
