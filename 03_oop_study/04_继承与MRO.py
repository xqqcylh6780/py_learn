# -*- coding: utf-8 -*-
"""
04 继承与 MRO —— 单继承、多重继承、方法解析顺序
==================================================

运行：  python 04_继承与MRO.py

MRO = Method Resolution Order，方法解析顺序。
它决定了「调用 obj.method() 时，Python 到底按什么顺序去哪个类里找」。
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 单继承与 super()
# ---------------------------------------------------------------
show("1. 单继承：super() 是「交给下一个」而不是「交给父类」")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def intro(self):
        return f"我是 {self.name}，{self.speak()}"


class Cat(Animal):
    def __init__(self, name, lives=9):
        super().__init__(name)          # 把通用初始化交给上一层
        self.lives = lives

    def speak(self):
        return "喵"


cat = Cat("咪咪")
print(cat.intro())
print("lives =", cat.lives, " <- 子类扩展出来的字段")
print()
print("子类没写 __init__ 时，会自动借用父类的。写了一般要先 super().__init__(...)。")


# ---------------------------------------------------------------
# 2. 多重继承与 MRO
# ---------------------------------------------------------------
show("2. 多重继承：方法到底先找谁")


class A:
    def hello(self):
        return "A"


class B(A):
    def hello(self):
        return "B -> " + super().hello()


class C(A):
    def hello(self):
        return "C -> " + super().hello()


class D(B, C):
    def hello(self):
        return "D -> " + super().hello()


print("D 的 MRO:")
for i, cls in enumerate(D.__mro__):
    print(f"  [{i}] {cls.__name__}")

print()
print("D().hello() =", D().hello())
print()
print("看到重点了吗：super() 不是「父类」，是「MRO 里的下一个」。")
print("所以 B 里的 super() 走到了 C，而不是直接跳到 A。")


# ---------------------------------------------------------------
# 3. 经典菱形问题，用 super() 协作解决
# ---------------------------------------------------------------
show("3. 菱形继承：为什么必须用 super() 而不是硬写父类名")


class Base:
    def __init__(self):
        print("   Base.__init__ 只执行一次")
        self.log = []


class Left(Base):
    def __init__(self):
        print("   Left.__init__")
        super().__init__()


class Right(Base):
    def __init__(self):
        print("   Right.__init__")
        super().__init__()


class Bottom(Left, Right):
    def __init__(self):
        print("   Bottom.__init__")
        super().__init__()


print("Bottom() 的初始化过程：")
b = Bottom()
print("MRO:", [c.__name__ for c in Bottom.__mro__])
print()
print("每个 __init__ 都只跑了一次，Base 也没被重复初始化 —— 这就是协作式 super 的功劳。")
print("如果每个类里硬写 Base.__init__(self)，Base 会被跑两次。")


# ---------------------------------------------------------------
# 4. isinstance / issubclass
# ---------------------------------------------------------------
show("4. 判断类型：isinstance 与 issubclass")

d = D()
print("isinstance(d, D)      =", isinstance(d, D))
print("isinstance(d, A)      =", isinstance(d, A), " <- 祖先也算")
print("isinstance(d, B)      =", isinstance(d, B))
print("issubclass(D, A)      =", issubclass(D, A))
print("issubclass(D, (B, C)) =", issubclass(D, (B, C)), " 可以传元组，任一命中即可")
print()
print("注意：type(d) is A 是 False。判断类型优先用 isinstance，别用 type() == 。")


# ---------------------------------------------------------------
# 5. 组合优于继承
# ---------------------------------------------------------------
show("5. 组合优于继承")


class Engine:
    def start(self):
        return "引擎启动"


class Car:
    def __init__(self):
        self.engine = Engine()          # 组合：有一个引擎

    def start(self):
        return "汽车：" + self.engine.start()


print(Car().start())
print()
print("继承表达「是一种」（猫是动物），组合表达「有一个」（车有引擎）。")
print("关系说不清时，多半该用组合 —— 继承层级一深，改动会变得非常痛苦。")


# ---------------------------------------------------------------
# 6. Mixin：多重继承最正当的用法
# ---------------------------------------------------------------
show("6. Mixin：只为「附加能力」而生的类")


class JsonMixin:
    """只提供 to_json，自己不单独使用。"""

    def to_json(self):
        import json
        return json.dumps(self.__dict__, ensure_ascii=False)


class User(JsonMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


print(User("张三", 28).to_json())
print()
print("Mixin 的规矩：名字以 Mixin 结尾、不单独实例化、只加一小块能力。")
print("它就是在不破坏继承树的前提下「贴」上功能。")


show("练习：去 99_exercises.py 做 ex7 ~ ex8")
