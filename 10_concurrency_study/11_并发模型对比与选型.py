# -*- coding: utf-8 -*-
"""
11 并发模型对比与选型 —— 到底该用哪个
========================================

运行：  python 11_并发模型对比与选型.py

前面十节把三种模型都过了一遍。这一节只回答一个问题：
拿到一个真实需求，我该选哪个？
"""

import asyncio
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


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
        ("协程 asyncio", "并发", "是", "视共享状态而定", "极低", "高并发 IO"),
    ]
    print(f"  {'模型':<22}{'类型':<8}{'共享内存':<10}{'需要锁':<14}{'开销':<8}擅长")
    print("  " + "-" * 78)
    for name, kind, shared, lock, cost, good in rows:
        print(f"  {name:<22}{kind:<8}{shared:<10}{lock:<14}{cost:<8}{good}")

    print()
    print("  几点补充说明：")
    print("    - 线程「需要锁」那一栏：因为共享内存，只要涉及写就得加锁")
    print("    - 协程共享可变状态时仍可能需要 asyncio.Lock 等同步手段；尤其是读写之间存在 await 时")
    print("    - 进程的锁是另一回事：它靠队列/共享内存的锁，不是 threading.Lock")


# ---------------------------------------------------------------
# 2. 把需求转换为选择条件
# ---------------------------------------------------------------
def choose_model(task_kind, library_style, needs_parallel_python=False):
    """给出起点方案；实际项目仍要用目标负载验证。"""
    if needs_parallel_python or task_kind == "cpu":
        return "processes"
    if library_style == "async":
        return "asyncio"
    return "threads"


def part2_decision():
    show("2. 从任务性质和依赖接口开始选择")

    scenarios = [
        ("同步 HTTP 客户端", "io", "sync", False),
        ("异步数据库驱动", "io", "async", False),
        ("纯 Python 图像计算", "cpu", "sync", True),
    ]
    for name, task_kind, library_style, parallel in scenarios:
        model = choose_model(task_kind, library_style, parallel)
        print(f"  {name:<20} -> {model}")

    print()
    print("  并发数量不是固定分界线。文件描述符、内存、下游限流、任务时长都会改变选择。")
    print("  先用最简单的可行模型，再用真实负载测吞吐、尾延迟和资源占用。")


# ---------------------------------------------------------------
# 3. 运行约束
# ---------------------------------------------------------------
def part3_constraints():
    show("3. 模型选定后仍要回答的运行问题")

    for question in [
        "任务怎样取消，超时后底层工作是否仍在运行？",
        "输入能否序列化，传输成本会不会淹没计算收益？",
        "谁限制并发，怎样避免压垮数据库或远端接口？",
        "异常在哪里汇总，后台任务失败是否可见？",
        "关闭时怎样停止接收、等待在途任务并释放资源？",
    ]:
        print("  -", question)

    print("\n  选型只决定执行模型；背压、超时、错误传播和关闭协议决定系统能否稳定运行。")


# ---------------------------------------------------------------
# 5. 混合使用
# ---------------------------------------------------------------
def part5_hybrid():
    show("5. 混合使用：协程调度 + 线程池干重活")

    print("  真实场景：一个异步服务，偶尔要跑 CPU 密集的任务。")
    print("  做法：协程负责并发调度；同步阻塞 IO 可丢线程池，真正 CPU 密集计算通常丢进程池。")
    print()

    async def handle_request(name):
        # 第一步：异步 IO（等接口）
        await asyncio.sleep(0.05)
        data = f"{name} 的数据"

        # 第二步：这里只演示把一小段同步计算移出事件循环；线程池能避免卡 loop，但不会绕过传统 GIL 获得纯 Python CPU 并行
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
    print("  注意：这里用线程池的目的只是避免阻塞事件循环，不是让纯 Python CPU 计算并行。")
    print("  真正重的 CPU 任务通常应使用 ProcessPoolExecutor；小任务则要权衡进程调度/序列化开销。")
    print()
    print("  真实的分工长这样：")
    print("    asyncio       管网络、管调度、管超时重试")
    print("    to_thread     接住同步库和老代码")
    print("    ProcessPool   接住真正吃 CPU 的大计算")


def main():
    part1_table()
    part2_decision()
    part3_constraints()
    part5_hybrid()

    show("练习：去 99_exercises.py 做 ex17")


if __name__ == "__main__":
    main()
