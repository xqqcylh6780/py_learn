# -*- coding: utf-8 -*-
"""
11 并发模型对比与选型 —— 到底该用哪个
========================================

运行：  python 11_并发模型对比与选型.py

前面十节把三种模型都过了一遍。这一节只回答一个问题：
拿到一个真实需求，我该选哪个？
"""

import asyncio
import multiprocessing
import os
import time
from concurrent.futures import ThreadPoolExecutor


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---- 三种模型各自的任务实现 ----

def io_sync(name, seconds=0.1):
    time.sleep(seconds)
    return name


async def io_async(name, seconds=0.1):
    await asyncio.sleep(seconds)
    return name


def cpu_worker(n):
    total = 0
    for i in range(n):
        total += i * i % 7
    return total


# ---------------------------------------------------------------
# 1. 总览
# ---------------------------------------------------------------
def part1_table():
    show("1. 三种模型总览")

    rows = [
        ("线程 threading", "并发", "是", "是（有 GIL）", "中", "IO 密集"),
        ("进程 multiprocessing", "并行", "否", "否", "高", "CPU 密集"),
        ("协程 asyncio", "并发", "是", "否", "极低", "高并发 IO"),
    ]
    print(f"  {'模型':<22}{'类型':<8}{'共享内存':<10}{'需要锁':<14}{'开销':<8}擅长")
    print("  " + "-" * 78)
    for name, kind, shared, lock, cost, good in rows:
        print(f"  {name:<22}{kind:<8}{shared:<10}{lock:<14}{cost:<8}{good}")

    print()
    print("  几点补充说明：")
    print("    - 线程「需要锁」那一栏：因为共享内存，只要涉及写就得加锁")
    print("    - 协程不需要锁：同一时刻只有一个协程在跑，切换点都是你自己写的 await")
    print("    - 进程的锁是另一回事：它靠队列/共享内存的锁，不是 threading.Lock")


# ---------------------------------------------------------------
# 2. IO 密集实测
# ---------------------------------------------------------------
def part2_io_compare():
    show("2. IO 密集：三种写法实测（8 个任务，每个 0.1 秒）")

    N = 8

    t0 = time.perf_counter()
    for i in range(N):
        io_sync(f"t{i}")
    t_sync = time.perf_counter() - t0

    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=N) as pool:
        list(pool.map(io_sync, [f"t{i}" for i in range(N)]))
    t_thread = time.perf_counter() - t0

    async def run_async():
        return await asyncio.gather(*[io_async(f"t{i}") for i in range(N)])

    t0 = time.perf_counter()
    asyncio.run(run_async())
    t_async = time.perf_counter() - t0

    print(f"  串行         : {t_sync:.2f} 秒   (基准)")
    print(f"  线程池       : {t_thread:.2f} 秒   ({t_sync / t_thread:.1f} 倍)")
    print(f"  asyncio      : {t_async:.2f} 秒   ({t_sync / t_async:.1f} 倍)")
    print()
    print("  三者都快很多。选哪个？")
    print("    - 任务数量少（几十个以内）、代码已经写好了 -> 线程池，改起来最省事")
    print("    - 要开几千上万个（爬虫、网关）        -> asyncio，线程开不了那么多")
    print("    - 依赖的库只有同步版本                -> 线程池")


# ---------------------------------------------------------------
# 3. CPU 密集实测
# ---------------------------------------------------------------
def part3_cpu_compare():
    show("3. CPU 密集：只有进程有效")

    N = 4
    WORK = 4_000_000

    t0 = time.perf_counter()
    serial_results = [cpu_worker(WORK) for _ in range(N)]
    t_serial = time.perf_counter() - t0

    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=N) as pool:
        thread_results = list(pool.map(cpu_worker, [WORK] * N))
    t_thread = time.perf_counter() - t0

    pool = multiprocessing.Pool(N)
    t0 = time.perf_counter()
    proc_results = pool.map(cpu_worker, [WORK] * N)
    t_proc = time.perf_counter() - t0
    pool.close()
    pool.join()

    print(f"  串行         : {t_serial:.2f} 秒   (基准)")
    print(f"  线程池       : {t_thread:.2f} 秒   ({t_serial / t_thread:.2f} 倍)  <- 白忙")
    print(f"  进程池       : {t_proc:.2f} 秒   ({t_serial / t_proc:.2f} 倍)")
    print(f"  结果一致吗   : {serial_results == thread_results == proc_results}")
    print()
    print("  线程池这一栏基本在 1.0 附近晃 —— 这就是 GIL 的代价。")
    print("  asyncio 更没用，连测都不用测：它是单线程的。")


# ---------------------------------------------------------------
# 4. 决策流程
# ---------------------------------------------------------------
def part4_decision():
    show("4. 拿到需求，按这个顺序问自己")

    steps = [
        "第 1 问：任务是「等」为主还是「算」为主？",
        "       算为主（CPU 密集） -> 直接上「进程池」，后面的都不用问了",
        "       等为主（IO 密集）   -> 继续第 2 问",
        "",
        "第 2 问：并发量大概多大？",
        "       几十个以内          -> 线程池，最简单",
        "       几百以上            -> asyncio",
        "",
        "第 3 问：依赖的库是同步还是异步？",
        "       有成熟的异步库       -> asyncio",
        "       只有同步库           -> 线程池（或在协程里用 to_thread 包一层）",
        "",
        "第 4 问：有没有需要共享的可变状态？",
        "       有                   -> 优先用队列传，别用共享变量加锁",
        "       没有                 -> 随便选，这时候选你团队最熟的",
    ]
    for line in steps:
        print("  " + line)

    print()
    print("  一个反过来的建议：如果三种都能用，就选最简单的那个。")
    print("  并发代码的调试成本很高，别为了「技术上更优雅」给自己挖坑。")


# ---------------------------------------------------------------
# 5. 混合使用
# ---------------------------------------------------------------
def part5_hybrid():
    show("5. 混合使用：协程调度 + 线程池干重活")

    print("  真实场景：一个异步服务，偶尔要跑 CPU 密集的任务。")
    print("  做法：协程负责并发调度，重活丢给线程池/进程池。")
    print()

    async def handle_request(name):
        # 第一步：异步 IO（等接口）
        await asyncio.sleep(0.05)
        data = f"{name} 的数据"

        # 第二步：CPU 密集的重活，丢到线程池，不卡事件循环
        loop = asyncio.get_running_loop()
        processed = await loop.run_in_executor(None, cpu_worker, 500_000)

        return f"{data} -> 计算结果 {processed}"

    async def main_async():
        t0 = time.perf_counter()
        results = await asyncio.gather(*[handle_request(f"请求{i}") for i in range(6)])
        return results, time.perf_counter() - t0

    results, elapsed = asyncio.run(main_async())
    print(f"    处理了 {len(results)} 个请求，耗时 {elapsed:.2f} 秒")
    print(f"    第一个结果: {results[0]}")
    print()
    print("  注意：这里用的是线程池不是进程池。因为任务是「每个都很小」，")
    print("  开进程的 60 毫秒开销比计算本身还贵。任务大才换进程池。")
    print()
    print("  真实的分工长这样：")
    print("    asyncio       管网络、管调度、管超时重试")
    print("    to_thread     接住同步库和老代码")
    print("    ProcessPool   接住真正吃 CPU 的大计算")


def main():
    part1_table()
    part2_io_compare()
    part3_cpu_compare()
    part4_decision()
    part5_hybrid()

    show("练习：去 99_exercises.py 做 ex17")


if __name__ == "__main__":
    main()
