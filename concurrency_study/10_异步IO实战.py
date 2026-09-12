# -*- coding: utf-8 -*-
"""
10 异步IO实战 —— 以及协程最大的那个坑
========================================

运行：  python 10_异步IO实战.py

asyncio 只擅长一件事：等待。一旦你在协程里干「不等待的重活」，
整个事件循环都会被卡住 —— 这是新手最常踩、也最难查的坑。
"""

import asyncio
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


async def cpu_async(n=3_000_000):
    """一个「假装异步」的 CPU 密集任务：里面没有任何 await。"""
    total = 0
    for i in range(n):
        total += i * i % 7
    return total


# ---------------------------------------------------------------
# 1. asyncio 加速不了 CPU
# ---------------------------------------------------------------
async def part1_cpu_no_speedup():
    show("1. asyncio 对 CPU 密集毫无帮助")

    t0 = time.perf_counter()
    await cpu_async()
    await cpu_async()
    serial = time.perf_counter() - t0

    t0 = time.perf_counter()
    await asyncio.gather(cpu_async(), cpu_async())
    gathered = time.perf_counter() - t0

    print(f"    串行两次 await : {serial:.2f} 秒")
    print(f"    gather 并发    : {gathered:.2f} 秒")
    print(f"    加速比         : {serial / gathered:.2f} 倍")
    print()
    print("  完全没有加速。原因很直白：协程是「单线程」的并发，")
    print("  它省下的是「等待时间」，而 CPU 密集里根本没有等待。")
    print()
    print("  记住这个分工：")
    print("    asyncio -> 省下等待（IO 密集）")
    print("    多进程  -> 真吃多核（CPU 密集）")


# ---------------------------------------------------------------
# 2. 更严重的问题：卡死事件循环
# ---------------------------------------------------------------
async def part2_blocking_loop():
    show("2. 后果比「没加速」严重得多：整个循环被卡住")

    async def heartbeat(record, count=12, interval=0.02):
        last = time.perf_counter()
        for _ in range(count):
            await asyncio.sleep(interval)
            now = time.perf_counter()
            record.append(now - last)
            last = now

    # 情况 A：只有心跳
    gaps_a = []
    await heartbeat(gaps_a)
    print(f"  A. 只有心跳任务（间隔 0.02 秒）")
    print(f"     实际间隔最大 {max(gaps_a):.3f} 秒，平均 {sum(gaps_a) / len(gaps_a):.3f} 秒")
    print("     很稳定 —— 事件循环运转正常。")

    # 情况 B：心跳 + 一个阻塞任务
    print()
    print("  B. 心跳 + 一个「没有 await 的耗时计算」")
    gaps_b = []
    t0 = time.perf_counter()
    await asyncio.gather(heartbeat(gaps_b, count=12, interval=0.02), cpu_async(3_000_000))
    print(f"     实际间隔最大 {max(gaps_b):.3f} 秒，平均 {sum(gaps_b) / len(gaps_b):.3f} 秒")
    print(f"     总共 {len(gaps_b)} 次心跳里有 {sum(1 for g in gaps_b if g > 0.1)} 次被卡住了")
    print()
    print("  看到差距了吗：心跳本该每 0.02 秒跳一次，结果有一次被卡了上百毫秒。")
    print()
    print("  为什么？事件循环是单线程的。cpu_async 里从头到尾没有 await，")
    print("  它就一直占着这个线程，循环根本没机会去推进别的协程。")
    print()
    print("  在真实项目里的表现：")
    print("    - 一个接口做大数据处理 -> 整个服务的所有请求都卡住")
    print("    - 用了同步的 requests / time.sleep / 读大文件 -> 同上")
    print("    - 现象是「平时好好的，某个请求一来全站变慢」")


# ---------------------------------------------------------------
# 3. 解法：丢到线程里去跑
# ---------------------------------------------------------------
async def part3_to_thread():
    show("3. 解法：asyncio.to_thread")

    def blocking_io(name, seconds):
        """一个典型的同步阻塞函数：老的库大多长这样。"""
        time.sleep(seconds)
        return f"{name} 完成"

    async def heartbeat(record, count=10, interval=0.02):
        last = time.perf_counter()
        for _ in range(count):
            await asyncio.sleep(interval)
            now = time.perf_counter()
            record.append(now - last)
            last = now

    print("  错误做法：直接 await 一个同步阻塞函数")
    t0 = time.perf_counter()
    for i in range(4):
        result = blocking_io(f"任务{i}", 0.1)
    print(f"    串行调用 4 个 0.1 秒的阻塞函数: {time.perf_counter() - t0:.2f} 秒")

    print()
    print("  正确做法：用 asyncio.to_thread 丢到线程池")
    gaps = []
    t0 = time.perf_counter()
    results = await asyncio.gather(
        heartbeat(gaps),
        *[asyncio.to_thread(blocking_io, f"任务{i}", 0.1) for i in range(4)],
    )
    elapsed = time.perf_counter() - t0

    print(f"    4 个任务并发完成: {elapsed:.2f} 秒")
    print(f"    结果: {[r for r in results if r]}")
    print(f"    心跳最大间隔: {max(gaps):.3f} 秒  <- 没有被卡住")
    print()
    print("  asyncio.to_thread 做的事：把同步函数扔进一个后台线程池，")
    print("  然后 await 它的结果。事件循环该干嘛干嘛。")
    print("  它是 Python 3.9+ 的新写法，等价于以前的 loop.run_in_executor。")


async def part4_run_in_executor():
    show("4. 老写法：run_in_executor")

    def blocking(n):
        return sum(i * i for i in range(n))

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking, 1_000_000)
    print("    run_in_executor 结果:", result)
    print()
    print("  第一个参数传 None 表示用默认线程池；")
    print("  也可以传自己的 ThreadPoolExecutor 来控制线程数。")
    print()
    print("  现在直接用 asyncio.to_thread 更简洁，除非你要精细控制线程池。")


# ---------------------------------------------------------------
# 5. 实战：带重试和限流的异步调用
# ---------------------------------------------------------------
async def part5_real_world():
    show("5. 实战：一个还算像样的异步调用封装")

    call_count = {}

    async def unreliable_api(name, fail_times=2):
        """模拟一个会失败的接口。"""
        call_count[name] = call_count.get(name, 0) + 1
        await asyncio.sleep(0.03)
        if call_count[name] <= fail_times:
            raise ConnectionError(f"{name} 第 {call_count[name]} 次失败")
        return f"{name} 的数据"

    async def with_retry(coro_factory, retries=3, base_delay=0.02):
        last_error = None
        for attempt in range(retries):
            try:
                return await coro_factory()
            except (ConnectionError, asyncio.TimeoutError) as e:
                last_error = e
                await asyncio.sleep(base_delay * (2 ** attempt))   # 指数退避
        raise last_error

    sem = asyncio.Semaphore(3)

    async def guarded(name):
        async with sem:                    # 限流
            async with asyncio.timeout(1.0):   # 整体超时
                return await with_retry(lambda: unreliable_api(name))   # 重试

    t0 = time.perf_counter()
    results = await asyncio.gather(*[guarded(f"接口{i}") for i in range(5)])
    print(f"    5 个接口都拿到了数据: {results}")
    print(f"    总耗时 {time.perf_counter() - t0:.2f} 秒")
    print(f"    调用次数 {call_count}")
    print()
    print("  这三样是真实项目的标配：")
    print("    限流   防止把对方打挂")
    print("    超时   防止一个慢请求拖垮全局")
    print("    重试   应对偶发的网络抖动（记得用指数退避，别死命重试）")


# ---------------------------------------------------------------
# 6. 有哪些异步库
# ---------------------------------------------------------------
async def part6_libraries():
    show("6. 生态：哪些库是异步的")

    rows = [
        ("HTTP 客户端", "aiohttp / httpx", "requests（同步）"),
        ("数据库", "asyncpg / aiosqlite / SQLAlchemy 2.0 async", "psycopg2 / sqlite3"),
        ("Redis", "redis-py 的 asyncio 版", "redis-py 同步版"),
        ("Web 框架", "FastAPI / Starlette / aiohttp", "Flask / Django（同步视图）"),
        ("消息队列", "aio-pika / aiokafka", "pika / kafka-python"),
        ("文件读写", "aiofiles", "内置 open()"),
    ]
    print(f"    {'用途':<14}{'异步选择':<42}同步对照")
    print("    " + "-" * 72)
    for use, async_lib, sync_lib in rows:
        print(f"    {use:<14}{async_lib:<42}{sync_lib}")

    print()
    print("  怎么判断一个库是不是异步的？看它的函数是不是 async def、")
    print("  用不用 await 调用。requests 就是典型的同步库，")
    print("  在协程里直接调它会卡住事件循环，必须用 to_thread 包一层。")


async def main():
    await part1_cpu_no_speedup()
    await part2_blocking_loop()
    await part3_to_thread()
    await part4_run_in_executor()
    await part5_real_world()
    await part6_libraries()

    show("练习：去 99_exercises.py 做 ex16")


if __name__ == "__main__":
    asyncio.run(main())
