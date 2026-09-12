# -*- coding: utf-8 -*-
"""
12 常见陷阱 —— 踩过的坑都在这
================================

运行：  python 12_常见陷阱.py

这一节是前面 11 节的「错题本」。每个坑都给出现象、原因、解法。
"""

import asyncio
import multiprocessing
import queue
import signal
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


async def quick(x):
    await asyncio.sleep(0.01)
    return x


# ---------------------------------------------------------------
def part1_race():
    show("坑 1：共享数据不加锁 —— 结果时对时错")

    print("  现象：计数少了几千次，但重跑一次可能又是对的")
    print("  原因：counter += 1 是「读-改-写」三步，中间会被切走")
    print("  解法：with lock，或者干脆用 queue 传数据")
    print()
    print("  完整实测见 03 节。重点记住这句：")
    print("  有 GIL ≠ 线程安全。不要把某些 CPython 操作当前看起来原子，当成语言级同步保证。")


# ---------------------------------------------------------------
def part2_deadlock():
    show("坑 2：死锁 —— 程序卡住不动了")

    print("  现象：程序不报错也不结束，CPU 占用接近 0")
    print("  原因：两个线程各持一把锁，又都在等对方那把")
    print("  解法：")
    print("    1. 所有线程按同一个顺序获取多把锁")
    print("    2. 加锁时带 timeout")
    print("    3. 能用一把锁就别用两把")
    print()
    print("  排查技巧：卡住时用 py-spy dump --pid <PID>，")
    print("  它能直接打印出每个线程卡在哪一行 —— 比 print 大法高效一百倍。")


# ---------------------------------------------------------------
def part3_swallowed_exception():
    show("坑 3：线程/池里的异常被静默吞掉")

    def boom():
        raise ValueError("我在线程里炸了")

    print("  用 ThreadPoolExecutor，但不去取 result：")
    with ThreadPoolExecutor(max_workers=1) as pool:
        pool.submit(boom)
    print("    池子关了，但控制台干干净净，你根本不知道出过错")

    print()
    print("  正确姿势：一定要取 result 或 exception")
    with ThreadPoolExecutor(max_workers=1) as pool:
        f = pool.submit(boom)
        try:
            f.result()
        except ValueError as e:
            print("    这次抓到了:", e)

    print()
    print("  现象：任务明明失败了，但日志里什么都没有，结果还少了几条。")
    print("  解法：拿到 Future 就必须处理，别 submit 完就不管了。")


# ---------------------------------------------------------------
def part4_poison_pill():
    show("坑 4：毒丸数量不对 —— 消费者永远等下去")

    print("  这个坑我在写这套教程时刚踩过一次，所以放进来了。")
    print()
    print("  场景：1 个生产者、2 个消费者，队列里放 1 个 None 当收工信号")
    print("  结果：一个消费者拿到 None 走了，另一个永远等在 q.get() 上")
    print("        -> 程序挂住，不报错，CPU 也不高，非常难查")
    print()
    print("  解法：消费者有几个，就放几颗毒丸。")

    q = queue.Queue()
    for _ in range(2):                  # 两个消费者 -> 两颗毒丸
        q.put(None)
    stopped = 0
    for _ in range(2):
        if q.get() is None:
            stopped += 1
    print(f"    实测：放 {stopped} 颗毒丸，{stopped} 个消费者都能正常退出")


# ---------------------------------------------------------------
def part5_daemon():
    show("坑 5：daemon 线程 / 进程被无声掐断")

    print("  现象：日志少了最后几条，数据写了一半")
    print("  原因：daemon 线程在主线程退出时会被直接杀掉，没有收尾机会")
    print("  解法：")
    print("    - 要写数据、要提交事务的，绝对不要用 daemon")
    print("    - 主线程退出前显式 join，或者用 Event 通知它们收工")
    print()
    print("  daemon 只适合「丢了也无所谓」的后台活：心跳、监控上报。")


# ---------------------------------------------------------------
def part6_forgot_await():
    show("坑 6：协程里忘了 await")

    async def bad():
        quick(1)                        # 少了 await
        return "ok"

    import gc
    import warnings

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        asyncio.run(bad())
        gc.collect()

    print("  现象：某个请求从来没发出去，但程序不报错")
    print("  警告:", str(caught[0].message) if caught else "(没捕获到)")
    print()
    print("  最坑的是这个警告要等垃圾回收才发，可能距离出错的地方很远。")
    print("  看到 'coroutine ... was never awaited' 一定要回头查。")


# ---------------------------------------------------------------
def part7_blocking_in_async():
    show("坑 7：在协程里调用阻塞函数")

    async def heartbeat(gaps, count=8):
        last = time.perf_counter()
        for _ in range(count):
            await asyncio.sleep(0.02)
            now = time.perf_counter()
            gaps.append(now - last)
            last = now

    def blocking_call():
        time.sleep(0.2)                 # 同步阻塞函数；直接在协程里调用会卡死整个循环
        return "done"

    async def demo(use_thread):
        gaps = []
        if use_thread:
            await asyncio.gather(heartbeat(gaps), asyncio.to_thread(blocking_call))
        else:
            async def call_blocking_directly():
                return blocking_call()
            await asyncio.gather(heartbeat(gaps), call_blocking_directly())
        return max(gaps)

    gap_bad = asyncio.run(demo(use_thread=False))
    gap_good = asyncio.run(demo(use_thread=True))

    print(f"  直接调用同步阻塞函数 : 心跳最大间隔 {gap_bad:.3f} 秒  <- 被卡住了")
    print(f"  用 asyncio.to_thread : 心跳最大间隔 {gap_good:.3f} 秒  <- 正常")
    print()
    print("  症状：平时一切正常，某个慢请求一来，全站响应都变慢。")
    print("  这是异步服务最常见的性能事故，09、10 节有完整讲解。")


# ---------------------------------------------------------------
def part8_pickle():
    show("坑 8：把不能 pickle 的东西传给进程")

    print("  现象：单进程跑得好好的，一上多进程就报错")
    print("        Can't pickle <function <lambda> ...>")
    print("  原因：进程之间传数据要序列化，lambda / 嵌套函数 / 文件对象都过不去")
    print("  解法：")
    print("    - 传给进程的函数，定义在模块顶层（用普通 def）")
    print("    - 要传的对象，确保能被 pickle")
    print()
    print("  顺带一提：进程传大数据是要「复制」的。")
    print("  传一个几百 MB 的对象给子进程，光复制就能让性能崩掉。")


# ---------------------------------------------------------------
def part9_main_guard():
    show("坑 9：多进程没写 if __name__ == '__main__'")

    print("  现象：一运行就疯狂开进程，把机器卡死")
    print("  原因：Windows 用 spawn 模式，子进程会重新导入你的模块，")
    print("        如果开进程的代码在顶层，就会被反复执行")
    print("  解法：把入口代码放进 main()，然后：")
    print()
    print("        if __name__ == '__main__':")
    print("            main()")
    print()
    print(f"  当前模块里 __name__ = {__name__!r}")
    print("  主进程是 '__main__'（守卫成立），子进程是 '__mp_main__'（守卫跳过）。")


# ---------------------------------------------------------------
def part10_thread_pool_size():
    show("坑 10：线程池开太大反而更慢")

    print("  以为「开得越多越快」是新手最常见的误解。")
    print()
    print("  CPU 密集：开成核数的几倍，只会互相抢 GIL，切换开销反而拖慢。")
    print("  IO  密集：可以开大，但要看下游承受能力 ——")
    print("            你开 500 个线程打对方接口，大概率被封 IP。")
    print("            而且每个线程都有独立栈空间，线程多了内存也吃不消。")
    print()
    print("  正确做法：从一个保守值开始（IO 密集 20~50），")
    print("  压测加观察，慢慢往上调，别一上来就 1000。")


# ---------------------------------------------------------------
def part11_graceful_shutdown():
    show("坑 11：收到停止信号就立刻退出")

    stopping = threading.Event()

    def request_stop(signum, _frame):
        print(f"  收到信号 {signum}：停止接收新任务")
        stopping.set()

    # 教程不真正发送系统信号，用一次模拟调用展示状态转换。
    request_stop(getattr(signal, "SIGTERM", signal.SIGINT), None)
    assert stopping.is_set()

    print("  正确关闭顺序：停止接收 -> 通知任务 -> 等待在途工作 -> 关闭池/队列/连接。")
    print("  signal.signal(...) 只能在主线程注册；Windows 服务还要遵循服务管理器的停止协议。")
    print("  超时后是否强制终止要由应用明确决定，不能让重要写入做到一半。")


# ---------------------------------------------------------------
def part12_backpressure():
    show("坑 12：生产速度失控，没有背压")

    bounded = queue.Queue(maxsize=2)
    bounded.put_nowait("task-1")
    bounded.put_nowait("task-2")
    try:
        bounded.put_nowait("task-3")
    except queue.Full:
        print("  有界队列已满：生产者必须等待、拒绝或降级，不能无限堆积。")

    print("  无界队列在消费者变慢时会持续占用内存，并把真正故障推迟成内存事故。")
    print("  背压策略要明确：阻塞多久、是否丢弃、谁重试，以及怎样记录拒绝数量。")


# ---------------------------------------------------------------
def part13_summary():
    show("总结：排错速查表")

    rows = [
        ("程序不结束、CPU 很低", "死锁 / 消费者没收到毒丸", "py-spy dump 看每个线程卡在哪"),
        ("结果时对时错", "竞态，共享数据没加锁", "加锁，或改用队列"),
        ("某任务从来没执行", "协程忘了 await", "搜 never awaited 警告"),
        ("任务失败了但没日志", "Future 没取 result", "submit 后必须 result/exception"),
        ("全站响应变慢", "协程里调了阻塞函数", "用 to_thread 包一层"),
        ("一运行开满进程", "缺 if __name__ 守卫", "把入口放进 main()"),
        ("多进程报 pickle 错", "传了 lambda/嵌套函数", "函数提到模块顶层"),
        ("日志少了几条", "daemon 被强杀", "别用 daemon 做重要的事"),
        ("部署停止时数据损坏", "没有优雅关闭协议", "先停流量，再等待在途任务"),
        ("内存持续上涨", "生产快于消费且队列无界", "限制队列并设计背压策略"),
    ]
    print(f"  {'现象':<26}{'原因':<30}怎么查")
    print("  " + "-" * 80)
    for sym, cause, how in rows:
        print(f"  {sym:<26}{cause:<30}{how}")


def main():
    part1_race()
    part2_deadlock()
    part3_swallowed_exception()
    part4_poison_pill()
    part5_daemon()
    part6_forgot_await()
    part7_blocking_in_async()
    part8_pickle()
    part9_main_guard()
    part10_thread_pool_size()
    part11_graceful_shutdown()
    part12_backpressure()
    part13_summary()

    show("练习：去 99_exercises.py 做 ex18")


if __name__ == "__main__":
    main()
