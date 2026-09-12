# -*- coding: utf-8 -*-
"""
06 进程基础 —— 真·并行，以及那个必须写的 if __name__
=======================================================

运行：  python 06_进程基础.py

进程是绕过 GIL 的官方途径。但它有几个必须知道的门槛，
其中「必须写 if __name__ == '__main__'」是最容易让人懵的一个。
"""

import multiprocessing
import os
import threading
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


def busy(n=5_000_000):
    """CPU 密集的活。"""
    total = 0
    for i in range(n):
        total += i * i % 7
    return total


def who_am_i(tag):
    return f"{tag} 跑在进程 {os.getpid()}（父进程 {os.getppid()}）"


def noop():
    """什么都不做，用来测量进程的启动开销。"""
    pass


# ---------------------------------------------------------------
# 1. Process 基本用法
# ---------------------------------------------------------------
def part1_basic():
    show("1. 开一个进程")

    print("主进程 PID:", os.getpid())
    print()

    p = multiprocessing.Process(target=who_am_i, args=("子进程",))
    p.start()
    p.join()
    print()
    print("用法和 Thread 几乎一模一样：target / args / start / join。")
    print("但 Process 没有返回值 —— 想让子进程吐数据回来，得用 07 节的队列。")


# ---------------------------------------------------------------
# 2. 为什么必须写 if __name__ == "__main__"
# ---------------------------------------------------------------
def part2_the_guard():
    show("2. 那个必须写的 if __name__ == '__main__'")

    print("这是 Windows / macOS 上写多进程最容易踩的坑。")
    print()
    print("原因：这两个系统创建新进程用的是 spawn 模式 ——")
    print("它会「重新导入一次你的模块」，然后才执行目标函数。")
    print()
    print("如果开进程的代码写在模块顶层，那么子进程一导入这个模块，")
    print("又会执行一遍开进程的代码 -> 又开一个 -> 再导入 -> 无限递归。")
    print("结果就是瞬间开出一大堆进程，把机器卡死。")
    print()
    print("解决办法就是那个守卫：")
    print("    if __name__ == '__main__':")
    print("        main()")
    print()
    print(f"  主进程里 __name__ = {__name__!r}  -> 守卫成立，会执行 main()")
    print("  子进程里 __name__ = '__mp_main__' -> 守卫不成立，直接跳过")
    print()
    print("所以你打开真多进程的代码，一定会看到这一行，现在你知道它是干嘛的了。")


# ---------------------------------------------------------------
# 3. 进程之间不共享内存
# ---------------------------------------------------------------
def part3_no_sharing():
    show("3. 进程之间不共享内存")

    shared_counter.append(1)            # 主进程先放一个
    p = multiprocessing.Process(target=child_append)
    p.start()
    p.join()

    print("  主进程的列表:", shared_counter)
    print("  子进程往里 append 了 3 次，主进程这边看到几个？")
    print()
    print("  答案：还是 1 个。因为子进程拿到的是列表的「副本」——")
    print("  它改的是自己那份，跟主进程的完全无关。")
    print()
    print("这一点和线程正相反：线程共享内存（所以才要加锁），")
    print("进程各过各的（所以不用锁，但也没法直接通信）。")


shared_counter = []


def child_append():
    for _ in range(3):
        shared_counter.append("子进程加的")


# ---------------------------------------------------------------
# 4. 实测：CPU 密集的加速
# ---------------------------------------------------------------
def part4_speedup():
    show("4. 实测：CPU 密集能快多少")

    cores = os.cpu_count() or 2
    n_workers = min(4, cores)
    print(f"  本机 CPU 核数: {cores}，下面用 {n_workers} 个进程")
    print()

    n_tasks = n_workers

    t0 = time.perf_counter()
    serial = [busy() for _ in range(n_tasks)]
    t_serial = time.perf_counter() - t0

    pool = multiprocessing.Pool(n_workers)      # 提前建好，不计入启动开销
    t0 = time.perf_counter()
    parallel = pool.map(busy, [5_000_000] * n_tasks)
    t_parallel = time.perf_counter() - t0
    pool.close()
    pool.join()

    print(f"  串行跑 {n_tasks} 次: {t_serial:.2f} 秒")
    print(f"  {n_workers} 个进程并行: {t_parallel:.2f} 秒")
    print(f"  加速比: {t_serial / t_parallel:.2f} 倍")
    print(f"  结果一致吗: {serial == parallel}")


# ---------------------------------------------------------------
# 5. 启动开销
# ---------------------------------------------------------------
def part5_overhead():
    show("5. 进程很贵，别乱开")

    N_THREADS = 20
    t0 = time.perf_counter()
    ts = [threading.Thread(target=noop) for _ in range(N_THREADS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    thread_total = time.perf_counter() - t0

    t0 = time.perf_counter()
    p = multiprocessing.Process(target=noop)
    p.start()
    p.join()
    proc_total = time.perf_counter() - t0

    print(f"  开并跑完 {N_THREADS} 个线程 : {thread_total * 1000:6.1f} 毫秒"
          f"   (平均 {thread_total / N_THREADS * 1000:.2f} 毫秒/个)")
    print(f"  开并跑完 1 个进程     : {proc_total * 1000:6.1f} 毫秒")
    print(f"  相差约 {proc_total / (thread_total / N_THREADS):,.0f} 倍")
    print()
    print("进程这么贵，是因为 spawn 模式下子进程要「重新导入一遍你的模块」。")
    print("所以进程池一旦建好就要尽量复用，别每次任务都新建一个。")
    print()
    print("结论：")
    print("  - 任务要「够大」才值得开进程。算 1 毫秒的活，开销是大头。")
    print("  - 千万别每个小任务开一个进程，一定要用进程池复用。")
    print("  - 进程池要么提前建好，要么长驻，不要每次用每次建。")
    print()
    print("顺带一提：这里如果把 target 写成 lambda，会直接报 Can't pickle 的错。")
    print("子进程是「重新导入模块再按名字找函数」，匿名函数没名字可找。")
    print("所以传进去的函数一定要定义在模块顶层 —— 07 节有实测。")


# ---------------------------------------------------------------
# 6. 进程数的甜点区
# ---------------------------------------------------------------
def part6_how_many():
    show("6. 开几个进程合适")

    cores = os.cpu_count() or 4
    print(f"  CPU 密集: {cores} 左右最合适（等于核数），多了只会互相抢 CPU")
    print("  IO  密集: 进程不是好选择 —— 用线程或协程，开销小得多")
    print()
    print("默认值: Pool() 不传参时用的是 os.cpu_count()，通常就是对的。")
    print()
    print("还有个容易忽略的点：进程之间传数据要「序列化 + 复制」。")
    print("传一个几百 MB 的 DataFrame 给子进程，光复制就能让你怀疑人生。")
    print("这种场景要么切分数据，要么改用共享内存（07 节讲）。")


def main():
    part1_basic()
    part2_the_guard()
    part3_no_sharing()
    part4_speedup()
    part5_overhead()
    part6_how_many()

    show("练习：去 99_exercises.py 做 ex10")


if __name__ == "__main__":
    main()
