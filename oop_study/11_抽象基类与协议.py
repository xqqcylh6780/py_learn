# -*- coding: utf-8 -*-
"""
11 抽象基类与协议 —— 怎么把「你必须实现这个方法」写进代码里
=============================================================

运行：  python 11_抽象基类与协议.py

两种表达「接口」的方式：
  ABC      —— 显式继承，我来规定你必须实现什么（名义子类型）
  Protocol —— 不继承也行，只要方法长得对就算数（结构子类型）
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 没有约束时会发生什么
# ---------------------------------------------------------------
show("1. 靠注释的约定，等于没有约定")


class ShapeBad:
    def area(self):
        raise NotImplementedError("子类自己实现")      # 只能在运行时才发现


class CircleBad(ShapeBad):
    pass                                   # 忘了实现，也不报错


print("CircleBad() 能造出来:", CircleBad())
try:
    CircleBad().area()
except NotImplementedError as e:
    print("但一调用就炸:", e)
print()
print("问题：错误暴露得太晚了。抽象基类就是为了把它提前到「写代码时」。")


# ---------------------------------------------------------------
# 2. ABC + abstractmethod
# ---------------------------------------------------------------
show("2. 抽象基类：不实现就造不出来")


class Shape(ABC):
    @abstractmethod
    def area(self):
        """子类必须实现。"""

    @abstractmethod
    def perimeter(self):
        """子类必须实现。"""

    def describe(self):                    # 抽象类里也能有具体方法
        return f"面积 {self.area():.2f}，周长 {self.perimeter():.2f}"


try:
    Shape()
except TypeError as e:
    print("实例化抽象类     :", e)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        import math
        return math.pi * self.r ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.r


try:
    class HalfDone(Shape):
        def area(self):
            return 1
    HalfDone()
except TypeError as e:
    print("只实现一半       :", e)

print("实现了就可以   :", Circle(2).describe())
print()
print("关键：@abstractmethod 标记的方法，子类不覆盖就无法实例化。")
print("错误在「造对象」这一刻就暴露了，而不是等调用到那行。")


# ---------------------------------------------------------------
# 3. 用 ABC 表达「可比较 / 可迭代」这类通用约束
# ---------------------------------------------------------------
show("3. 标准库里的抽象基类")

from collections.abc import Iterable, Sequence, Mapping, Sized

print("list 是 Sequence 吗 :", isinstance([1, 2], Sequence))
print("dict 是 Mapping 吗  :", isinstance({}, Mapping))
print("str 是 Iterable 吗  :", isinstance("abc", Iterable))
print("有 len 的都算 Sized :", isinstance({1, 2}, Sized))
print()
print("这些就是 collections.abc 里的抽象基类。注意：有些旧式对象只实现 __getitem__，")
print("依然能被 iter()/for 遍历却未必被 isinstance(x, Iterable) 识别；真要判断可迭代，直接尝试 iter(x) 最可靠。")


# ---------------------------------------------------------------
# 4. 虚拟子类：不改对方代码也能「注册」进来
# ---------------------------------------------------------------
show("4. register —— 把别人的类拉进自己的体系")


class MySequence(ABC):
    @abstractmethod
    def get(self, i):
        ...


class ThirdPartyList:                   # 别人的类，不可能去改它
    def get(self, i):
        return i * 2


MySequence.register(ThirdPartyList)     # 注册为虚拟子类

print("isinstance 通过 :", isinstance(ThirdPartyList(), MySequence))
print("issubclass 通过 :", issubclass(ThirdPartyList, MySequence))
print()
print("注意：register 只是让 isinstance 返回 True，并不会真的检查方法是否存在。")
print("它是个「我保证它符合」的声明，用错了要自己负责。")


# ---------------------------------------------------------------
# 5. Protocol：不继承也能算数
# ---------------------------------------------------------------
show("5. Protocol —— 鸭子类型的正式写法")


@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str:
        ...


class MyCircle:
    def draw(self):
        return "画一个圆"


class Square:
    def draw(self):
        return "画一个方块"


class Rock:
    def roll(self):
        return "滚"


print("MyCircle 继承了 Drawable 吗 :", Drawable in MyCircle.__mro__, " <- 并没有")
print("但 issubclass 仍然通过      :", issubclass(MyCircle, Drawable))
print("isinstance 也通过           :", isinstance(MyCircle(), Drawable))
print("Square 一样                 :", isinstance(Square(), Drawable))
print("Rock 没有 draw              :", isinstance(Rock(), Drawable))
print()
print("这就是 Protocol 的威力：它只关心「有没有那个方法」，不关心继承关系。")


def render_all(items):
    """只要求传进来的东西有 draw()。"""
    for it in items:
        print("   ", it.draw())


render_all([MyCircle(), Square()])
print()
print("对比一下：")
print("  ABC      = 名义子类型，必须显式继承，适合「我要管控实现方」")
print("  Protocol = 结构子类型，看方法不看血缘，适合「我只关心能力」")
print()
print("日常写业务代码，Protocol 往往更顺手 —— 因为它不强求别人改代码。")


show("练习：去 99_exercises.py 做 ex18 ~ ex19")
