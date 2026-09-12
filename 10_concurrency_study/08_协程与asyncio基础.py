# -*- coding: utf-8 -*-
"""
08 协程与 asyncio 基础 —— 单线程也能并发
==========================================

运行：  python 08_协程与asyncio基础.py

协程干的事和线程一样（在等待时切换去干别的），
但它把「什么时候切换」的决定权交给了你的代码 —— 靠 await 显式让出。
"""

import asyncio
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


async def fetch(name, delay=0.2):
    """模拟一次网络请求。"""
    print(f"   [{name}] 开始请求")
    await asyncio.sleep(delay)          # 关键：这里是「让出去」，不是「傻等」
    print(f"   [{name}] 拿到结果")
    return f"{name} 的数据"


# ---------------------------------------------------------------
# 1. 协程函数长得就不一样
# ---------------------------------------------------------------
def part1_syntax():
    show("1. async def 定义的是「协程函数」")

    print("调用普通函数 -> 立刻执行，返回结果")
    print("调用协程函数 -> 不执行！只返回一个「协程对象」")
    print()

    coro = fetch("X", 0.1)
    print("  fetch('X') 拿到了什么:", coro)
    print("  类型:", type(coro).__name__)
    print()
    print("注意上面一行都没打印出来 —— 函数体根本没跑。")
    print("要让它跑，必须交给事件循环，比如 asyncio.run() 或者 await 它。")
    print()
    print("  await 的含义 = 「我在这里等，但你可以先去干别的」")
    print("  它和 time.sleep 最大的区别：sleep 是死等，await 是会主动让位。")
    coro.close()                        # 关掉它，避免 RuntimeWarning


# ---------------------------------------------------------------
# 2. 串行 await vs 并发 gather
# ---------------------------------------------------------------
def part2_serial_vs_concurrent():
    show("2. 最容易搞错的地方：await 不等于并发")

    async def serial():
        t0 = time.perf_counter()
        await fetch("A", 0.2)
        await fetch("B", 0.2)
        await fetch("C", 0.2)
        return time.perf_counter() - t0

    async def concurrent():
        t0 = time.perf_counter()
        await asyncio.gather(
            fetch("A", 0.2),
            fetch("B", 0.2),
            fetch("C", 0.2),
        )
        return time.perf_counter() - t0

    print("写法一：一个接一个 await")
    t_serial = asyncio.run(serial())
    print(f"   总耗时 {t_serial:.2f} 秒")

    print()
    print("写法二：用 asyncio.gather 一起交出去")
    t_concurrent = asyncio.run(concurrent())
    print(f"   总耗时 {t_concurrent:.2f} 秒")

    print()
    print(f"  提速 {t_serial / t_concurrent:.1f} 倍")
    print()
    print("同样是 await，为什么差这么多？")
    print("  await fetch(...) 是「等这一个做完，才轮到下一行」—— 这是串行")
    print("  gather 是「把三个都交给事件循环，谁好了叫醒我」—— 这才是并发")
    print()
    print("记住：光写 async/await 不会自动变并发，得用 gather / create_task")
    print("把任务「同时交出去」。这是新手最常见的误区。")


# ---------------------------------------------------------------
# 3. create_task：真正把任务派出去
# ---------------------------------------------------------------
def part3_create_task():
    show("3. create_task —— 明确的「现在就派活」")

    async def demo():
        t0 = time.perf_counter()
        tasks = [asyncio.create_task(fetch(f"T{i}", 0.15)) for i in range(3)]
        print("   三个任务已经派出去了，下面开始收结果")
        results = []
        for t in tasks:
            results.append(await t)     # 逐个收，但它们在并行跑
        return results, time.perf_counter() - t0

    results, elapsed = asyncio.run(demo())
    print(f"   结果: {results}")
    print(f"   总耗时 {elapsed:.2f} 秒")
    print()
    print("create_task 和 gather 的区别：")
    print("  create_task 立刻把协程交给事件循环，返回一个 Task 句柄")
    print("  gather 一步到位，帮你把结果收集成列表")
    print()
    print("要边跑边处理结果，用 create_task；只是收集全部结果，用 gather。")


# ---------------------------------------------------------------
# 4. 事件循环是什么
# ---------------------------------------------------------------
def part4_event_loop():
    show("4. 事件循环：协程背后的调度器")

    print("asyncio.run(main()) 干了这些事：")
    print("  1. 创建一个事件循环")
    print("  2. 把 main() 协程丢进去跑")
    print("  3. 跑完就关掉循环")
    print()
    print("事件循环的日常工作就一句话：")
    print("  「谁准备好了就推进谁，都没准备好就等着」")
    print()

    async def peek():
        print("   当前任务:", asyncio.current_task().get_name())
        print("   所有任务:", [t.get_name() for t in asyncio.all_tasks() if t is not asyncio.current_task()])
        print("   循环在跑吗:", asyncio.get_running_loop().is_running())

    asyncio.run(peek())

    print()
    print("一个线程同一时刻只能运行一个事件循环；asyncio 的常见用法是在单线程事件循环里做协作式并发。")


# ---------------------------------------------------------------
# 5. 和线程比，好在哪
# ---------------------------------------------------------------
def part5_why_better():
    show("5. 协程相比线程的优势")

    async def quiet_worker(n):
        await asyncio.sleep(0.05)
        return n

    async def spawn_many():
        t0 = time.perf_counter()
        tasks = [asyncio.create_task(quiet_worker(i)) for i in range(500)]
        results = await asyncio.gather(*tasks)
        return results, time.perf_counter() - t0

    t0 = time.perf_counter()
    results, elapsed = asyncio.run(spawn_many())
    print(f"   同时跑 500 个协程: {elapsed:.2f} 秒")
    print(f"   全部拿到结果吗: {len(results) == 500 and sum(results) == sum(range(500))}")
    print()
    print("对比一下开 500 个线程：")
    print("  - 每个线程都有独立栈空间，具体默认大小取决于操作系统/运行时，几百个线程会显著增加内存占用")
    print("  - 线程切换由操作系统管，切换成本比协程高得多")
    print()
    print("协程的优势：")
    print("  1. 极轻量，开几万个都不怕")
    print("  2. 切换点通常发生在 await 附近，调度更可控")
    print("  3. 竞态更少但并非不存在：多个协程共享可变状态，并在读写之间 await，仍可能发生逻辑竞态")
    print()
    print("代价：只要有一处「不 await 的阻塞调用」，整个循环就卡死。")
    print("这是协程最需要小心的地方，10 节会专门讲。")


# ---------------------------------------------------------------
# 6. 忘了 await 会怎样
# ---------------------------------------------------------------
def part6_forgot_await():
    show("6. 坑：忘了写 await")

    import gc
    import warnings

    ran = []

    async def tracked(name):
        ran.append(name)
        await asyncio.sleep(0.01)

    async def bad():
        tracked("这个任务本该跑起来")       # 少了 await，协程对象被直接丢掉
        return "我返回了"

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = asyncio.run(bad())
        gc.collect()        # 强制回收那个被丢掉的协程，好让警告立刻出现

    print("   证据一：函数照样返回了:", result)
    print("   证据二：被丢掉的协程跑了吗 -> ran =", ran, " <- 空的，根本没执行")
    for w in caught:
        print("   证据三：Python 的警告 ->", str(w.message))

    print()
    print("这个坑很阴：程序不报错，只是那个协程从来没被执行过。")
    print("现象是「某个请求莫名其妙没发出去」「某个任务永远没跑」。")
    print()
    print("而且这个警告是协程对象被垃圾回收时才发的，可能离出错的地方很远。")
    print("看到 'coroutine ... was never awaited' 一定要回头查，别当噪音忽略。")


# ---------------------------------------------------------------
# 7. 三个概念对照
# ---------------------------------------------------------------
def part7_terminology():
    show("7. 协程 / 任务 / 事件循环")

    rows = [
        ("协程 (coroutine)", "async def 定义的函数调用后得到的东西", "还没排班"),
        ("任务 (Task)", "用 create_task 把协程交出去后的结果", "已排班，正在跑"),
        ("事件循环 (loop)", "调度器，负责推进所有任务", "只有一个，在某个线程里"),
    ]
    print(f"  {'概念':<20}{'是什么':<40}状态")
    print("  " + "-" * 72)
    for a, b, c in rows:
        print(f"  {a:<20}{b:<40}{c}")

    print()
    print("一句话串起来：把「协程」用 create_task 交给「事件循环」，")
    print("它就变成了一个正在跑的「任务」。")


def main():
    part1_syntax()
    part2_serial_vs_concurrent()
    part3_create_task()
    part4_event_loop()
    part5_why_better()
    part6_forgot_await()
    part7_terminology()

    show("练习：去 99_exercises.py 做 ex12 ~ ex13")


if __name__ == "__main__":
    main()
