# -*- coding: utf-8 -*-
"""
14 元类与类创建 —— 类是对象，那类是谁造的？
=============================================

运行：  python 14_元类与类创建.py

在 01 节我们看到 type(Dog) 是 type。
既然类也是对象，那它一定是被某个东西造出来的 —— 那就是元类。
元类 = 创建类的类。
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 用 type() 动态造类
# ---------------------------------------------------------------
show("1. class 语句其实是在调用 type()")


class Normal:
    x = 1

    def hello(self):
        return "hi"


# 上面这段完全等价于：
Dynamic = type("Dynamic", (), {"x": 1, "hello": lambda self: "hi"})

print("Normal()      =", Normal().hello(), "| 类型:", type(Normal()).__name__)
print("Dynamic()     =", Dynamic().hello(), "| 类型:", type(Dynamic()).__name__)
print("名字          :", Normal.__name__, "vs", Dynamic.__name__)
print()
print("type(名字, 父类元组, 命名空间字典) —— 这就是 class 语句背后的三件事。")


# 动态造类的真实用途：从配置生成类
fields = {"name": "", "age": 0}
ConfigClass = type("Config", (), fields)
inst = ConfigClass()
inst.name = "从配置生成的"
print("动态生成的类实例:", vars(inst))


# ---------------------------------------------------------------
# 2. 写一个元类
# ---------------------------------------------------------------
show("2. 元类：拦截「类的创建」")


class AutoRepr(type):
    def __new__(mcs, name, bases, namespace):
        print(f"   [元类] 正在创建类 {name}，字段: {list(namespace)}")
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.created_by_meta = True


class Product(metaclass=AutoRepr):
    def __init__(self, name):
        self.name = name


class Order(metaclass=AutoRepr):
    pass


print()
print("Product.created_by_meta =", Product.created_by_meta)
print("Order.created_by_meta   =", Order.created_by_meta)
print()
print("注意：元类的方法里第一个参数习惯叫 mcs（metaclass），")
print("它收到的是「类的命名空间」，也就是类里定义的那些东西。")


# ---------------------------------------------------------------
# 3. 元类的经典用途：自动注册
# ---------------------------------------------------------------
show("3. 实战：插件自动注册")


class PluginMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:                          # 跳过基类自己
            mcs.registry[name] = cls
        return cls


class Plugin(metaclass=PluginMeta):
    pass


class JsonPlugin(Plugin):
    def handle(self):
        return "处理 JSON"


class CsvPlugin(Plugin):
    def handle(self):
        return "处理 CSV"


print("注册表:", PluginMeta.registry)
print("用名字拿类  :", PluginMeta.registry["JsonPlugin"]().handle())
print()
print("好处：加新插件只要定义一个类，注册表自动更新，不用手改任何列表。")


# ---------------------------------------------------------------
# 4. 更简单的替代：__init_subclass__
# ---------------------------------------------------------------
show("4. 大多数时候，你其实想要 __init_subclass__")


class Base:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)     # 别忘了转发 kwargs
        Base.registry[cls.__name__] = cls
        print(f"   [__init_subclass__] 注册了 {cls.__name__}")


class Dog(Base):
    pass


class Cat(Base):
    pass


print()
print("注册表:", Base.registry)
print()
print("对比一下：")
print("  元类              能改变类的创建过程，威力大，也更容易把人绕晕")
print("  __init_subclass__ 只能在子类被创建后做点事，但写起来简单太多")
print()
print("经验法则：能用 __init_subclass__ 解决的，就别上元类。")


# ---------------------------------------------------------------
# 5. 元类冲突的坑
# ---------------------------------------------------------------
show("5. 坑：父类的元类必须兼容")


class A(metaclass=AutoRepr):
    pass


class B(metaclass=PluginMeta):
    pass


try:
    class C(A, B):                     # 两个不同的元类
        pass
except TypeError as e:
    print("   ", str(e)[:90], "...")

print()
print("所以元类是有代价的：一旦用了，别人继承你的类时也得跟着受约束。")


# ---------------------------------------------------------------
# 6. 什么时候真的需要元类
# ---------------------------------------------------------------
show("6. 什么时候真的该上元类")

print("现实中的答案：几乎不需要。")
print()
print("框架层需要（Django 的 Model、SQLAlchemy 的声明式映射等），")
print("因为它们要在类定义时读取字段、生成表结构。")
print()
print("业务代码里想用元类时，先问自己三个问题：")
print("  1. 用装饰器能解决吗？")
print("  2. 用 __init_subclass__ 能解决吗？")
print("  3. 用描述符能解决吗？")
print()
print("三个都否，再考虑元类。这不是保守，是因为元类的调试成本真的很高。")


show("练习：去 99_exercises.py 做 ex22")
