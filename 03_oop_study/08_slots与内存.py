# -*- coding: utf-8 -*-
"""
08 __slots__ 与内存 —— 给对象瘦身，顺便堵住乱加属性
======================================================

运行：  python 08_slots与内存.py

默认情况下，每个实例背后都挂着一个 __dict__ 来存属性。
字典很灵活，但很占地方。__slots__ 把「字典」换成「固定几个槽位」。
"""

import sys
import tracemalloc


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


class WithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WithSlots:
    __slots__ = ("x", "y")            # 只允许这两个属性

    def __init__(self, x, y):
        self.x = x
        self.y = y


# ---------------------------------------------------------------
# 1. 单看一个对象
# ---------------------------------------------------------------
show("1. 单个实例的开销")

d_obj = WithDict(1, 2)
s_obj = WithSlots(1, 2)

print("有 __dict__ 的实例本身 :", sys.getsizeof(d_obj), "字节")
print("它额外挂的 __dict__    :", sys.getsizeof(d_obj.__dict__), "字节")
print("合计                   :", sys.getsizeof(d_obj) + sys.getsizeof(d_obj.__dict__), "字节")
print()
print("用 __slots__ 的实例    :", sys.getsizeof(s_obj), "字节，且没有 __dict__ 那份开销")

try:
    s_obj.__dict__
except AttributeError as e:
    print("访问 s_obj.__dict__     :", e)

print()
print("注意：sys.getsizeof 对这两种对象报的都是", sys.getsizeof(d_obj), "字节，")
print("单看它你会以为没差别 —— 真正的差距在那个 __dict__ 上。")
print("所以下面用 tracemalloc 实测整体内存，那个数字才可信。")


# ---------------------------------------------------------------
# 2. 大批量实例才看得出差距
# ---------------------------------------------------------------
show("2. 造 10 万个对象，差距就明显了")

N = 100_000


def measure(cls):
    tracemalloc.start()
    objs = [cls(i, i) for i in range(N)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del objs
    return current / 1024 / 1024


mb_dict = measure(WithDict)
mb_slots = measure(WithSlots)

print(f"  {N:,} 个 WithDict  : {mb_dict:6.1f} MB")
print(f"  {N:,} 个 WithSlots : {mb_slots:6.1f} MB")
print(f"  省了              : {mb_dict - mb_slots:6.1f} MB"
      f"  ({(1 - mb_slots / mb_dict) * 100:.0f}%)")


# ---------------------------------------------------------------
# 3. 附带的好处：写错属性名会当场报错
# ---------------------------------------------------------------
show("3. 副作用之一：不能随便加属性了")

loose = WithDict(1, 2)
loose.typo_name = "打错了也不报错"        # 静默接受
print("普通对象偷偷加属性:", loose.__dict__)

tight = WithSlots(1, 2)
try:
    tight.typo_name = "打错了"
except AttributeError as e:
    print("__slots__ 对象    :", e)

print()
print("这其实是好事：属性名打错会立刻暴露，而不是变成 None 让你查半天。")


# ---------------------------------------------------------------
# 4. 三个必踩的坑
# ---------------------------------------------------------------
show("4. 坑一：__slots__ 里列的名字不能和类属性重名")

try:
    class Bad1:
        __slots__ = ("x",)
        x = 100                       # 冲突
except ValueError as e:
    print("   ", e)


show("5. 坑二：子类不写 __slots__，就又有 __dict__ 了")


class ChildNoSlots(WithSlots):
    pass                              # 没声明 __slots__


class ChildWithSlots(WithSlots):
    __slots__ = ("z",)


c1 = ChildNoSlots(1, 2)
c1.whatever = "又能乱加了"
print("子类没写 __slots__ :", "有 __dict__ ->", c1.__dict__)

c2 = ChildWithSlots(1, 2)
try:
    c2.whatever = 1
except AttributeError as e:
    print("子类写了 __slots__ :", e)


show("6. 坑三：多个带 __slots__ 的基类会布局冲突")


class BaseA:
    __slots__ = ("a",)


class BaseB:
    __slots__ = ("b",)


try:
    class Multi(BaseA, BaseB):        # 两个非空 slots 的基类
        __slots__ = ()
except TypeError as e:
    print("   ", e)

print()
print("解决办法：最多只能有一个基类带非空 __slots__，其余基类用空元组 ()。")


# ---------------------------------------------------------------
# 7. 什么时候值得用
# ---------------------------------------------------------------
show("7. 什么时候该上 __slots__")

print("值得用：")
print("  - 要创建几十万上百万个实例（数据点、坐标、日志条目）")
print("  - 字段固定、就那几个，不需要动态扩展")
print("  - 想让拼错属性名立刻报错")
print()
print("别用：")
print("  - 普通业务类，省那点内存毫无意义，反而丢掉灵活性")
print("  - 需要动态加属性、需要 __dict__ 的场景")
print()
print("注意它不省时间：访问速度基本没变，纯粹是内存和「确定性」的收益。")


show("练习：去 99_exercises.py 做 ex15")
