# -*- coding: utf-8 -*-
"""
01 并发基础与 GIL —— 先把概念和边界搞清
==========================================

运行：  python 01_并发基础与GIL.py

这一节要建立三个判断力：
  1. 并发 ≠ 并行
  2. 任务分「CPU 密集」和「IO 密集」，选型完全取决于它
  3. GIL 决定了 Python 线程能干什么、不能干什么
"""

import multiprocessing
import threading
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 任务定义
# ---------------------------------------------------------------

def io_task(name, duration=0.25):
    """模拟 IO 等待：比如等网络响应、等磁盘读取。"""
    time.sleep(duration)
    return f"{name} 完成"


CPU_N = 6_000_000


def cpu_task(n=CPU_N):
    """模拟 CPU 计算：纯 Python 循环，不吃 IO。"""
    total = 0
    for i in range(n):
        total += i * i % 7
    return total


# ---------------------------------------------------------------
# 1. 并发 vs 并行
# ---------------------------------------------------------------
def part1_concepts():
    show("1. 并发 ≠ 并行")

    print("并发 (Concurrency)：同一时间段内「交替」推进多个任务，不要求同时")
    print("并行 (Parallelism)：同一时刻「真正同时」执行多个任务，需要多核")
    print()
    print("类比：")
    print("  并发 = 一个厨师同时照看三口锅，来回切换（其实只有一个厨师）")
    print("  并行 = 三个厨师各看一口锅（真的有三个人）")
    print()
    print("Python 里：")
    print("  协程 / 线程  -> 并发（单核来回切，靠切换省下等待时间）")
    print("  进程         -> 并行（多核同时算）")


# ---------------------------------------------------------------
# 2. IO 密集：线程完胜
# ---------------------------------------------------------------
def part2_io_bound():
    show("2. IO 密集：串行 vs 线程")

    N = 4

    t0 = time.perf_counter()
    for i in range(N):
        io_task(f"任务{i}")
    serial = time.perf_counter() - t0

    threads = [threading.Thread(target=io_task, args=(f"任务{i}",)) for i in range(N)]
    t0 = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    threaded = time.perf_counter() - t0

    print(f"  串行跑 {N} 个 0.25 秒的 IO 任务 : {serial:.2f} 秒")
    print(f"  开 {N} 个线程跑同样的事        : {threaded:.2f} 秒")
    print(f"  提速 {serial / threaded:.1f} 倍")
    print()
    print("为什么快？等待的时候线程会把执行权交出去，别的线程顶上。")
    print("线程干的是「等」，等的时候不占 CPU，所以能叠起来。")


# ---------------------------------------------------------------
# 3. CPU 密集：线程没用，进程才行
# ---------------------------------------------------------------
def part3_cpu_bound():
    show("3. CPU 密集：串行 / 线程 / 进程 三方对比")

    N = 2

    t0 = time.perf_counter()
    for _ in range(N):
        cpu_task()
    serial = time.perf_counter() - t0

    threads = [threading.Thread(target=cpu_task) for _ in range(N)]
    t0 = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    threaded = time.perf_counter() - t0

    # 进程池提前建好，模拟「复用资源」的真实用法，避免把启动开销算进来
    pool = multiprocessing.Pool(N)
    t0 = time.perf_counter()
    pool.map(cpu_task, [CPU_N] * N)
    pooled = time.perf_counter() - t0
    pool.close()
    pool.join()

    print(f"  串行算 {N} 次       : {serial:.2f} 秒   (基准)")
    print(f"  开 {N} 个线程        : {threaded:.2f} 秒   ({serial / threaded:.2f} 倍)")
    print(f"  开 {N} 个进程        : {pooled:.2f} 秒   ({serial / pooled:.2f} 倍)")
    print()
    print("看结果：")
    print("  线程基本没有提速 —— 大家排队抢 GIL，本质还是一个核在干活")
    print("  进程接近翻倍       —— 每个进程有自己的 GIL，真吃上了多核")
    print()
    print("注意进程池我是「提前建好」才计时的。如果每次现建，")
    print("Windows 上光是启动进程就要几百毫秒，小任务根本回不了本。")


# ---------------------------------------------------------------
# 4. GIL 是什么
# ---------------------------------------------------------------
def part4_gil():
    show("4. GIL 到底是什么")

    import sys

    print("GIL = Global Interpreter Lock（全局解释器锁）")
    print()
    print("在传统的、启用 GIL 的 CPython 构建中：同一解释器里通常只有一个线程能同时执行 Python 字节码。")
    print()
    print("  多线程要跑 -> 得先抢到 GIL")
    print("  抢不到     -> 只能等着")
    print("  抢到了     -> 跑一小会儿就让出来（默认 5 毫秒）")
    print()
    print("当前线程切换间隔:", sys.getswitchinterval(), "秒")
    print("活动线程数     :", threading.active_count())
    print()
    print("于是就有了这两条结论：")
    print("  CPU 密集 + 多线程 = 白忙一场，大家排队用一个核")
    print("  IO   密集 + 多线程 = 有效，因为等待时 GIL 是释放的")
    print()
    print("关键点：线程做 IO 等待时（读写文件、网络请求、sleep），")
    print("会主动释放 GIL，别的线程才能进来跑。这就是线程对 IO 有效的原因。")


# ---------------------------------------------------------------
# 5. GIL 保护了什么（它不是一个纯粹的坏事）
# ---------------------------------------------------------------
def part5_what_gil_protects():
    show("5. GIL 也不是纯负担")

    print("不要把 GIL 当成 Python 级别的线程安全保证。某些 CPython 内置操作在特定版本里看起来是原子的，")
    print()
    print("比如 list.append 在常见 CPython + GIL 构建中通常不会把列表内部结构写坏，")
    print("但这属于实现细节，不应作为跨版本、跨解释器的同步契约。")
    print()
    print("但下面这种就不行了：")
    print("    counter += 1")
    print()
    print("它其实是三步：读 -> 加 -> 写。线程可能在这三步之间被切走。")
    print("所以「有 GIL」不等于「代码自动线程安全」，03 节会实测这个坑。")


# ---------------------------------------------------------------
# 6. 绕过 GIL 的三条路
# ---------------------------------------------------------------
def part6_workarounds():
    show("6. 想真并行，怎么办")

    print("路线一：用进程（multiprocessing）")
    print("    每个进程有独立的解释器和 GIL，能真正吃满多核。")
    print("    代价：启动慢、内存大、数据要靠序列化传递。")
    print()
    print("路线二：用 C 扩展释放 GIL")
    print("    numpy、Pillow、lxml 这些库在算的时候会把 GIL 放掉。")
    print("    所以用 numpy 做矩阵运算时，多线程是真的有效的。")
    print()
    print("路线三：使用 free-threaded CPython 构建（如果你的 Python 版本、依赖和部署环境都支持）")
    print("    这会改变传统 GIL 下的线程行为；是否适合生产要按当前版本和依赖兼容性评估。")
    print()
    print("补充：IO 密集根本不用绕 —— 线程和协程就够了。")


# ---------------------------------------------------------------
# 7. 怎么判断我的任务属于哪一类
# ---------------------------------------------------------------
def part7_how_to_judge():
    show("7. 选型前先问自己一句话")

    print("「我的程序大部分时间花在等，还是花在算？」")
    print()
    print("  等（网络/磁盘/数据库/用户输入） -> IO 密集   -> 线程 或 协程")
    print("  算（循环/加密/图像/大数据处理） -> CPU 密集  -> 进程")
    print()
    print("实测技巧：跑一遍代码，看 CPU 占用率。")
    print("  CPU 长期很低、线程大多在等待 -> 更像 IO 密集")
    print("  一个或多个核心长期跑满       -> 更像 CPU 密集")
    print()
    print("拿不准就用 cProfile 看时间花在哪，别凭感觉猜。")


def main():
    part1_concepts()
    part2_io_bound()
    part3_cpu_bound()
    part4_gil()
    part5_what_gil_protects()
    part6_workarounds()
    part7_how_to_judge()

    show("练习：去 99_exercises.py 做 ex1 ~ ex2")


if __name__ == "__main__":
    main()
