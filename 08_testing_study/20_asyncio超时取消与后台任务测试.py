# -*- coding: utf-8 -*-
"""
20 asyncio 超时、取消与后台任务测试
=======================

直接运行本文件即可观察示例。
"""
import asyncio

async def slow():
    await asyncio.sleep(10)

async def main():
    try:
        async with asyncio.timeout(0.01):
            await slow()
    except TimeoutError:
        print("超时被正确观察到")

    started = asyncio.Event()
    async def worker():
        started.set()
        try:
            await asyncio.sleep(10)
        finally:
            print("worker cleanup")

    task = asyncio.create_task(worker())
    await started.wait()
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("取消被正确传播")

asyncio.run(main())

# 异步测试尤其要清理自己创建的后台 task，
# 否则容易出现 “Task was destroyed but it is pending!”。
