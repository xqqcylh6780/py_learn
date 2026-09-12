# -*- coding: utf-8 -*-
"""
07 描述符 —— property 背后的那个机制
======================================

运行：  python 07_描述符.py

描述符是 Python 属性系统的底层引擎。你天天用的 property、classmethod、
staticmethod、甚至函数本身，全都是描述符。

规则很简单：一个类只要实现了下面三个方法中的任意一个，
它的实例就是描述符；把这个实例放在另一个类的类属性位置上，
就能拦截对那个属性的访问。
    __get__(self, obj, objtype=None)
    __set__(self, obj, value)
    __delete__(self, obj)
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 最小描述符：观察它什么时候被触发
# ---------------------------------------------------------------
show("1. 最小描述符")


class Verbose:
    def __get__(self, obj, objtype=None):
        print(f"   __get__ 被调用 (obj={obj}, objtype={objtype.__name__ if objtype else None})")
        return "取到的值"

    def __set__(self, obj, value):
        print(f"   __set__ 被调用, value={value!r}")
        obj.__dict__["_hidden"] = value


class Demo:
    x = Verbose()                    # 描述符实例挂在类属性上

    def __init__(self):
        self.y = 1


d = Demo()
print("读取 Demo.x  (类访问):")
_ = Demo.x
print("读取 d.x     (实例访问):")
_ = d.x
print("写入 d.x = 5 :")
d.x = 5

print()
print("注意 objtype 参数：obj 为 None 表示是通过类访问的，这时一般返回描述符自己。")


# ---------------------------------------------------------------
# 2. 属性查找优先级
# ---------------------------------------------------------------
show("2. 属性查找的完整优先级")

print("obj.attr 的查找顺序：")
print("  1. 类里的「数据描述符」   （有 __set__ 或 __delete__）")
print("  2. 实例的 __dict__")
print("  3. 类里的「非数据描述符」 （只有 __get__）")
print("  4. 类属性 / 基类")
print()
print("记住这句话就够了：数据描述符能压过实例字典，非数据描述符不行。")
print("这就是为什么 property（数据描述符）能接管赋值，")
print("而普通方法（非数据描述符）可以被实例属性覆盖掉。")


# ---------------------------------------------------------------
# 3. 实战：可复用的类型校验描述符
# ---------------------------------------------------------------
show("3. 实战：一个描述符，多处复用")


class Positive:
    def __set_name__(self, owner, name):
        """类创建时自动调用，告诉你自己被赋给了哪个属性名。"""
        self.public = name
        self.private = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                      # 通过类访问，返回描述符本身
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.public} 必须是数字")
        if value <= 0:
            raise ValueError(f"{self.public} 必须为正数，收到 {value}")
        setattr(obj, self.private, value)

    def __repr__(self):
        return f"Positive({self.public})"


class Order:
    qty = Positive()                     # 声明一次，两个字段都受益
    price = Positive()

    def __init__(self, qty, price):
        self.qty = qty                   # 走描述符的 __set__
        self.price = price

    def total(self):
        return self.qty * self.price


o = Order(3, 9.9)
print("Order(3, 9.9)      =", o.__dict__)
print("o.qty              =", o.qty)
print("o.total()          =", round(o.total(), 2))

for bad in (0, -5):
    try:
        o.qty = bad
    except ValueError as e:
        print("设置非法值         :", e)

print()
print("__set_name__ 是 Python 3.6+ 才有的，它让我们不用手写 Positive('qty') 这种重复名字。")
print("好处：校验逻辑写一遍，多个类、多个字段都能用 —— 这是 property 做不到的。")


# ---------------------------------------------------------------
# 4. property 就是描述符
# ---------------------------------------------------------------
show("4. 证据：property 本身就是描述符")

print("property 的类型      :", type(property(lambda self: 1)))
print("有没有 __get__       :", hasattr(property, "__get__"))
print("有没有 __set__       :", hasattr(property, "__set__"))
print("是数据描述符吗        :", hasattr(property, "__set__") or hasattr(property, "__delete__"))
print()
print("所以 03 节讲的 property 能拦截赋值，原理就在这里。")
print("区别只是：property 的读写函数是「跟着类走的」，")
print("而描述符把逻辑封装成了可复用的类。")


show("练习：去 99_exercises.py 做 ex13 ~ ex14")
