# -*- coding: utf-8 -*-
"""
03 封装与 property —— 下划线、双下划线、计算属性
===================================================

运行：  python 03_封装与property.py

Python 的封装哲学和 Java 很不一样：
它不是「禁止你访问」，而是「用命名约定提醒你别碰」，
然后把属性访问做得足够优雅，让你不需要写 getXxx/setXxx。
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 三种命名约定的含义
# ---------------------------------------------------------------
show("1. 单下划线 / 双下划线 / 前后各两个下划线")


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance          # 单下划线：内部用，请别碰
        self.__secret = "密钥"           # 双下划线：会被改名

    def show_secret(self):
        return self.__secret


a = Account("张三", 100)

print("正常属性      :", a.owner)
print("单下划线属性  :", a._balance, " <- 能访问，只是个君子协定")

try:
    a.__secret
except AttributeError as e:
    print("双下划线属性  :", e)

print()
print("它其实没消失，只是被改名成了 _Account__secret：")
print("  a._Account__secret =", a._Account__secret, " <- 真想拿还是拿得到")
print()
print("所以双下划线的作用是「防止子类不小心撞名」，不是「保密」。")


# ---------------------------------------------------------------
# 2. 名称改写（name mangling）到底解决了什么
# ---------------------------------------------------------------
show("2. 双下划线解决的问题：继承时的撞名")


class Parent:
    def __init__(self):
        self.__data = "父类的数据"

    def get(self):
        return self.__data


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = "子类自己的数据"

    def get_child(self):
        return self.__data


c = Child()
print("父类方法看到的是:", c.get())
print("子类方法看到的是:", c.get_child())
print()
print("两个 __data 被改成了 _Parent__data 和 _Child__data，所以互不干扰。")
print("这就是 Python 用来避免继承撞名的手段。")


# ---------------------------------------------------------------
# 3. property：让属性访问带上逻辑
# ---------------------------------------------------------------
show("3. property —— 看起来像属性，其实在跑函数")


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius           # 注意：这里走的是下面的 setter

    @property
    def celsius(self):                   # getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):            # setter：赋值时先校验
        if value < -273.15:
            raise ValueError("低于绝对零度了，物理不存在")
        self._celsius = value

    @property
    def fahrenheit(self):                # 只读计算属性：没有 setter
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print("t.celsius    =", t.celsius)
print("t.fahrenheit =", t.fahrenheit, " <- 现算的，没有存这个字段")

t.celsius = 100
print("改成 100 度后:", t.fahrenheit, "华氏")

try:
    t.celsius = -300
except ValueError as e:
    print("设置非法值  :", e)

try:
    t.fahrenheit = 100
except AttributeError as e:
    print("写只读属性  :", e)


# ---------------------------------------------------------------
# 4. property 的三种形态
# ---------------------------------------------------------------
show("4. 只读 / 可读写 / 带删除逻辑")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("半径必须为正")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("    （半径被删了，重置为 1）")
        self._radius = 1

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2


cc = Circle(2)
print("面积        =", round(cc.area, 3))
del cc.radius
print("删除后半径  =", cc.radius)


# ---------------------------------------------------------------
# 5. 什么时候该上 property
# ---------------------------------------------------------------
show("5. 什么时候该上 property")

print("该用：")
print("  - 赋值需要校验，比如年龄不能为负")
print("  - 需要现算，比如由半径算面积，别存冗余字段")
print("  - 老代码里本来是公开属性，后来要加逻辑")
print()
print("不必用：")
print("  - 只是 get/set 原样转发，那就直接公开属性")
print()
print("Python 的惯例是：先公开 self.x，等真需要逻辑了再改成 property ——")
print("因为改成 property 之后，调用方的 obj.x 写法一个字都不用动。")
print("这一点和 Java 上来就写 getter/setter 的习惯正好相反。")


show("练习：去 99_exercises.py 做 ex5 ~ ex6")
