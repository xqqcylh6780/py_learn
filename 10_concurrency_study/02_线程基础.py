# -*- coding: utf-8 -*-
"""
02 线程基础 —— 开线程、等线程、守护线程
==========================================

运行：  python 02_线程基础.py

线程的最小知识量其实很少：怎么开、怎么等、什么时候会死。
这一节把这三件事说透。
"""

import threading
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 最简单的线程
# ---------------------------------------------------------------
show("1. 开一个线程")


def say(name, times=3):
    for i in range(times):
        time.sleep(0.05)
        print(f"   [{name}] 第 {i + 1} 次, 当前线程: {threading.current_thread().name}")


t = threading.Thread(target=say, args=("工人A",))
t.start()
t.join()

print()
print("Thread(target=函数, args=(位置参数元组,), kwargs={关键字参数})")
print("参数一定要是元组。只传一个参数时别忘写逗号：args=(\"A\",)")


# ---------------------------------------------------------------
# 2. start() 和直接调用函数的区别
# ---------------------------------------------------------------
show("2. start() vs 直接调用")


def work():
    print(f"   跑在: {threading.current_thread().name}")


print("直接调用 work()：")
work()

print("用线程跑：")
th = threading.Thread(target=work, name="我的线程")
th.start()
th.join()

print()
print("直接调用 = 就在当前线程里跑，跟线程一点关系都没有。")
print("只有 start() 才真的开了个新线程，并且立刻返回、不阻塞。")
print()
print("顺带一提：有人会误写 t.run()，那等于直接调用，白开一个线程。")


# ---------------------------------------------------------------
# 3. join：等它跑完
# ---------------------------------------------------------------
show("3. join 就是「等这个线程结束」")

start = time.perf_counter()
threads = [threading.Thread(target=say, args=(f"工人{i}", 2)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"   三个线程都跑完了，总耗时 {time.perf_counter() - start:.2f} 秒")
print()
print("注意 join 是「等」，不是「启动」。start 循环和 join 循环要分开写。")
print("如果写成 for t in threads: t.start(); t.join()，")
print("那就变成「开一个等一个」，退化成串行了。")


# ---------------------------------------------------------------
# 4. 不 join 会怎样
# ---------------------------------------------------------------
show("4. 不 join：主线程先跑完了")


def slow_worker():
    for i in range(10):
        time.sleep(0.05)
        print(f"   [后台] 第 {i + 1} 次")


print("主线程不等后台线程，直接往下走")
bg = threading.Thread(target=slow_worker)
bg.start()
time.sleep(0.12)
print("主线程走到末尾了")
print()
print("接下来会发生什么？见下一节 —— 因为这是个非 daemon 线程，")
print("Python 会等它跑完才退出程序。")
bg.join()
print("（join 之后才继续）")


# ---------------------------------------------------------------
# 5. daemon 线程
# ---------------------------------------------------------------
show("5. daemon 线程：主线程一走，它就被强杀")


def forever():
    i = 0
    while True:
        i += 1
        time.sleep(0.05)
        print(f"   [守护] 第 {i} 次")


print("非 daemon 线程会让程序「等它」；daemon 线程不会。")
d = threading.Thread(target=forever, daemon=True)
d.start()
time.sleep(0.12)
print("主线程结束 -> 程序立刻退出，守护线程被直接掐掉")
print()
print("规则：")
print("  非 daemon（默认）-> 只要有它还活着，程序就不退出")
print("  daemon           ->  主线程结束，它跟着死")
print()
print("daemon 适合：后台心跳、日志刷盘、监控上报 —— 丢了不影响正确性。")
print("不适合：写文件、写数据库 —— 可能写到一半被掐断，数据就烂了。")


# ---------------------------------------------------------------
# 6. 继承 Thread
# ---------------------------------------------------------------
show("6. 用继承的方式写线程")


class Downloader(threading.Thread):
    def __init__(self, url):
        super().__init__(name=f"下载-{url}")     # 顺便设个线程名，调试时有用
        self.url = url
        self.result = None

    def run(self):                              # 注意是 run，不是 start
        time.sleep(0.05)
        self.result = f"{self.url} 的内容"
        print(f"   {self.name} 完成")


d1 = Downloader("a.com")
d2 = Downloader("b.com")
d1.start()
d2.start()
d1.join()
d2.join()
print("结果:", d1.result, "|", d2.result)
print()
print("继承的好处：能把结果存成属性（self.result），调用方拿得到。")
print("坏处：线程多起来之后，类会爆炸。更好的办法是 05 节的线程池。")


# ---------------------------------------------------------------
# 7. 线程拿不到返回值
# ---------------------------------------------------------------
show("7. 线程的返回值去哪了")


def add(a, b):
    return a + b


result_box = []
th = threading.Thread(target=lambda: result_box.append(add(1, 2)))
th.start()
th.join()
print("   Thread 本身拿不到返回值，只能像这样用个容器接着:", result_box)
print()
print("这是 Thread 设计上的硬伤。要返回值，用 05 节的 ThreadPoolExecutor，")
print("submit() 会给你一个 Future，future.result() 就是返回值。")


# ---------------------------------------------------------------
# 8. 几个常用工具
# ---------------------------------------------------------------
show("8. 常用工具函数")

print("threading.current_thread().name  =", threading.current_thread().name)
print("threading.active_count()         =", threading.active_count())
print("threading.main_thread().name     =", threading.main_thread().name)
print("threading.enumerate()            =", [t.name for t in threading.enumerate()])
print()
print("调试多线程时，给线程起个有意义的名字（name=\"下载-图片1\"），")
print("日志里一眼就能看出是谁在跑。默认名字是 Thread-1、Thread-2，很难认。")


# ---------------------------------------------------------------
# 9. 线程杀不掉
# ---------------------------------------------------------------
show("9. 重要：线程没办法被强制杀死")

print("Python 没有 stop() / kill() 这种 API。原因：")
print("  线程可能正持有锁、正写到一半。硬杀会留下烂摊子。")
print()
print("想让线程停下来，只能用「协作式」的办法：")
print("  1. 用一个 threading.Event 当开关，线程自己定期检查")
print("  2. 用一个队列，往里面放一个「毒丸」表示收工")
print()
print("这是并发编程的通用原则：让任务自己决定何时退出，别从外面砍。")


show("练习：去 99_exercises.py 做 ex3 ~ ex4")
