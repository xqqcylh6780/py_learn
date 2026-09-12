# -*- coding: utf-8 -*-
"""
09 asyncio 并发控制 —— 限流、超时、取消
==========================================

运行：  python 09_asyncio并发控制.py

光会 gather 还不够。真实项目里还要控制并发数量、设置超时、
处理某个任务失败、主动取消跑太久的任务。
"""

import asyncio
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


async def fetch(name, delay=0.1):
    await asyncio.sleep(delay)
    return f"{name}({delay}s)"


# ---------------------------------------------------------------
# 1. gather vs as_completed
# ---------------------------------------------------------------
async def part1_gather_vs_as_completed():
    show("1. gather 和 as_completed 的区别")

    print("  gather：全部跑完，按「输入顺序」给你结果")
    t0 = time.perf_counter()
    results = await asyncio.gather(
        fetch("慢", 0.25), fetch("快", 0.05), fetch("中", 0.12)
    )
    print(f"    {results}   耗时 {time.perf_counter() - t0:.2f} 秒")

    print()
    print("  as_completed：谁先完成先给你谁")
    t0 = time.perf_counter()
    order = []
    for coro in asyncio.as_completed(
        [fetch("慢", 0.25), fetch("快", 0.05), fetch("中", 0.12)]
    ):
        order.append(await coro)
    print(f"    {order}   耗时 {time.perf_counter() - t0:.2f} 秒")

    print()
    print("  两者总耗时一样（都由最慢那个决定），区别只在「交付顺序」。")
    print("  想边完成边处理用 as_completed；只想拿全部结果用 gather。")


# ---------------------------------------------------------------
# 2. 超时
# ---------------------------------------------------------------
async def part2_timeout():
    show("2. 超时控制")

    print("  方式一：asyncio.wait_for")
    try:
        await asyncio.wait_for(fetch("慢接口", 1.0), timeout=0.15)
    except asyncio.TimeoutError:
        print("    wait_for 超时 -> asyncio.TimeoutError")
        print("    注意：那个任务会被取消，不是「不管它继续跑」")

    print()
    print("  方式二：asyncio.timeout（Python 3.11+，可以包住一整段代码）")
    try:
        async with asyncio.timeout(0.15):
            await fetch("接口A", 0.05)
            print("    接口A 成功")
            await fetch("接口B", 1.0)
            print("    这行永远不会执行")
    except asyncio.TimeoutError:
        print("    超时了，整段被打断")

    print()
    print("  两者区别：")
    print("    wait_for -> 管「一个协程」")
    print("    timeout  -> 管「一整段代码」，里面可以有很多 await")


# ---------------------------------------------------------------
# 3. Semaphore 限流
# ---------------------------------------------------------------
async def part3_semaphore():
    show("3. Semaphore 限流（协程版）")

    sem = asyncio.Semaphore(3)
    state = {"active": 0, "peak": 0}

    async def limited(name):
        async with sem:                     # 最多 3 个同时进来
            state["active"] += 1
            state["peak"] = max(state["peak"], state["active"])
            await asyncio.sleep(0.08)
            state["active"] -= 1
            return name

    t0 = time.perf_counter()
    await asyncio.gather(*[limited(f"任务{i}") for i in range(10)])
    elapsed = time.perf_counter() - t0

    print("    10 个任务，每个耗时 0.08 秒")
    print(f"    最大并发数: {state['peak']}   （限制是 3）")
    print(f"    总耗时: {elapsed:.2f} 秒   （不限流只要 0.08 秒）")
    print()
    print("  为什么需要限流？")
    print("    - 对方接口有 QPS 限制，打太快会被封")
    print("    - 数据库连接池只有 10 个，开 1000 个协程只会互相等")
    print("    - 本机文件句柄、内存都是有限的")
    print()
    print("  协程虽然轻量，但「同时打出去的请求数」还是要控制。")


# ---------------------------------------------------------------
# 4. TaskGroup
# ---------------------------------------------------------------
async def part4_task_group():
    show("4. TaskGroup —— 一个失败，全部收手")

    async def may_fail(n):
        await asyncio.sleep(0.05)
        if n == 2:
            raise ValueError(f"任务{n} 炸了")
        return f"任务{n} 成功"

    print("  用 TaskGroup 跑 4 个任务，其中一个是坏的：")
    try:
        async with asyncio.TaskGroup() as tg:
            for i in range(4):
                tg.create_task(may_fail(i))
    except* ValueError as eg:
        print(f"    捕获到 {len(eg.exceptions)} 个异常: {eg.exceptions[0]}")
        print("    其余还没跑完的任务会被自动取消")

    print()
    print("  对比 gather：")
    print("    gather    默认「一个失败，其他继续跑」，异常要单独处理")
    print("    TaskGroup 一个失败立刻取消全部，并汇总成 ExceptionGroup")
    print()
    print("  except* 是 Python 3.11 新增的语法，专门用来接 ExceptionGroup。")
    print("  新项目建议优先 TaskGroup —— 它不会留下没人管的孤儿任务。")


# ---------------------------------------------------------------
# 5. 取消任务
# ---------------------------------------------------------------
async def part5_cancel():
    show("5. 主动取消任务")

    async def long_running():
        try:
            print("    长任务开始了")
            await asyncio.sleep(10)
            print("    这行永远不会执行")
        except asyncio.CancelledError:
            print("    收到取消信号，正在清理（关文件、回滚事务）")
            raise                           # 记得重新抛出，别吞掉

    task = asyncio.create_task(long_running())
    await asyncio.sleep(0.1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("    确认已取消")

    print()
    print("  取消是「协作式」的：cancel() 只是发个信号，")
    print("  真正的取消发生在任务下一次执行到 await 的时候。")
    print()
    print("  所以如果协程里有长时间不 await 的同步代码（死循环、大计算），")
    print("  cancel() 是没用的 —— 它根本回不到 await 点。")


# ---------------------------------------------------------------
# 6. asyncio.Queue
# ---------------------------------------------------------------
async def part6_queue():
    show("6. asyncio.Queue —— 协程版生产者消费者")

    q = asyncio.Queue(maxsize=3)
    consumed = []

    async def producer():
        for i in range(6):
            await q.put(f"产品{i}")        # 队列满了会在这里等
            await asyncio.sleep(0.02)
        for _ in range(2):                 # 有两个消费者，就得放两颗毒丸
            await q.put(None)

    async def consumer(name):
        while True:
            item = await q.get()
            if item is None:
                return
            consumed.append(f"{name}:{item}")
            await asyncio.sleep(0.03)

    await asyncio.gather(producer(), consumer("C1"), consumer("C2"))
    print(f"    处理了 {len(consumed)} 项: {consumed}")
    print()
    print("  和线程队列用法几乎一样，只是 put/get 前要加 await。")
    print("  因为 await 会主动让出，所以完全不需要锁。")
    print("  这是协程相比线程最舒服的地方：并发结构清楚了，同步问题自然就少。")


async def main():
    await part1_gather_vs_as_completed()
    await part2_timeout()
    await part3_semaphore()
    await part4_task_group()
    await part5_cancel()
    await part6_queue()

    show("练习：去 99_exercises.py 做 ex14 ~ ex15")


if __name__ == "__main__":
    asyncio.run(main())
