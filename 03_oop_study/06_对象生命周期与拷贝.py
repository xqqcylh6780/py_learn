# -*- coding: utf-8 -*-
"""
06 对象生命周期与拷贝 —— __new__、__del__、深浅拷贝、弱引用
==============================================================

运行：  python 06_对象生命周期与拷贝.py

一个对象的一生：
    __new__ 造出空壳  ->  __init__ 填充内容  ->  ...使用...  ->  __del__ / 被回收
"""

import copy
import gc
import sys
import weakref


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. __new__ 和 __init__ 的分工
# ---------------------------------------------------------------
show("1. __new__ 负责造，__init__ 负责填")


class Demo:
    def __new__(cls, *args, **kwargs):
        print("   [1] __new__ 被调用，负责造出空对象")
        obj = super().__new__(cls)
        print("   [1] 造好了:", obj)
        return obj

    def __init__(self, x):
        print("   [2] __init__ 被调用，负责填充")
        self.x = x


print("执行 Demo(42)：")
d = Demo(42)
print("最终 d.x =", d.x)
print()
print("关键：__new__ 必须 return 一个实例，__init__ 只能返回 None。")
print("如果 __new__ 返回的不是本类实例，__init__ 就不会被调用（单例就靠这个）。")


# ---------------------------------------------------------------
# 2. 单例：__new__ 最经典的用途
# ---------------------------------------------------------------
show("2. 单例模式")


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, debug=False):
        self.debug = debug


c1 = Config(debug=True)
c2 = Config()
print("c1 is c2 :", c1 is c2, " <- 同一个对象")
print("c2.debug =", c2.debug, " <- 第二次构造又跑了一遍 __init__，把值覆盖了")
print()
print("注意这个坑：__init__ 每次都会执行。要防止重复初始化，得再加个标志位。")


# ---------------------------------------------------------------
# 3. __del__ 靠不住
# ---------------------------------------------------------------
show("3. __del__ 不是「析构函数」，别指望它")


class Resource:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"   __del__ 触发了: {self.name}")


print("创建 r，然后把变量删掉：")
r = Resource("资源A")
print("引用计数:", sys.getrefcount(r) - 1, " (减去 getrefcount 自己那次)")
del r

print()
print("看起来正常。但下面这种循环引用就麻烦了：")


class Node:
    def __init__(self, name):
        self.name = name
        self.peer = None

    def __del__(self):
        print(f"   __del__ 触发了: {self.name}")


gc.disable()                           # 关掉自动回收，让输出稳定可复现
n1 = Node("节点1")
n2 = Node("节点2")
n1.peer = n2
n2.peer = n1
del n1, n2
print("   已经 del 了，但上面什么都没打印 —— 循环引用要靠垃圾回收器")
gc.collect()
print("   手动 gc.collect() 之后才清理掉")
gc.enable()
print()
print("结论：需要确定性释放资源，用 with 语句（15 节），别依赖 __del__。")


# ---------------------------------------------------------------
# 4. 浅拷贝 vs 深拷贝（日常最容易踩）
# ---------------------------------------------------------------
show("4. 浅拷贝 vs 深拷贝")

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)          # 只复制最外层
shallow[0].append(99)
print("浅拷贝后改了内层列表：")
print("  original =", original, " <- 被连累了！")
print("  shallow  =", shallow)
print("  因为内外两层指向的是同一个内层列表:", original[0] is shallow[0])

print()
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)        # 递归复制到底
deep[0].append(99)
print("深拷贝后改了内层列表：")
print("  original2 =", original2, " <- 完全没影响")
print("  deep      =", deep)
print()
print("一句话：copy() 复制一层壳，deepcopy() 复制到底。")
print("嵌套可变对象需要彼此独立时才用 deepcopy；如果允许共享内部对象，浅拷贝更合适。")


# ---------------------------------------------------------------
# 5. 自定义拷贝行为
# ---------------------------------------------------------------
show("5. 用 __copy__ / __deepcopy__ 定制拷贝")


class Box:
    def __init__(self, items):
        self.items = list(items)
        self.copies_made = 0

    def __copy__(self):
        new = Box(self.items)
        new.copies_made = self.copies_made + 1
        return new

    def __repr__(self):
        return f"Box({self.items}, copies_made={self.copies_made})"


box = Box([1, 2, 3])
print("copy.copy(box)    =", copy.copy(box))
print("原对象            =", box, " <- 没被改动")


# ---------------------------------------------------------------
# 6. 弱引用：不增加引用计数的引用
# ---------------------------------------------------------------
show("6. weakref —— 引用了，但不阻止对方被回收")


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name})"


item = Item("苹果")
ref = weakref.ref(item)

print("ref()        =", ref(), " <- 对象还在，能取到")
print("引用计数     =", sys.getrefcount(item) - 1, " 弱引用不增加计数")

del item
gc.collect()
print("del 之后 ref() =", ref(), " <- 对象被回收，弱引用变成 None")
print()
print("用途：缓存、观察者列表。不想因为「登记了一下」就让对象永远不被回收。")

wvd = weakref.WeakValueDictionary()
tmp = Item("香蕉")
wvd["k"] = tmp
print("WeakValueDictionary 里有:", wvd["k"])
del tmp
gc.collect()
print("tmp 被删后，字典也自动空了:", dict(wvd))


show("练习：去 99_exercises.py 做 ex11 ~ ex12")
