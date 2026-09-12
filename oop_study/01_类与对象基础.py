# -*- coding: utf-8 -*-
"""
01 类与对象基础 —— 从「是什么」到「属性到底存在哪」
====================================================

运行：  python 01_类与对象基础.py

这一节要建立三个直觉：
  1. 类是模板，实例是按模板造出来的东西
  2. self 就是「这个实例自己」，它不是关键字
  3. 实例属性和类属性存在两个不同的地方
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 最小的类
# ---------------------------------------------------------------
show("1. 定义类、造对象")


class Dog:
    species = "犬科"                  # 类属性：全体共享

    def __init__(self, name, age):
        self.name = name              # 实例属性：每个对象各有一份
        self.age = age

    def speak(self):
        return f"{self.name} 说：汪！"


d1 = Dog("旺财", 3)
d2 = Dog("小白", 1)

print("d1.speak() :", d1.speak())
print("d2.speak() :", d2.speak())
print()
print("self 是什么？其实就是调用时自动传入的第一个参数")
print("  d1.speak()  等价于  Dog.speak(d1)")
print("验证一下:", Dog.speak(d1) == d1.speak())


# ---------------------------------------------------------------
# 2. 实例属性和类属性住在两个地方
# ---------------------------------------------------------------
show("2. 属性查找顺序：先找自己，再找类")

print("d1.__dict__ =", d1.__dict__, " <- 实例自己的属性")
print("类属性放在  :", "species" in Dog.__dict__)
print()
print("d1.species :", d1.species, " <- 自己没有，去类里找")
print("Dog.species:", Dog.species)

d1.species = "猫科"
print()
print("执行 d1.species = '猫科' 之后：")
print("  d1.species  =", d1.species, "  <- 实例字典里有了，优先用它")
print("  d2.species  =", d2.species, "  <- 没被影响")
print("  Dog.species =", Dog.species, " <- 类属性也没变")
print("  d1.__dict__ =", d1.__dict__)


# ---------------------------------------------------------------
# 3. 头号大坑：可变的类属性被所有实例共享
# ---------------------------------------------------------------
show("3. 头号大坑：类属性里的可变对象是共享的")


class BadDog:
    toys = []                         # 危险！所有实例共用这一个列表

    def __init__(self, name):
        self.name = name


b1 = BadDog("旺财")
b2 = BadDog("小白")
b1.toys.append("球")

print("b1 往玩具箱里放了个球")
print("  b1.toys =", b1.toys)
print("  b2.toys =", b2.toys, " <- b2 也多了个球")
print()
print("原因：b1.toys.append 是「修改」，不是「赋值」，动的是类属性那个列表本身。")


class GoodDog:
    def __init__(self, name):
        self.name = name
        self.toys = []                # 正确：每个实例各建一个


g1 = GoodDog("旺财")
g2 = GoodDog("小白")
g1.toys.append("球")
print("正确写法：")
print("  g1.toys =", g1.toys)
print("  g2.toys =", g2.toys, " <- 干净")
print()
print("记法：类属性只放不变的常量；要变的东西一律在 __init__ 里 self.xxx = ...")


# ---------------------------------------------------------------
# 4. 类本身也是对象
# ---------------------------------------------------------------
show("4. 类本身也是对象")

print("type(d1)        =", type(d1))
print("type(d1) is Dog =", type(d1) is Dog)
print("type(Dog)       =", type(Dog), " <- 类的类型是 type")
print("isinstance(d1, Dog) =", isinstance(d1, Dog))
print()
print("既然 type(Dog) 是 type，说明类也是被造出来的对象 —— 这是元类的地基。")


# ---------------------------------------------------------------
# 5. 动态加属性：Python 不拦你，但别乱来
# ---------------------------------------------------------------
show("5. 实例属性随时能加")

d1.color = "黄色"                     # 类里根本没定义过
print("d1.color    =", d1.color)
print("d1.__dict__ =", d1.__dict__)
print()
print("能加，但这说明写错了也没人拦你 —— 08 节的 __slots__ 就是为了堵这个口子。")


show("练习：去 99_exercises.py 做 ex1 ~ ex2")
