# -*- coding: utf-8 -*-
"""
16 迭代器与生成器协议 —— for 循环到底在做什么
================================================

运行：  python 16_迭代器与生成器协议.py

for x in obj 的执行过程：
    1. 调用 iter(obj) 拿到一个迭代器
    2. 反复调用 next(迭代器)
    3. 直到抛出 StopIteration，循环结束

搞懂这三步，你就能让任何对象支持 for 循环。
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 可迭代 ≠ 迭代器
# ---------------------------------------------------------------
show("1. 可迭代对象和迭代器是两样东西")

nums = [1, 2, 3]
print("list 有 __iter__ 吗 :", hasattr(nums, "__iter__"))
print("list 有 __next__ 吗 :", hasattr(nums, "__next__"), " <- 没有，所以 list 只是可迭代，不是迭代器")

it = iter(nums)                         # 从可迭代对象拿到迭代器
print()
print("iter(nums) 拿到的类型:", type(it).__name__)
print("迭代器有 __next__ 吗 :", hasattr(it, "__next__"))
print()
print("手动 next 一遍：")
print("   next(it) =", next(it))
print("   next(it) =", next(it))
print("   next(it) =", next(it))
try:
    next(it)
except StopIteration:
    print("   再 next  ->  StopIteration（这就是 for 结束的信号）")

print()
print("关键区别：")
print("  可迭代对象 能被 iter(obj) 成功转换成迭代器；很多容器可以反复遍历，但协议本身不保证这一点")
print("  迭代器     iter(it) 返回自身，并实现 __next__；通常是有状态的，用完就空")


# ---------------------------------------------------------------
# 2. 手写一个迭代器类
# ---------------------------------------------------------------
show("2. 手写迭代器：倒着数")


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountdownIterator(self.start)     # 每次都发一个全新的迭代器


class CountdownIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self                              # 迭代器返回自己

    def __next__(self):
        if self.current <= 0:
            raise StopIteration                  # 明确的结束信号
        self.current -= 1
        return self.current + 1


print("for 循环:", [x for x in Countdown(5)])
print("能再遍历一次:", [x for x in Countdown(5)], " <- 因为 __iter__ 每次都造新的")
print()
print("注意为什么要把「可迭代」和「迭代器」拆成两个类：")
print("迭代器是有状态的（记住数到几了），拆开才能反复遍历。")


# ---------------------------------------------------------------
# 3. 生成器函数：写迭代器的省事办法
# ---------------------------------------------------------------
show("3. 生成器：用 yield 代替 __next__")


def countdown(n):
    while n > 0:
        yield n                              # 交出值，然后暂停在这里
        n -= 1


print("生成器对象:", countdown(3))
print("遍历      :", list(countdown(3)))
print()
print("对比一下：上面那个迭代器类写了 15 行，这里 4 行就够了。")
print("yield 的本质：每次 next() 就从上次暂停的地方继续往下跑。")


# ---------------------------------------------------------------
# 4. 生成器是惰性的
# ---------------------------------------------------------------
show("4. 惰性：要一个才算一个")


def lazy_demo():
    print("   [生成器] 开始")
    for i in range(3):
        print(f"   [生成器] 准备产出 {i}")
        yield i
    print("   [生成器] 结束")


gen = lazy_demo()                            # 注意：这里什么都没打印
print("刚创建生成器时，函数体一行都没跑")
print()
print("开始取值：")
for x in gen:
    print("   拿到", x)

print()
print("这就是它能处理「无限序列」和「超大文件」的原因：")
print("不把所有值算出来，只在需要时算一个。")


def natural_numbers():
    """无限序列，永远不会结束。"""
    n = 1
    while True:
        yield n
        n += 1


from itertools import islice

print("从无限序列里取前 8 个:", list(islice(natural_numbers(), 8)))


# ---------------------------------------------------------------
# 5. yield from 和 send
# ---------------------------------------------------------------
show("5. yield from 与 send")


def inner():
    yield 1
    yield 2


def outer_bad():
    for x in inner():                        # 麻烦
        yield x


def outer_good():
    yield from inner()                       # 干净


print("yield from 展开:", list(outer_good()))
print()


def echo():
    while True:
        received = yield                    # yield 也能「收值」
        print("   收到:", received)


e = echo()
next(e)                                      # 先推进到第一个 yield
e.send("你好")
e.send("世界")
e.close()


# ---------------------------------------------------------------
# 6. itertools 速览
# ---------------------------------------------------------------
show("6. itertools：和迭代器协议配套的工具箱")

import itertools

print("chain       拼接多个:", list(itertools.chain([1, 2], [3, 4])))
print("islice      切片    :", list(itertools.islice(itertools.count(10), 5)))
print("cycle       循环    :", list(itertools.islice(itertools.cycle("AB"), 5)))
print("groupby     分组    :",
      [(k, len(list(g))) for k, g in itertools.groupby("aaabbc")])
print("combinations 组合   :", list(itertools.combinations([1, 2, 3], 2)))
print("product     笛卡尔积:", list(itertools.product([1, 2], "ab")))


# ---------------------------------------------------------------
# 7. 什么时候用生成器
# ---------------------------------------------------------------
show("7. 什么时候该用生成器")

print("该用：")
print("  - 数据量很大，不想一次全装进内存")
print("  - 是「流水线」的一环，边读边处理")
print("  - 要表示无限序列")
print()
print("别用：")
print("  - 需要反复遍历同一批数据（生成器用完就空）")
print("  - 需要 len() 或下标访问")
print()
print("判断技巧：如果函数体里出现了「先 append 到列表，最后 return 列表」，")
print("而且调用方只是遍历它，那多半可以改成生成器。")


show("练习：去 99_exercises.py 做 ex24")
