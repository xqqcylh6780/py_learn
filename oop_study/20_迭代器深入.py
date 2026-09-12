# -*- coding: utf-8 -*-
"""
20 迭代器深入 —— 生成器的完整能力
====================================

运行：  python 20_迭代器深入.py

16 节讲了「for 循环怎么工作」，这一节讲「把生成器用到极致」：
send / throw / close、yield from 的完整语义、惰性流水线、itertools。
"""

import itertools
import tracemalloc


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 三者关系一次理清
# ---------------------------------------------------------------
show("1. 可迭代 / 迭代器 / 生成器")

print("可迭代对象 (Iterable)  能被 iter(obj) 成功转换成迭代器；不保证一定能重复遍历")
print("迭代器     (Iterator)  有 __iter__ 和 __next__，有状态，用完就空")
print("生成器     (Generator) 用 yield 写出来的函数，本质上就是个迭代器")
print()
print("关系：可迭代对象 --iter()--> 迭代器 <--生成器函数调用后就是迭代器")
print()
print("list 是可迭代对象，但不是迭代器:", hasattr([], "__next__"))
print("生成器是迭代器，也是可迭代对象 :",
      hasattr((x for x in []), "__next__"), hasattr((x for x in []), "__iter__"))


# ---------------------------------------------------------------
# 2. 手写迭代器的经典错误
# ---------------------------------------------------------------
show("2. 坑：__iter__ 返回 self 的后果")


class BadRange:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self                     # 危险

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i - 1


bad = BadRange(3)
print("第一次遍历:", list(bad))
print("第二次遍历:", list(bad), " <- 空了！状态被上一次耗光了")


class GoodRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return GoodRangeIterator(self.n)    # 每次都发一个全新的


class GoodRangeIterator:
    def __init__(self, n):
        self.n, self.i = n, 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i - 1


good = GoodRange(3)
print("第一次遍历:", list(good))
print("第二次遍历:", list(good), " <- 正常，因为每次都是新的迭代器")
print()
print("如果想更省事，直接写成生成器函数，Python 自动帮你处理这些：")


def good_range_gen(n):
    for i in range(n):
        yield i


print("生成器版   :", list(good_range_gen(3)), list(good_range_gen(3)))


# ---------------------------------------------------------------
# 3. 生成器不只有 yield：返回值
# ---------------------------------------------------------------
show("3. 生成器的 return 是有意义的")


def with_return():
    yield 1
    yield 2
    return "这是我的返回值"


g = with_return()
print("next ->", next(g))
print("next ->", next(g))
try:
    next(g)
except StopIteration as e:
    print("StopIteration 里带着:", e.value)

print()
print("平时用不到，但 yield from 需要它 —— 见第 5 节。")


# ---------------------------------------------------------------
# 4. send：把值送进生成器
# ---------------------------------------------------------------
show("4. send —— 生成器可以「双向通信」")


def running_average():
    total, count = 0.0, 0
    average = None
    while True:
        x = yield average           # yield 既吐出值，也接收值
        if x is None:
            break
        total += x
        count += 1
        average = total / count
    return total, count


avg = running_average()
next(avg)                            # 必须先推进到第一个 yield
print("   send(10) ->", avg.send(10))
print("   send(20) ->", avg.send(20))
print("   send(30) ->", avg.send(30))

try:
    avg.send(None)                   # 触发 break
except StopIteration as e:
    print("   结束，返回累计值:", e.value)

print()
print("要点：刚创建的生成器还没停在 yield 上，所以第一次必须用 next() 启动，")
print("不能直接 send(非 None)，否则会 TypeError。")
print()
print("还有个方法叫 throw()，可以往生成器里丢异常；close() 可以提前结束它。")
print("这些主要给协程框架用，日常写业务很少碰 —— 现在更推荐 asyncio。")


# ---------------------------------------------------------------
# 5. yield from 的完整语义
# ---------------------------------------------------------------
show("5. yield from —— 不只是语法糖")


def inner():
    yield 1
    yield 2
    return "inner 的结果"


def outer():
    result = yield from inner()      # 既能转发 yield，也能拿到返回值
    print("   outer 收到 inner 的返回值:", result)
    yield 3


print("遍历结果:", list(outer()))
print()
print("yield from inner() 做了三件事：")
print("  1. 把 inner 产出的值原样转发出去")
print("  2. 把 send() 进来的值转发给 inner")
print("  3. inner 结束后，把它的 return 值当作表达式的结果")
print()
print("等于手写一个 for + yield，但省事得多，也更快。")


# ---------------------------------------------------------------
# 6. 惰性流水线
# ---------------------------------------------------------------
show("6. 把生成器串成流水线")


def read_numbers(lines):
    for line in lines:
        yield int(line.strip())


def only_even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n


def squared(nums):
    for n in nums:
        yield n * n


raw = ["1", "2", "3", "4", "5", "6", "7", "8"]

pipeline = squared(only_even(read_numbers(raw)))
print("流水线结果:", list(pipeline))
print()
print("每一环都只处理「流过来的那一个」，中间不产生任何临时列表。")
print("数据有一亿行也不会爆内存，因为它永远是「一个进、一个出」。")
print()
print("这就是 Linux 管道 | 的思路。Python 里用生成器写出来一样优雅：")
print("    squared(only_even(read_numbers(lines)))")
print("    读 -> 筛 -> 平方，三行代码各管一件事，还能单独测试。")


# ---------------------------------------------------------------
# 7. itertools 三大类
# ---------------------------------------------------------------
show("7. itertools：三个抽屉")

print("抽屉一：无限序列（记得配 islice 截断）")
print("   count   :", list(itertools.islice(itertools.count(5, 2), 5)))
print("   cycle   :", list(itertools.islice(itertools.cycle("AB"), 6)))
print("   repeat  :", list(itertools.repeat("x", 4)))

print()
print("抽屉二：组合")
print("   product        :", list(itertools.product([0, 1], repeat=2)))
print("   permutations   :", list(itertools.permutations("AB", 2)), " (有顺序)")
print("   combinations   :", list(itertools.combinations("ABC", 2)), " (无顺序)")

print()
print("抽屉三：加工与过滤")
print("   chain       :", list(itertools.chain([1, 2], "ab")))
print("   accumulate  :", list(itertools.accumulate([1, 2, 3, 4])))
print("   takewhile   :", list(itertools.takewhile(lambda x: x < 4, [1, 2, 5, 1])))
print("   dropwhile   :", list(itertools.dropwhile(lambda x: x < 4, [1, 2, 5, 1])))
print("   pairwise    :", list(itertools.pairwise([1, 2, 3, 4])))
print("   zip_longest :", list(itertools.zip_longest([1, 2, 3], "ab", fillvalue="-")))


# ---------------------------------------------------------------
# 8. 内存实测
# ---------------------------------------------------------------
show("8. 列表推导 vs 生成器表达式")

N = 500_000

tracemalloc.start()
squares_list = [i * i for i in range(N)]
list_mb = tracemalloc.get_traced_memory()[1] / 1024 / 1024
tracemalloc.stop()
del squares_list

tracemalloc.start()
squares_gen = (i * i for i in range(N))
gen_mb = tracemalloc.get_traced_memory()[1] / 1024 / 1024
tracemalloc.stop()
del squares_gen

print(f"   [i*i for i in range({N:,})]  : {list_mb:8.1f} MB")
print(f"   (i*i for i in range({N:,}))  : {gen_mb:8.4f} MB")
print(f"   差了 {list_mb / max(gen_mb, 0.0001):,.0f} 倍")
print()
print("注意：生成器的主要优势是省内存，不保证比列表更快；具体速度要实测。")
print("如果只顺序消费一次，生成器通常更省内存；如果要反复遍历或按下标取，列表更合适。")


# ---------------------------------------------------------------
# 9. 另外两个坑
# ---------------------------------------------------------------
show("9. 坑：生成器只能用一次")


def numbers():
    yield 1
    yield 2


g2 = numbers()
print("第一次:", list(g2))
print("第二次:", list(g2), " <- 空的")
saved = numbers()
print("重新调用函数就好了:", list(saved), " <- 每次调用都产生新的生成器")


show("10. 坑：闭包里的变量是延迟绑定的")

funcs = [lambda: i for i in range(3)]
print("   [lambda: i for i in range(3)]  ->", [f() for f in funcs])
print("   期望 [0,1,2]，实际全是 2 —— 因为查找 i 是调用时才发生的")

funcs2 = [lambda i=i: i for i in range(3)]
print("   [lambda i=i: i ...]            ->", [f() for f in funcs2], " <- 用默认值锁住")

print()
print("同理，生成器表达式里引用的变量也是延迟求值的。")
print("这个问题和生成器是同一类：只要是「以后才算」，就要留个心眼。")


# ---------------------------------------------------------------
# 11. 实战：分页
# ---------------------------------------------------------------
show("11. 实战：把任意序列切成一页一页")


def chunked(iterable, size):
    """不一次性读完，来多少切多少。"""
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk


for i, page in enumerate(chunked(range(1, 11), 3), 1):
    print(f"   第 {i} 页: {page}")

print()
print("注意 chunked 接受任何可迭代对象 —— 列表、文件、数据库游标都行。")
print("这就是「面向迭代器编程」的好处：不关心数据从哪来、有多少。")


show("练习：去 99_exercises.py 做 ex29 ~ ex30")
