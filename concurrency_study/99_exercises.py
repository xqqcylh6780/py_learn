# -*- coding: utf-8 -*-
"""
并发编程练习册 —— 18 道题，自动判分
======================================

运行：  python 99_exercises.py

一开始全是 [FAIL] 是正常的，那就是待办清单。
卡住了翻到最底下的「参考答案」，建议先自己想 5 分钟。

注意：涉及多进程的题目要求函数定义在模块顶层，
这是 Windows spawn 模式的硬性要求（12 节坑 8）。
"""

import asyncio
import multiprocessing
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

_checks = []


def check(fn):
    _checks.append(fn)
    return fn


# ---------------------------------------------------------------
# 给多进程题目准备的模块级函数
# 它们必须定义在顶层，否则无法被 pickle 送进子进程
# ---------------------------------------------------------------

def _cpu_worker(n):
    total = 0
    for i in range(n):
        total += i * i % 7
    return total


def _mp_sender(q):
    for i in range(3):
        q.put(i)


# =================================================================
# 01 并发基础与 GIL
# =================================================================

@check
def ex1_choose_model():
    """给 4 个场景各选一个模型，填进 chose 列表。

    可选值："asyncio" / "threading" / "multiprocessing" / "to_thread"

    场景：
      0. 要同时下载 5000 个网页
      1. 要给 10 万张图片做纯计算（哈希、缩放）
      2. 并发调用 30 个接口，但手上只有同步的 requests 库
      3. 在异步服务里，要调用一个同步的旧库
    """
    chose = [None, None, None, None]        # TODO
    expected = ["asyncio", "multiprocessing", "threading", "to_thread"]
    assert chose == expected, f"实际填的是 {chose}"


@check
def ex2_thread_pool_io():
    """用线程池并发跑 5 个 IO 任务，总耗时要明显低于串行。"""

    def io_job(i):
        time.sleep(0.1)
        return i * 2

    start = time.perf_counter()
    results = None                          # TODO
    elapsed = time.perf_counter() - start

    assert results is not None, "还没开始写"
    assert sorted(results) == [0, 2, 4, 6, 8], f"结果不对: {results}"
    assert elapsed < 0.3, f"耗时 {elapsed:.2f} 秒，看起来是串行跑的"


# =================================================================
# 02 线程基础
# =================================================================

@check
def ex3_threads_and_join():
    """开 4 个线程，每个等 0.05 秒后把自己的编号记下来，并等它们全部结束。"""
    collected = []
    lock = threading.Lock()

    def worker(n):
        time.sleep(0.05)
        with lock:
            collected.append(n)

    # TODO: 开 4 个线程跑 worker(0..3)，并确保主线程等它们全部跑完

    assert sorted(collected) == [0, 1, 2, 3], \
        f"只收集到 {sorted(collected)} —— 是不是没 join 就往下走了？"


@check
def ex4_event():
    """用 Event 让 worker 线程一直等到主线程发信号。"""
    gate = threading.Event()
    log = []

    def worker():
        gate.wait()
        log.append("被唤醒了")

    t = threading.Thread(target=worker, daemon=True)   # daemon 防止卡住判分器
    t.start()
    time.sleep(0.05)

    assert log == [], "还没发信号就醒了，说明门根本没关上"

    # TODO: 发出信号

    t.join(timeout=1.0)
    assert log == ["被唤醒了"], "worker 没被唤醒，信号发出去了吗？"


# =================================================================
# 03 线程同步
# =================================================================

@check
def ex5_fix_race():
    """下面这段有竞态，用锁把它修好，让结果一分不差。"""
    counter = 0
    lock = threading.Lock()

    def add():
        nonlocal counter
        for _ in range(20_000):
            tmp = counter
            sum(range(200))         # 放大竞态窗口，别删这行
            counter = tmp + 1

    threads = [threading.Thread(target=add) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert counter == 80_000, f"实际 {counter}，丢了 {80_000 - counter} 次 —— 加上锁"


@check
def ex6_semaphore():
    """用 Semaphore 保证同一时刻最多只有 3 个任务在跑。"""
    sem = threading.Semaphore(3)
    state = {"active": 0, "peak": 0}
    lock = threading.Lock()

    def task(i):
        # TODO: 用 sem 把下面的逻辑包起来
        with lock:
            state["active"] += 1
            state["peak"] = max(state["peak"], state["active"])
        time.sleep(0.05)
        with lock:
            state["active"] -= 1

    threads = [threading.Thread(target=task, args=(i,)) for i in range(9)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert state["peak"] <= 3, f"峰值并发 {state['peak']}，超过限制了"
    assert state["peak"] >= 2, f"峰值只有 {state['peak']}，看起来根本没并起来"


# =================================================================
# 04 队列
# =================================================================

@check
def ex7_producer_consumer():
    """1 个生产者、2 个消费者，用毒丸让两个消费者都能退出。

    小心：毒丸的数量必须等于消费者的数量。
    """
    q = queue.Queue()
    consumed = []
    lock = threading.Lock()

    def producer():
        for i in range(6):
            q.put(f"item{i}")

    def consumer():
        while True:
            item = q.get()
            if item is None:
                return
            with lock:
                consumed.append(item)

    pt = threading.Thread(target=producer, daemon=True)
    consumers = [threading.Thread(target=consumer, daemon=True) for _ in range(2)]

    pt.start()
    pt.join()
    for c in consumers:
        c.start()

    # TODO: 放毒丸，让两个消费者都能退出

    for c in consumers:
        c.join(timeout=1.0)
        assert not c.is_alive(), "还有消费者卡在 get() 上 —— 毒丸数量对吗？"

    assert sorted(consumed) == [f"item{i}" for i in range(6)], f"实际 {sorted(consumed)}"


# =================================================================
# 05 线程池
# =================================================================

@check
def ex8_thread_pool():
    """用线程池跑 6 个任务，拿到按输入顺序排列的结果。"""

    def job(i):
        time.sleep(0.05)
        return i ** 2

    results = None                          # TODO

    assert results is not None, "还没开始写"
    assert results == [0, 1, 4, 9, 16, 25], f"实际 {results}，顺序也要对"


@check
def ex9_future_exception():
    """任务里有异常，把它们收集到 errors 列表里。"""

    def job(i):
        if i == 2:
            raise ValueError("第 2 个坏了")
        return i

    errors = []
    # TODO: 用线程池跑 range(4)，把抛出的异常收集进 errors

    assert len(errors) == 1, f"应该收集到 1 个异常，实际 {len(errors)}"
    assert "第 2 个坏了" in str(errors[0]), f"异常内容不对: {errors[0]}"


# =================================================================
# 06 进程基础
# =================================================================

@check
def ex10_process_pool():
    """用进程池并行算 4 次，验证结果正确且有加速。"""
    WORK = 8_000_000

    t0 = time.perf_counter()
    serial = [_cpu_worker(WORK) for _ in range(4)]
    t_serial = time.perf_counter() - t0

    t0 = time.perf_counter()
    parallel = None                         # TODO
    t_parallel = time.perf_counter() - t0

    assert parallel is not None, "还没开始写"
    assert parallel == serial, "结果和串行不一致"
    assert t_parallel < t_serial * 0.85, \
        f"没看到并行效果：串行 {t_serial:.2f} 秒，并行 {t_parallel:.2f} 秒"


# =================================================================
# 07 进程间通信
# =================================================================

@check
def ex11_process_queue():
    """子进程往队列里放了 3 个数，把它们取回主进程。"""
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=_mp_sender, args=(q,))
    p.start()
    p.join()

    received = []
    # TODO: 从 q 里把 3 个数取出来放进 received

    assert received == [0, 1, 2], f"实际 {received}"


# =================================================================
# 08 协程基础
# =================================================================

@check
def ex12_asyncio_gather():
    """用 gather 并发跑 4 个协程。"""

    async def job(i):
        await asyncio.sleep(0.1)
        return i * 10

    async def run():
        return None                         # TODO

    start = time.perf_counter()
    results = asyncio.run(run())
    elapsed = time.perf_counter() - start

    assert results is not None, "还没开始写"
    assert results == [0, 10, 20, 30], f"实际 {results}"
    assert elapsed < 0.25, f"耗时 {elapsed:.2f} 秒，看起来是串行 await 的"


@check
def ex13_make_it_concurrent():
    """下面这段是串行的，改成并发，让它快 3 倍。"""

    async def job():
        await asyncio.sleep(0.1)

    async def run():
        await job()
        await job()
        await job()
        # TODO: 改成并发

    t0 = time.perf_counter()
    asyncio.run(run())
    elapsed = time.perf_counter() - t0

    assert elapsed < 0.2, f"耗时 {elapsed:.2f} 秒，还是串行的"


# =================================================================
# 09 asyncio 并发控制
# =================================================================

@check
def ex14_async_semaphore():
    """用 asyncio.Semaphore 限制同一时刻最多 2 个协程在跑。"""
    sem = asyncio.Semaphore(2)
    state = {"active": 0, "peak": 0}

    async def job():
        # TODO: 用 sem 限制
        state["active"] += 1
        state["peak"] = max(state["peak"], state["active"])
        await asyncio.sleep(0.05)
        state["active"] -= 1

    async def run():
        await asyncio.gather(*[job() for _ in range(8)])

    asyncio.run(run())

    assert state["peak"] <= 2, f"峰值 {state['peak']}，超过限制了"
    assert state["peak"] == 2, f"峰值只有 {state['peak']}，压根没并起来"


@check
def ex15_timeout():
    """给这个慢任务加 0.1 秒超时，超时就返回字符串 "timeout"。"""

    async def slow():
        await asyncio.sleep(1.0)
        return "done"

    async def run():
        return None                         # TODO

    t0 = time.perf_counter()
    result = asyncio.run(run())
    elapsed = time.perf_counter() - t0

    assert result == "timeout", f"实际返回 {result!r}"
    assert elapsed < 0.5, f"等了 {elapsed:.2f} 秒，超时没生效"


# =================================================================
# 10 异步 IO 实战
# =================================================================

@check
def ex16_to_thread():
    """把阻塞函数丢到线程里跑，别卡住事件循环。"""

    def blocking():
        time.sleep(0.2)
        return "阻塞任务完成"

    async def run():
        gaps = []

        async def heartbeat():
            last = time.perf_counter()
            for _ in range(10):
                await asyncio.sleep(0.02)
                now = time.perf_counter()
                gaps.append(now - last)
                last = now

        # TODO: 并发跑 heartbeat 和 blocking（后者要用 to_thread 包一层）
        result = None
        return result, gaps

    result, gaps = asyncio.run(run())

    assert result == "阻塞任务完成", f"实际 {result!r}"
    assert max(gaps) < 0.1, \
        f"心跳被卡了 {max(gaps):.2f} 秒 —— 是不是直接 await 阻塞函数了？"


# =================================================================
# 11 / 12 选型与排错
# =================================================================

@check
def ex17_spot_the_bug():
    """下面 4 段代码各有什么问题？把编号填进 answers。

    可选值："race" / "blocking" / "guard" / "swallowed"

      A. 两个线程对同一个全局计数器做 counter += 1，没有任何同步措施
      B. async def 里调用了 time.sleep(1)
      C. 模块顶层直接写 p = Process(...); p.start()，没有 main 守卫
      D. 线程池 submit 之后，从来不调用 result()
    """
    answers = [None, None, None, None]      # TODO
    expected = ["race", "blocking", "guard", "swallowed"]
    assert answers == expected, f"实际填的是 {answers}"


@check
def ex18_capstone():
    """综合题：并发处理 10 个任务，把成功和失败分别收集起来。"""

    def task(i):
        time.sleep(0.02)
        if i % 4 == 3:
            raise RuntimeError(f"任务{i}失败")
        return i

    successes = []
    failures = []

    # TODO: 用 ThreadPoolExecutor 并发跑 range(10)
    #       成功的 append 进 successes，抛异常的 append 进 failures

    assert sorted(successes) == [0, 1, 2, 4, 5, 6, 8, 9], f"成功列表: {successes}"
    assert len(failures) == 2, f"失败了 {len(failures)} 个，应该是 2 个"
    assert all("任务" in str(f) for f in failures), f"失败信息不对: {failures}"


# =================================================================
# 判分器
# =================================================================

def run_all():
    print("=" * 62)
    print("并发编程练习册")
    print("=" * 62)
    passed = 0
    for fn in _checks:
        name = f"{fn.__name__:<34}"
        try:
            fn()
        except AssertionError as e:
            print(f"[FAIL] {name} {e or '断言没通过'}")
        except Exception as e:
            print(f"[ERR ] {name} {type(e).__name__}: {e}")
        else:
            passed += 1
            print(f"[ OK ] {name}")
    total = len(_checks)
    print("-" * 62)
    print(f"通过 {passed}/{total}")
    if passed == total:
        print("全部通过。并发这块的坑基本都见识过了。")


if __name__ == "__main__":
    run_all()


# =================================================================
# 参考答案（建议先自己写）
# =================================================================
"""
ex1_choose_model
    chose = ["asyncio", "multiprocessing", "threading", "to_thread"]

ex2_thread_pool_io
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(io_job, range(5)))

ex3_threads_and_join
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

ex4_event
    gate.set()

ex5_fix_race
    def add():
        nonlocal counter
        for _ in range(20_000):
            with lock:
                tmp = counter
                sum(range(200))
                counter = tmp + 1
    # 关键：读-改-写三步必须在同一把锁里

ex6_semaphore
    def task(i):
        with sem:
            with lock:
                state["active"] += 1
                state["peak"] = max(state["peak"], state["active"])
            time.sleep(0.05)
            with lock:
                state["active"] -= 1

ex7_producer_consumer
    for _ in consumers:          # 两个消费者 -> 两颗毒丸
        q.put(None)

ex8_thread_pool
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(job, range(6)))
    # map 保证结果顺序和输入顺序一致

ex9_future_exception
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(job, i) for i in range(4)]
        for f in futures:
            try:
                f.result()
            except ValueError as e:
                errors.append(e)
    # 不调用 result() 的话，异常就被静默吞掉了

ex10_process_pool
    with multiprocessing.Pool(4) as pool:
        parallel = pool.map(_cpu_worker, [WORK] * 4)
    # 注意用 with，池子会自动 close + join

ex11_process_queue
    for _ in range(3):
        received.append(q.get())
    # 也可以 q.get(timeout=1) 防止卡住

ex12_asyncio_gather
    async def run():
        return await asyncio.gather(*[job(i) for i in range(4)])

ex13_make_it_concurrent
    async def run():
        await asyncio.gather(job(), job(), job())
    # 光写 await 不会并发，必须用 gather / create_task

ex14_async_semaphore
    async def job():
        async with sem:
            state["active"] += 1
            state["peak"] = max(state["peak"], state["active"])
            await asyncio.sleep(0.05)
            state["active"] -= 1

ex15_timeout
    async def run():
        try:
            return await asyncio.wait_for(slow(), timeout=0.1)
        except asyncio.TimeoutError:
            return "timeout"
    # 3.11+ 也可以写成 async with asyncio.timeout(0.1)

ex16_to_thread
    async def run():
        gaps = []

        async def heartbeat():
            last = time.perf_counter()
            for _ in range(10):
                await asyncio.sleep(0.02)
                now = time.perf_counter()
                gaps.append(now - last)
                last = now

        # 注意顺序：heartbeat 返回 None，所以结果里第一个是 None
        _, result = await asyncio.gather(heartbeat(), asyncio.to_thread(blocking))
        return result, gaps

ex17_spot_the_bug
    answers = ["race", "blocking", "guard", "swallowed"]

ex18_capstone
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(task, i) for i in range(10)]
        for f in futures:
            try:
                successes.append(f.result())
            except RuntimeError as e:
                failures.append(e)
    # 也可以用 as_completed(futures)，完成一个处理一个
"""
