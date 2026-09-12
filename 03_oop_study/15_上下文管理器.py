# -*- coding: utf-8 -*-
"""
15 上下文管理器 —— with 语句背后的协议
========================================

运行：  python 15_上下文管理器.py

with 解决的是「无论中途出什么事，收尾都要执行」这个老问题。
它替代的是 try/finally。
"""

import time
from contextlib import contextmanager, suppress


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 不用 with 要写多少
# ---------------------------------------------------------------
show("1. with 替代的是什么")

print("不用 with 的写法：")
print("    f = open('x.txt')")
print("    try:")
print("        ...")
print("    finally:")
print("        f.close()      # 必须记得写，忘了就漏资源")
print()
print("用 with：")
print("    with open('x.txt') as f:")
print("        ...            # 出了这个块自动关，出异常也照关")


# ---------------------------------------------------------------
# 2. 手写一个上下文管理器
# ---------------------------------------------------------------
show("2. __enter__ 和 __exit__")


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        print("   [enter] 开始计时")
        return self                     # 这个返回值给 as 后面的变量

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"   [exit]  耗时 {self.elapsed * 1000:.2f} 毫秒")
        return False                    # 返回 False = 异常继续往外抛


with Timer() as t:
    total = sum(range(1_000_000))
print("块外面还能拿到 t.elapsed:", round(t.elapsed, 4), "秒")


# ---------------------------------------------------------------
# 3. __exit__ 的三个参数与返回值
# ---------------------------------------------------------------
show("3. 出异常时会怎样")


class Watcher:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("   [exit] 正常结束，三个参数都是 None")
        else:
            print(f"   [exit] 出异常了: {exc_type.__name__}: {exc_value}")
        return False                    # 不吞，继续抛


print("正常情况：")
with Watcher():
    pass

print("出异常的情况：")
try:
    with Watcher():
        raise ValueError("故意炸一个")
except ValueError as e:
    print("   异常被外面的 try 接住了:", e)


show("4. 返回 True 就能吞掉异常")


class Swallow:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"   吞掉: {exc_value}")
        return True                     # True = 这个异常我处理了，别往外传


with Swallow():
    raise RuntimeError("这个异常不会被抛出去")

print("   程序继续往下走了，说明异常真的被吞了")
print()
print("这个能力要小心用：__exit__ 返回真值时会抑制异常；返回 False 或 None 都会继续向外抛。")


# ---------------------------------------------------------------
# 5. 用生成器函数一行搞定
# ---------------------------------------------------------------
show("5. @contextmanager —— 不用写类了")


@contextmanager
def tag(name):
    print(f"   <{name}>")
    try:
        yield                           # 这里就是 with 块的内容
    finally:
        print(f"   </{name}>")           # 即使 with 块抛异常也保证收尾


with tag("div"):
    print("   中间的内容")


@contextmanager
def transaction(name):
    """把 yield 包在 try 里，就能处理异常。"""
    print(f"   BEGIN {name}")
    try:
        yield
    except Exception as e:
        print(f"   ROLLBACK {name}（原因: {e}）")
    else:
        print(f"   COMMIT {name}")


with transaction("下单"):
    print("   扣库存、扣余额")

with transaction("下单2"):
    print("   扣库存")
    raise ValueError("余额不足")

print()
print("写法要点：")
print("  yield 之前的代码 = __enter__")
print("  yield 之后的代码 = __exit__")
print("  把 yield 放进 try/except 就能模拟「异常处理」")
print("  注意：生成器函数只能 yield 一次，否则会报错")


# ---------------------------------------------------------------
# 6. 标准库里的好帮手
# ---------------------------------------------------------------
show("6. contextlib 里现成的工具")

with suppress(FileNotFoundError):
    open("这个文件不存在.txt")
print("   suppress 把 FileNotFoundError 吃掉了，无需 try")

from contextlib import ExitStack

with ExitStack() as stack:
    names = []
    for n in ["A", "B", "C"]:
        stack.enter_context(tag(n))
        names.append(n)
    print("   同时进入了:", names)
print("   ExitStack 适合「数量不确定的多个资源」")


# ---------------------------------------------------------------
# 7. 什么时候该写上下文管理器
# ---------------------------------------------------------------
show("7. 什么时候该写")

print("典型信号：某段代码总是成对出现「开始...结束」，而且结束必须执行。")
print()
print("  - 打开/关闭（文件、连接、锁）")
print("  - 开始/提交或回滚（数据库事务）")
print("  - 进入/退出临时状态（改工作目录、切上下文变量）")
print("  - 开始/结束计时、埋点")
print()
print("判断标准很简单：如果写在 finally 里，多半就能做成上下文管理器。")


show("练习：去 99_exercises.py 做 ex23")
