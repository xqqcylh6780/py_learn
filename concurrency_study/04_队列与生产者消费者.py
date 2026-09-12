# -*- coding: utf-8 -*-
"""
04 队列与生产者消费者
======================

运行：  python 04_队列与生产者消费者.py

多线程最经典的模型：一拨人负责生产，另一拨人负责消费，中间用一个队列缓冲。
Python 的 queue.Queue 自带锁，你不需要自己写任何同步代码。
"""

import queue
import threading
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 为什么不用普通列表
# ---------------------------------------------------------------
show("1. 用普通列表当队列，你得自己处理这些")

print("共享列表看着能用，但每个操作都要自己加锁：")
print("    if items:               <- 判断")
print("        item = items[0]     <- 读")
print("        del items[0]        <- 删")
print()
print("这三步之间线程会被切走：判断时还有元素，真取的时候已经被别人拿走了。")
print("另外列表头部删除是 O(n)，元素一多就慢。")
print()
print("queue.Queue 把这些全包好了：")
print("  - 内部自带锁，put / get 都是原子的")
print("  - 空的时候 get 会阻塞等待，不用你写轮询")
print("  - 底层是双端队列，进出都是 O(1)")


# ---------------------------------------------------------------
# 2. 生产者消费者
# ---------------------------------------------------------------
show("2. 生产者-消费者模型")

q = queue.Queue(maxsize=5)
POISON = None                       # 毒丸：收到它就该收工了
results = []
lock = threading.Lock()


def producer(n):
    for i in range(n):
        item = f"产品{i}"
        q.put(item)                 # 队列满了会在这里等
        print(f"   [生产] {item}")
        time.sleep(0.01)


def consumer(name):
    while True:
        item = q.get()
        if item is POISON:
            q.task_done()
            print(f"   [消费-{name}] 收到毒丸，收工")
            return
        with lock:
            results.append(item)
        print(f"   [消费-{name}] 处理 {item}")
        time.sleep(0.025)
        q.task_done()               # 告诉队列：这一项处理完了


producers = [threading.Thread(target=producer, args=(6,))]
consumers = [threading.Thread(target=consumer, args=(f"C{i}",)) for i in range(2)]

for t in consumers:
    t.start()
for t in producers:
    t.start()

for t in producers:
    t.join()

for _ in consumers:                 # 每个消费者发一颗毒丸
    q.put(POISON)

for t in consumers:
    t.join()

print(f"\n   共处理 {len(results)} 项: {results}")

print()
print("几个设计点：")
print("  1. 生产者只管往队里扔，不关心谁来消费")
print("  2. 消费者只管从队里拿，不关心谁生产的")
print("  3. 队列满/空时自动阻塞等待，不用写轮询和 sleep")
print("  4. 毒丸（None）是通知消费者收工的标准做法")


# ---------------------------------------------------------------
# 3. queue 的常用方法
# ---------------------------------------------------------------
show("3. 常用方法")

demo_q = queue.Queue()
demo_q.put("a")
demo_q.put("b")

print("qsize()              =", demo_q.qsize())
print("empty()              =", demo_q.empty())
print("get()                =", demo_q.get())
print("get_nowait()         =", demo_q.get_nowait(), " <- 不阻塞，队列空就抛 Empty")

try:
    demo_q.get_nowait()
except queue.Empty:
    print("再 get_nowait()      -> queue.Empty 异常")

try:
    demo_q.get(timeout=0.1)
except queue.Empty:
    print("get(timeout=0.1)     -> 等 0.1 秒还是空，抛 Empty")

full_q = queue.Queue(maxsize=2)
full_q.put(1)
full_q.put(2)
print()
print("有界队列满了之后：")
print("  put_nowait()         -> 抛 queue.Full")
print("  put(timeout=0.1)     -> 等 0.1 秒还是满，抛 Full")
try:
    full_q.put_nowait(3)
except queue.Full:
    print("  实测 put_nowait()    -> queue.Full 异常")


# ---------------------------------------------------------------
# 4. task_done 和 join
# ---------------------------------------------------------------
show("4. task_done 与 join")

work_q = queue.Queue()


def do_work():
    while True:
        item = work_q.get()
        if item is None:
            work_q.task_done()
            return
        time.sleep(0.02)
        print(f"   [工人] 做完了 {item}")
        work_q.task_done()          # 关键：少写这行，join 会永远等下去


workers = [threading.Thread(target=do_work) for _ in range(2)]
for t in workers:
    t.start()

for i in range(4):
    work_q.put(f"任务{i}")

work_q.join()                       # 等到所有 put 进去的都被 task_done
print("   队列里所有任务都处理完了")

for _ in workers:
    work_q.put(None)
for t in workers:
    t.join()

print()
print("queue 内部有个计数器：put 加一，task_done 减一，减到 0 就唤醒 join。")
print("所以调了 get() 就必须配对调 task_done()，否则 join 永远不返回。")


# ---------------------------------------------------------------
# 5. 另外两种队列
# ---------------------------------------------------------------
show("5. PriorityQueue 和 LifoQueue")

pq = queue.PriorityQueue()
for task in [(3, "低优先级"), (1, "高优先级"), (2, "中优先级")]:
    pq.put(task)

print("PriorityQueue 按优先级从小到大出：")
while not pq.empty():
    print("   ", pq.get())

print()
print("注意：PriorityQueue 是按整个元组的第一个元素比较的。")
print("如果第一个元素相同，会去比第二个 —— 这时候第二个必须是可比较的类型，")
print("否则会 TypeError。常见解法是加个自增序号: (priority, seq, item)")

lq = queue.LifoQueue()
for x in [1, 2, 3]:
    lq.put(x)
print()
print("LifoQueue 后进先出:", [lq.get() for _ in range(3)])


# ---------------------------------------------------------------
# 6. 为什么队列能替代大部分锁
# ---------------------------------------------------------------
show("6. 队列的哲学")

print("自己加锁的代码长这样：")
print("    拿锁 -> 改数据 -> 放锁")
print("    出错了忘了放锁 -> 死锁")
print()
print("用队列的代码长这样：")
print("    放进去 / 拿出来")
print()
print("「不要通过共享内存来通信，而要通过通信来共享内存」—— 这句话来自 Go，")
print("但 Python 的 queue 就是同一个思路。")
print()
print("所以：多线程之间要传数据，第一选择是 queue，不是共享变量加锁。")


show("练习：去 99_exercises.py 做 ex7")
