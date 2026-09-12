# -*- coding: utf-8 -*-
"""
07 进程间通信 —— 进程之间怎么传数据
======================================

运行：  python 07_进程间通信.py

进程不共享内存，所以要传数据必须走「通信」。
四种方式各有适用场景，这一节全部跑一遍。
"""

import multiprocessing
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---- 给 Queue 用的 ----
def producer(q, n):
    for i in range(n):
        q.put(f"数据{i}")
    q.put(None)                     # 收工信号


def consumer(q, out):
    while True:
        item = q.get()
        if item is None:
            break
        out.append(item)


# ---- 给 Pipe 用的 ----
def pipe_child(conn):
    conn.send(["子进程算出来的", 1, 2, 3])
    reply = conn.recv()
    conn.send(f"收到你的回复: {reply}")
    conn.close()


# ---- 给 Manager 用的 ----
def manager_worker(shared_dict, shared_list, key):
    shared_dict[key] = f"{key} 写的"
    shared_list.append(key)


# ---- 给 Value 用的 ----
def add_to_value(val, times):
    for _ in range(times):
        with val.get_lock():
            val.value += 1


# ---------------------------------------------------------------
# 1. Queue：最常用
# ---------------------------------------------------------------
def part1_queue():
    show("1. multiprocessing.Queue —— 首选方案")

    q = multiprocessing.Queue()
    out = multiprocessing.Manager().list()

    p1 = multiprocessing.Process(target=producer, args=(q, 5))
    p2 = multiprocessing.Process(target=consumer, args=(q, out))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("  子进程收到的数据:", list(out))
    print()
    print("用法和线程的 queue.Queue 几乎一样：put / get，队列空就阻塞。")
    print("底层靠 pickle 序列化，所以传的东西必须能 pickle。")
    print()
    print("注意：multiprocessing.Queue 和 queue.Queue 是两个不同的类，别搞混。")
    print("  queue.Queue            -> 线程之间用")
    print("  multiprocessing.Queue  -> 进程之间用")


# ---------------------------------------------------------------
# 2. Pipe：两队之间的专线
# ---------------------------------------------------------------
def part2_pipe():
    show("2. Pipe —— 双向直连")

    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=pipe_child, args=(child_conn,))
    p.start()

    data = parent_conn.recv()
    print("  父进程收到:", data)
    parent_conn.send("干得好")
    print("  父进程再收到:", parent_conn.recv())
    p.join()

    print()
    print("Pipe 只在「两个进程之间」用，比 Queue 轻量、更快。")
    print("send / recv 是成对出现的，一方 send，另一方 recv。")
    print("超过两个进程就别用 Pipe 了，改用 Queue。")


# ---------------------------------------------------------------
# 3. Manager：把普通容器变成共享的
# ---------------------------------------------------------------
def part3_manager():
    show("3. Manager —— 共享 dict / list")

    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict()
        shared_list = manager.list()

        ps = [
            multiprocessing.Process(
                target=manager_worker, args=(shared_dict, shared_list, f"进程{i}")
            )
            for i in range(3)
        ]
        for p in ps:
            p.start()
        for p in ps:
            p.join()

        print("  共享字典:", dict(shared_dict))
        print("  共享列表:", list(shared_list))

    print()
    print("Manager 最方便 —— 写法跟普通 dict / list 完全一样，")
    print("多个进程都能改，改动互相可见。")
    print()
    print("代价：每次访问都要通过一个管理进程转发，比直接用共享内存慢。")
    print("数据量小、读写不频繁，用 Manager 图省事；")
    print("数据量大或高频读写，用它就太慢了。")


# ---------------------------------------------------------------
# 4. Value / Array：真正的共享内存
# ---------------------------------------------------------------
def part4_shared_memory():
    show("4. Value / Array —— 真共享内存，最快")

    counter = multiprocessing.Value("i", 0)     # i = 有符号整数
    arr = multiprocessing.Array("d", [0.0, 0.0, 0.0])   # d = 双精度浮点

    ps = [
        multiprocessing.Process(target=add_to_value, args=(counter, 1000))
        for _ in range(4)
    ]
    for p in ps:
        p.start()
    for p in ps:
        p.join()

    print("  4 个进程各加 1000 次，结果:", counter.value)
    print("  数组:", list(arr))
    print()
    print("Value / Array 是真·共享内存，读写最快，但只能装 C 语言的基础类型。")
    print("想放复杂结构（比如嵌套 dict），就用 multiprocessing.shared_memory")
    print("或者上 numpy 的共享数组。")
    print()
    print("重要：共享内存意味着多个进程会同时改，所以必须加锁。")
    print("上面用了 with val.get_lock() —— 不加的话，就会重演 03 节的竞态。")


# ---------------------------------------------------------------
# 5. 必须可 pickle
# ---------------------------------------------------------------
def part5_pickle():
    show("5. 传的东西必须能 pickle")

    print("进程之间传数据要序列化，所以这些传不过去：")
    print("  - lambda")
    print("  - 定义在函数内部的嵌套函数")
    print("  - 打开的文件对象、数据库连接、锁")
    print("  - 大多数「有状态」的对象")
    print()

    try:
        import pickle
        pickle.dumps(lambda x: x)
    except Exception as e:
        print("  实测 pickle 一个 lambda:")
        print(f"    {type(e).__name__}: {e}")

    print()
    print("这个坑的典型表现是：明明单进程跑得好好的，一上多进程就报错")
    print("「Can't pickle <function <lambda> ...>」。")
    print()
    print("解法：把要传的函数提到模块顶层，写成普通的 def。")


# ---------------------------------------------------------------
# 6. 四种方式怎么选
# ---------------------------------------------------------------
def part6_choose():
    show("6. 选型建议")

    rows = [
        ("Queue", "多生产者多消费者、任务分发", "中等", "大多数情况的默认选择"),
        ("Pipe", "只有两个进程要通信", "快", "父子进程之间的双向对话"),
        ("Manager", "要共享 dict / list，数据量不大", "慢", "图省事，写法最像单进程"),
        ("Value/Array", "共享几个数字、大数组", "最快", "配合 numpy 处理大数据"),
    ]
    print(f"  {'方式':<12}{'适用场景':<32}{'速度':<8}备注")
    print("  " + "-" * 70)
    for name, scene, speed, note in rows:
        print(f"  {name:<12}{scene:<32}{speed:<8}{note}")

    print()
    print("一句话：优先 Queue，只有两个进程才考虑 Pipe，")
    print("需要共享容器就 Manager（不怕慢的话），追性能才上共享内存。")


def main():
    part1_queue()
    part2_pipe()
    part3_manager()
    part4_shared_memory()
    part5_pickle()
    part6_choose()

    show("练习：去 99_exercises.py 做 ex11")


if __name__ == "__main__":
    main()
