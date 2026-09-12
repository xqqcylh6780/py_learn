# -*- coding: utf-8 -*-
"""24 线程 / asyncio 调试：异常可能发生在另一个执行单元。"""
import asyncio
import threading


def thread_worker():
    try:
        raise RuntimeError("thread failed")
    except RuntimeError as e:
        print("线程内部明确处理:", e)


t = threading.Thread(target=thread_worker)
t.start(); t.join()

async def child():
    await asyncio.sleep(0)
    raise ValueError("task failed")

async def main():
    task = asyncio.create_task(child(), name="demo-child")
    print("task name:", task.get_name())
    try:
        await task
    except ValueError as e:
        print("await 时收到 Task 异常:", e)

asyncio.run(main())

print("\n调试 asyncio 时可以在开发环境使用 asyncio.run(..., debug=True) 或 PYTHONASYNCIODEBUG=1。")
print("不要创建 Task 后完全丢掉引用并忽略结果，否则异常可能只在事件循环警告里出现。")
