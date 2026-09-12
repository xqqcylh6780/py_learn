# -*- coding: utf-8 -*-
"""
15 asyncio 中的异常传播、取消与超时
====================================
"""

import asyncio


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


async def fail():
    await asyncio.sleep(0)
    raise ValueError("任务失败")


async def cancellation_demo():
    async def worker():
        try:
            await asyncio.sleep(10)
        finally:
            print("worker finally: 即使取消也执行清理")

    task = asyncio.create_task(worker())
    await asyncio.sleep(0)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("调用方观察到 CancelledError")


async def main():
    show("1. await 会把任务异常传播给等待者")
    try:
        await fail()
    except ValueError as exc:
        print("捕获:", exc)

    show("2. 超时")
    try:
        async with asyncio.timeout(0.01):
            await asyncio.sleep(1)
    except TimeoutError:
        print("asyncio.timeout 超时后在上下文外表现为 TimeoutError")

    show("3. 取消不是普通失败")
    print("CancelledError 用于协作式取消。通常清理后应继续传播，不要随便吞掉。")
    await cancellation_demo()

    show("4. TaskGroup")
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fail())
            tg.create_task(fail())
    except* ValueError as eg:
        print("TaskGroup 收集到 ValueError:", len(eg.exceptions))

    show("5. create_task 后不 await/不管理，会让异常更难处理")
    print("后台任务应有明确所有者、生命周期和异常处理策略。")


if __name__ == "__main__":
    asyncio.run(main())
    print("\n练习：99_exercises.py -> ex29 ~ ex30")
