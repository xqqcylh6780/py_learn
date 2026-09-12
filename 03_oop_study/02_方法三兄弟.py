# -*- coding: utf-8 -*-
"""
02 方法三兄弟 —— 实例方法 / 类方法 / 静态方法
================================================

运行：  python 02_方法三兄弟.py

判断口诀，看第一个参数是谁：
  实例方法  def m(self)  -> 收到实例，能读写实例数据
  类方法    def m(cls)   -> 收到类，能造对象、能感知子类
  静态方法  def m()      -> 谁也不收，就是挂在类里命名空间下的普通函数
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 三种方法各写一遍
# ---------------------------------------------------------------
show("1. 同一个类里放三种方法")


class Pizza:
    shop_name = "老王披萨"

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def describe(self):                       # 实例方法
        return " + ".join(self.ingredients)

    @classmethod                              # 类方法
    def margherita(cls):
        return cls(["mozzarella", "tomato"])

    @classmethod
    def shop(cls):
        return f"本店叫 {cls.shop_name}"

    @staticmethod                             # 静态方法
    def is_vegetarian(ingredients):
        meat = {"pepperoni", "ham", "bacon"}
        return not (set(ingredients) & meat)


p = Pizza.margherita()
print("p.describe()            :", p.describe())
print("Pizza.shop()            :", Pizza.shop())
print("is_vegetarian(火腿)     :", Pizza.is_vegetarian(["ham", "cheese"]))
print("is_vegetarian(番茄罗勒) :", Pizza.is_vegetarian(["tomato", "basil"]))


# ---------------------------------------------------------------
# 2. 类方法真正的价值：它认识子类
# ---------------------------------------------------------------
show("2. 类方法里用 cls，而不是硬写类名")


class SubPizza(Pizza):
    shop_name = "小王披萨（分店）"


print("SubPizza.margherita() 造出来的类型:", type(SubPizza.margherita()).__name__)
print("SubPizza.shop() :", SubPizza.shop())
print()
print("因为类方法里写的是 cls(...)，子类调用时 cls 就是子类，自动跟着变。")
print("如果里面硬写 Pizza(...)，子类调用会退回父类 —— 这是个很隐蔽的 bug。")


# ---------------------------------------------------------------
# 3. 它们之间的真实区别
# ---------------------------------------------------------------
show("3. 区别不在「能不能调用」，而在「要不要隐式参数」")


class Weird:
    def normal(self):
        return "我是实例方法"

    @staticmethod
    def stat():
        return "我是静态方法"


w = Weird()
print("w.normal()  :", w.normal())
print("w.stat()    :", w.stat(), " <- 实例调静态方法也行，实例被忽略")
print("Weird.stat():", Weird.stat())
print()
print("普通方法用类直接调才是坑：Weird.normal() 会报缺少 self。")
try:
    Weird.normal()
except TypeError as e:
    print("  Weird.normal() ->", e)


# ---------------------------------------------------------------
# 4. 实战：用类方法做多种构造方式
# ---------------------------------------------------------------
show("4. 实战：一个类，好几种造法")


class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, text):
        y, m, d = (int(x) for x in text.split("-"))
        return cls(y, m, d)

    @classmethod
    def from_tuple(cls, t):
        return cls(*t)

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"


print(Date(2026, 9, 12))
print(Date.from_string("2026-09-12"))
print(Date.from_tuple((2026, 9, 12)))
print()
print("好处：调用方不用关心内部字段顺序，类自己知道怎么把自己拼出来。")


# ---------------------------------------------------------------
# 5. 什么时候用哪个
# ---------------------------------------------------------------
show("5. 选择标准")

print("要用 self 的数据             -> 实例方法")
print("要造对象 / 需要 cls 的多态    -> 类方法")
print("跟这个类相关，但两者都不需要  -> 静态方法")
print()
print("拿不定主意时：先写实例方法，等真的需要备用构造器再上类方法。")
print("静态方法堆得太多，通常说明那些函数根本不该放在这个类里。")


show("练习：去 99_exercises.py 做 ex3 ~ ex4")
