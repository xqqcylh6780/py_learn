# -*- coding: utf-8 -*-
"""
03 线程同步 —— 锁、信号量、事件、死锁
========================================

运行：  python 03_线程同步.py

只要多个线程会「写」同一份数据，就必须考虑同步。
这一节先看事故现场，再一个个上工具。
"""

import threading
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 事故现场：竞态条件
# ---------------------------------------------------------------
show("1. 事故现场：计数为什么少了很多")

THREADS = 4


def run_threads(target, n_threads=THREADS):
    ts = [threading.Thread(target=target) for _ in range(n_threads)]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return time.perf_counter() - t0


# ---- 第一次：最朴素的写法，代码里没有任何多余操作 ----
NATURAL_N = 200_000
counter = 0


def add_natural():
    global counter
    for _ in range(NATURAL_N):
        counter += 1


elapsed = run_threads(add_natural)
natural_total = NATURAL_N * THREADS

print(f"  A. 朴素版：{THREADS} 个线程各加 {NATURAL_N:,} 次，应该是 {natural_total:,}")
print(f"     实际结果: {counter:,}   （耗时 {elapsed:.2f} 秒）")

if counter == natural_total:
    print("     居然全对。这就是竞态最阴险的地方 —— 它会「时对时错」。")
else:
    print(f"     丢了 {natural_total - counter:,} 次")

print()
print("  跑得太快，线程来不及在关键点上抢跑。我们把那个抢跑的窗口撑开再看：")
print()

# ---- 第二次：人为把竞态窗口放大，让问题必然暴露 ----
WIDENED_N = 50_000
counter = 0


def add_widened():
    global counter
    for _ in range(WIDENED_N):
        tmp = counter           # 步骤1：把当前值读出来
        sum(range(200))         # 中间干点别的事，撑开窗口（真实代码里没有这行）
        counter = tmp + 1       # 步骤2：把加完的值写回去


elapsed = run_threads(add_widened)
widened_total = WIDENED_N * THREADS
lost = widened_total - counter

print(f"  B. 放大版：{THREADS} 个线程各加 {WIDENED_N:,} 次，应该是 {widened_total:,}")
print(f"     实际结果: {counter:,}   （耗时 {elapsed:.2f} 秒）")
print(f"     丢了 {lost:,} 次，错误率 {lost / widened_total * 100:.1f}%")

print()
print("为什么？counter += 1 看着是一行，字节码层面其实是三步：")
print("    LOAD  counter    <- 读出来")
print("    ADD   1          <- 加一")
print("    STORE counter    <- 写回去")
print()
print("线程可能在这个中间被切走：")
print("   线程A 读到 100 -> 被切走 -> 线程B 也读到 100")
print("   线程A 写回 101 -> 线程B 也写回 101")
print("   加了两次，却只涨了 1。")
print()
print("B 版的 sum(range(50)) 只是「放大镜」，让窗口宽到必然撞上。")
print("A 版里窗口一样存在，只是窄到要靠运气才撞得到 —— 这才是它可怕的地方：")
print("测试环境跑一万次都对，线上高峰期就出错。")
print()
print("教训：有 GIL 不等于线程安全。GIL 只保证「单条字节码」不被打断，")
print("不保证「多条字节码组成的逻辑」不被打断。")


# ---------------------------------------------------------------
# 2. Lock：把三步包成一步
# ---------------------------------------------------------------
show("2. 用 Lock 修好它")

counter = 0
lock = threading.Lock()


def safe_add():
    global counter
    for _ in range(WIDENED_N):
        with lock:              # 进这块区域，别人只能在外面等
            tmp = counter
            sum(range(200))     # 窗口还在，但已经锁上了
            counter = tmp + 1


elapsed = run_threads(safe_add)

print(f"  加了锁之后: {counter:,}")
print(f"  正确吗    : {counter == widened_total}")
print(f"  耗时      : {elapsed:.2f} 秒")
print()
print("完全相同的窗口，只是套了个 with lock，数字就一分不差了。")
print()
print("用 with lock: 是最推荐的写法 —— 就算中间抛异常，锁也会自动释放。")
print("手写 lock.acquire() / lock.release() 一旦忘了 release，就是死锁。")
print()
print("另一个角度：加锁让程序变慢了（临界区变成串行）。")
print("所以临界区要尽量小 —— 只把真正共享的那几行包进去，别整段包。")


# ---------------------------------------------------------------
# 3. RLock：可重入锁
# ---------------------------------------------------------------
show("3. RLock：同一个线程能重复获取")

normal_lock = threading.Lock()

print("普通 Lock 在同一线程里连拿两次 -> 自己把自己锁死：")
try:
    if normal_lock.acquire(timeout=0.1):
        print("   第一次拿到了")
        got = normal_lock.acquire(timeout=0.1)
        print("   第二次拿到了吗:", got, " <- 拿不到，因为锁已经被自己持有")
        normal_lock.release()
except Exception as e:
    print("   出错了:", e)

rlock = threading.RLock()
with rlock:
    print("RLock 第一次:", True)
    with rlock:
        print("RLock 第二次:", True, " <- 同一个线程可以重复进")

print()
print("什么时候需要 RLock：一个加锁的方法内部调用了另一个加锁的方法。")
print("比如 add() 有锁，add_all() 也有锁，而 add_all 里调用了 add。")
print()
print("优先用普通 Lock。RLock 只在真的需要重入时才用，")
print("因为它会掩盖「锁设计得不对」这个信号。")


# ---------------------------------------------------------------
# 4. Semaphore：限制同时干活的线程数
# ---------------------------------------------------------------
show("4. Semaphore：控制并发数量")

sem = threading.Semaphore(3)        # 最多 3 个同时进行
active = []
lock = threading.Lock()


def limited_task(i):
    with sem:
        with lock:
            active.append(i)
            current = list(active)
        time.sleep(0.08)
        with lock:
            active.remove(i)
        print(f"   任务{i} 在跑，当前并发数 {len(current)}")


threads = [threading.Thread(target=limited_task, args=(i,)) for i in range(8)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print()
print("8 个任务，但同一时刻最多 3 个在跑。")
print("用途：限制对数据库/第三方接口的并发请求数，防止把对方打挂。")
print()
print("注意和 Lock 的区别：Lock 只允许 1 个，Semaphore 允许 N 个。")
print("Semaphore(1) 的效果就等于 Lock。")


# ---------------------------------------------------------------
# 5. Event：线程之间的信号灯
# ---------------------------------------------------------------
show("5. Event：一个线程等信号，另一个线程发信号")

ready = threading.Event()
result = {}


def producer():
    print("   [生产者] 正在准备数据...")
    time.sleep(0.15)
    result["data"] = "准备好了"
    ready.set()                     # 点亮信号灯
    print("   [生产者] 已发出信号")


def consumer():
    print("   [消费者] 等信号中...")
    ready.wait()                    # 睡觉，直到有人 set
    print("   [消费者] 收到信号，拿到:", result["data"])


tc = threading.Thread(target=consumer)
tp = threading.Thread(target=producer)
tc.start()
tp.start()
tc.join()
tp.join()

print()
print("Event 三板斧：")
print("  event.set()      点亮，所有 wait 的线程被唤醒")
print("  event.wait()     阻塞直到被点亮（可以加 timeout）")
print("  event.clear()    熄灯，重新变成等待状态")
print()
print("它比轮询（while not flag: sleep）好得多 —— 不浪费 CPU，响应还更快。")


# ---------------------------------------------------------------
# 6. 死锁：最经典的翻车方式
# ---------------------------------------------------------------
show("6. 死锁是怎么发生的")

lock_a = threading.Lock()
lock_b = threading.Lock()


def thread_1():
    with lock_a:
        print("   线程1 拿到了 lock_a，想再拿 lock_b")
        time.sleep(0.05)
        got = lock_b.acquire(timeout=0.3)      # 用 timeout 演示，避免真卡死
        if got:
            print("   线程1 也拿到了 lock_b")
            lock_b.release()
        else:
            print("   线程1 拿不到 lock_b")


def thread_2():
    with lock_b:
        print("   线程2 拿到了 lock_b，想再拿 lock_a")
        time.sleep(0.05)
        got = lock_a.acquire(timeout=0.3)
        if got:
            print("   线程2 也拿到了 lock_a")
            lock_a.release()
        else:
            print("   线程2 拿不到 lock_a")


t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)
t1.start()
t2.start()
t1.join()
t2.join()

print()
print("上面两个线程刚好错开了，所以都没卡住。但把 timeout 去掉：")
print("  线程1 等 lock_b，而 lock_b 在线程2 手里")
print("  线程2 等 lock_a，而 lock_a 在线程1 手里")
print("  两边都不放手 -> 永久卡死。这就是死锁。")
print()
print("避免死锁的四条实用规则：")
print("  1. 所有线程按「同一个顺序」获取多把锁（比如永远先 A 后 B）")
print("  2. 能用一把锁就别用两把")
print("  3. 加锁时带 timeout，拿不到就退出来重试")
print("  4. 临界区别嵌套，也别在里面调用别人的回调")


# ---------------------------------------------------------------
# 7. 到底该不该加锁
# ---------------------------------------------------------------
show("7. 什么时候必须加锁")

print("必须加锁：多个线程会「写」同一份数据。")
print("  计数、累加、往同一个列表里 append（复合操作）、改字典的多个键、")
print("  「先判断再修改」这种 read-modify-write 模式。")
print()
print("不用加锁：")
print("  只读共享数据 —— 完全不冲突")
print("  各线程只碰自己的局部变量 —— 天然隔离，这是最好的设计")
print()
print("最省事的思路：能用「不共享」解决的，就别用锁。")
print("让每个线程处理自己的数据，最后汇总，比到处加锁清爽得多。")


show("练习：去 99_exercises.py 做 ex5 ~ ex6")
