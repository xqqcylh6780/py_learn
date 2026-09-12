# -*- coding: utf-8 -*-
"""
05 线程池 —— 实际写代码时的标准姿势
======================================

运行：  python 05_线程池.py

自己 new Thread 只适合学习和简单脚本。真写业务，用
concurrent.futures.ThreadPoolExecutor。
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


def fetch(url, delay=0.1):
    """模拟一次网络请求。"""
    time.sleep(delay)
    return f"{url} 的数据"


# ---------------------------------------------------------------
# 1. 为什么需要池
# ---------------------------------------------------------------
show("1. 每次新建线程有什么问题")

print("假设要处理 1000 个请求：")
print()
print("  做法一：来一个开一个线程")
print("    缺点：线程创建/销毁有开销；1000 个线程抢 GIL 切换成本极高；")
print("          还可能把内存吃光（每个线程默认约 8MB 栈空间）。")
print()

t0 = time.perf_counter()
ts = [threading.Thread(target=fetch, args=(f"url{i}",)) for i in range(100)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print(f"  新建 100 个线程完成 100 次请求: {time.perf_counter() - t0:.2f} 秒")

print()
print("  做法二：开一个固定大小的池，任务排队等着被复用")
print("    优点：线程数量可控、复用省开销、能拿到返回值、异常好处理")
print()

# ---------------------------------------------------------------
# 2. ThreadPoolExecutor 基本用法
# ---------------------------------------------------------------
show("2. 基本用法：submit + result")

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=10) as pool:
    futures = [pool.submit(fetch, f"url{i}") for i in range(100)]
    data = [f.result() for f in futures]
print(f"  线程池完成 100 次请求: {time.perf_counter() - t0:.2f} 秒")
print(f"  拿到 {len(data)} 条结果，第一条: {data[0]}")
print()
print("with 语句结束时自动调用 shutdown(wait=True)：")
print("  不再接收新任务，并等所有已提交的任务跑完。")
print("写成 with 就不用担心忘记关池子。")


# ---------------------------------------------------------------
# 3. Future：线程的「取货凭证」
# ---------------------------------------------------------------
show("3. Future 是什么")

with ThreadPoolExecutor(max_workers=2) as pool:
    f = pool.submit(fetch, "example.com", 0.15)

    print("  刚提交完:")
    print("    done()   =", f.done(), " <- 还没跑完")
    print("    running()=", f.running())
    print()
    print("  现在调用 result()，它会阻塞到任务完成:")
    t0 = time.perf_counter()
    value = f.result()
    print(f"    result() = {value}   （等了 {time.perf_counter() - t0:.2f} 秒）")
    print()
    print("  跑完之后:")
    print("    done()   =", f.done())
    print("    result() =", f.result(), " <- 再取一次，立刻返回（结果被缓存了）")

print()
print("Future 就是个「取货凭证」。submit 立刻返回一个 Future，")
print("真正的结果过一会儿才放进去。这跟点外卖拿到订单号是一个道理。")


# ---------------------------------------------------------------
# 4. 异常处理
# ---------------------------------------------------------------
show("4. 任务里抛异常怎么办")


def may_fail(n):
    if n == 2:
        raise ValueError(f"第 {n} 个任务故意炸了")
    return f"任务{n} 成功"


with ThreadPoolExecutor(max_workers=3) as pool:
    fs = [pool.submit(may_fail, i) for i in range(4)]
    for i, f in enumerate(fs):
        try:
            print(f"   {f.result()}")
        except ValueError as e:
            print(f"   任务{i} 抛出: {e}")
        print(f"     exception() 能看到异常对象: {type(f.exception()).__name__}")

print()
print("重点：异常不会自动往外冒，必须调用 result() 或 exception() 才拿得到。")
print("如果你 submit 了却从来不取 result，异常就被静默吞掉了 —— 这是大坑。")


# ---------------------------------------------------------------
# 5. map：按顺序批量处理
# ---------------------------------------------------------------
show("5. map —— 最简洁的批量写法")

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, [f"site{i}" for i in range(8)], [0.08] * 8))

print(f"  8 个任务并发完成: {time.perf_counter() - t0:.2f} 秒")
print("  结果顺序和输入顺序一致:", results[:3], "...")
print()
print("map 的特点：返回的顺序 = 输入的顺序，即使后面那些先跑完也一样。")
print("这很符合直觉，但如果前面的任务特别慢，你会干等着。")


# ---------------------------------------------------------------
# 6. as_completed：谁先完成先处理
# ---------------------------------------------------------------
show("6. as_completed —— 完成的顺序处理")


def fetch_slow(url, delay):
    time.sleep(delay)
    return f"{url}(耗时{delay}s)"


with ThreadPoolExecutor(max_workers=3) as pool:
    futures = [
        pool.submit(fetch_slow, "慢的", 0.25),
        pool.submit(fetch_slow, "快的", 0.05),
        pool.submit(fetch_slow, "中的", 0.12),
    ]
    print("  按提交顺序是: 慢的 / 快的 / 中的")
    print("  按完成顺序是:")
    for f in as_completed(futures):
        print("    ", f.result())

print()
print("as_completed 返回的是「已完成」的 Future，顺序不定。")
print("适合：谁先回来先处理谁（比如抓取多个源，用最先返回的那个）。")
print("map 适合：结果必须按输入顺序排列（比如批量转换文件）。")


# ---------------------------------------------------------------
# 7. 超时
# ---------------------------------------------------------------
show("7. 超时控制")

with ThreadPoolExecutor(max_workers=2) as pool:
    f = pool.submit(fetch, "慢站点", 0.5)
    try:
        f.result(timeout=0.1)
    except TimeoutError:
        print("  result(timeout=0.1) -> TimeoutError")
        print("  注意：超时只是「不再等了」，任务本身还在后台跑，不会被取消")
        print("  最终结果还是拿到了:", f.result())

print()
print("批量的话可以给 as_completed 传 timeout:")
print("    for f in as_completed(futures, timeout=1.0): ...")


# ---------------------------------------------------------------
# 8. max_workers 该设多少
# ---------------------------------------------------------------
show("8. max_workers 设多少合适")

print("IO 密集型（网络请求、读写文件）：")
print("    可以设大一些，几十到几百都行。因为线程大部分时间在等，不占 CPU。")
print("    但要考虑下游承受能力 —— 你开 500 个线程打对方接口，可能被封。")
print()
print("CPU 密集型：")
print("    设成 CPU 核数左右就够了，再多了也只是抢 GIL。")
print("    而且 CPU 密集本来就该用进程池，不是线程池。")
print()
print("当前机器 CPU 核数:", __import__("os").cpu_count())
print("默认值（3.8+）是 min(32, CPU核数 + 4)，对 IO 密集来说偏保守。")
print()
print("不确定就从小开始，边加边看 CPU 和内存，别一上来就开 1000。")


show("练习：去 99_exercises.py 做 ex8 ~ ex9")
