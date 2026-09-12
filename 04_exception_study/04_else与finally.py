# -*- coding: utf-8 -*-
"""
04 else 与 finally —— 把成功路径和清理路径分开
===============================================
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. else 只在 try 正常完成时执行")
try:
    n = int("42")
except ValueError:
    print("解析失败")
else:
    print("解析成功:", n)


show("2. else 的价值：缩小 try 范围")

def parse_and_double(text):
    try:
        n = int(text)
    except ValueError:
        return None
    else:
        # 如果这里出现别的 bug，不会被上面的 ValueError 处理逻辑混进去。
        return n * 2

print(parse_and_double("21"))


show("3. finally 无论成功、失败、return，通常都会执行")

def demo_return():
    try:
        print("try")
        return "result"
    finally:
        print("finally: 清理资源")

print("返回值:", demo_return())


show("4. finally 中 return 会吞掉异常 —— 强烈避免")

def dangerous():
    try:
        1 / 0
    finally:
        return "异常被 return 覆盖了"

print(dangerous())
print("这就是为什么 finally 里通常只做清理，不写 return/break/continue。")


show("5. 文件资源优先用 with，而不是手写 finally")
print("with open(...) 会把关闭资源的清理职责交给上下文管理器。")


show("6. finally 适合哪些资源")
print("锁、临时状态恢复、事务回滚/收尾、外部句柄等。")

print("\n练习：99_exercises.py -> ex07 ~ ex08")
