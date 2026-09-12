# -*- coding: utf-8 -*-
"""
17 设计模式 —— 但用 Python 的方式写
=====================================

运行：  python 17_设计模式.py

重要前提：设计模式来自 Java/C++ 的世界，很多在 Python 里有更轻的解法。
照搬 Java 那套（一堆接口 + 一堆实现类）会让你写出很不 Python 的代码。
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 单例
# ---------------------------------------------------------------
show("1. 单例：保证全局只有一个实例")

# 最简单也最推荐的「单例」：模块级对象。Python 的模块天然只加载一次。
#   config.py
#       settings = {"debug": False}
#   用的时候 from config import settings  —— 拿到的永远是同一个字典
print("最推荐的写法：模块级变量。Python 的模块天然就是单例，")
print("不需要任何模式代码，from module import instance 拿到的永远是同一个。")


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name=""):
        self.name = name


a, b = Singleton("A"), Singleton("B")
print()
print("用 __new__ 实现: a is b ->", a is b, "| b.name =", b.name)
print("（注意 __init__ 又跑了一遍，把名字覆盖了 —— 06 节提过这个坑）")


# ---------------------------------------------------------------
# 2. 工厂
# ---------------------------------------------------------------
show("2. 工厂：把「造什么」和「怎么用」分开")


class JsonParser:
    def parse(self, text):
        return f"解析 JSON: {text}"


class CsvParser:
    def parse(self, text):
        return f"解析 CSV: {text}"


class XmlParser:
    def parse(self, text):
        return f"解析 XML: {text}"


_PARSERS = {"json": JsonParser, "csv": CsvParser, "xml": XmlParser}


def make_parser(kind):
    cls = _PARSERS.get(kind)
    if cls is None:
        raise ValueError(f"不支持的格式: {kind}")
    return cls()


for kind in ["json", "csv"]:
    print("   ", make_parser(kind).parse("数据"))

print()
print("调用方只管说「我要 json 解析器」，不关心类名是什么、怎么构造。")
print("要加新格式，只在字典里加一行，别处不用动。")


# ---------------------------------------------------------------
# 3. 策略模式：Python 里就是「传函数」
# ---------------------------------------------------------------
show("3. 策略：在 Java 里要写接口，在 Python 里直接传函数")


def price_normal(amount):
    return amount


def price_vip(amount):
    return amount * 0.8


def price_discount(amount):
    return amount - 10 if amount > 100 else amount


class Checkout:
    def __init__(self, strategy=price_normal):
        self.strategy = strategy            # 策略就是一个可调用对象

    def total(self, amount):
        return self.strategy(amount)


for name, strategy in [("原价", price_normal), ("VIP", price_vip), ("满减", price_discount)]:
    print(f"   {name:<4} 200 元 -> {Checkout(strategy).total(200):.2f}")

print()
print("在 Java 里这里要定义 Strategy 接口 + 三个实现类；")
print("Python 里函数就是一等公民，传个函数就完事了。")
print("再进一步：需要带参数时用 functools.partial，需要带状态时用 __call__ 对象（05 节）。")


# ---------------------------------------------------------------
# 4. 观察者
# ---------------------------------------------------------------
show("4. 观察者：一个变了，通知所有人")


class EventBus:
    def __init__(self):
        self._listeners = []                # 存的是「可调用对象」，不是接口

    def subscribe(self, fn):
        self._listeners.append(fn)
        return fn                           # 方便当装饰器用

    def emit(self, event):
        for fn in self._listeners:
            fn(event)


bus = EventBus()


@bus.subscribe                            # 装饰器顺手就注册了
def log_event(event):
    print(f"   [日志] 收到事件: {event}")


@bus.subscribe
def send_mail(event):
    print(f"   [邮件] 事件 {event} 通知管理员")


bus.emit("user_registered")
print()
print("关键点：EventBus 不认识任何具体的处理函数，只要求「能被调用」。")
print("这就是 11 节讲的鸭子类型/协议，比定义 Observer 接口灵活得多。")


# ---------------------------------------------------------------
# 5. 装饰器模式
# ---------------------------------------------------------------
show("5. 装饰器：不改原函数，往外包一层")

import functools
import time


def retry(times=3, delay=0.01):
    def decorator(func):
        @functools.wraps(func)              # 保留原函数的 __name__ 等元信息
        def wrapper(*args, **kwargs):
            last = None
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last = e
                    print(f"   第 {i + 1} 次失败: {e}，重试中")
                    time.sleep(delay)
            raise last
        return wrapper
    return decorator


calls = {"n": 0}


@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("网络抖了一下")
    return "第三次成功了"


print("   ", flaky())
print()
print("注意 points：")
print("  - functools.wraps 一定要加，否则被装饰函数的名字会变成 wrapper")
print("  - 带参数的装饰器要套三层（装饰器工厂 -> 装饰器 -> wrapper）")


# ---------------------------------------------------------------
# 6. 别硬套模式
# ---------------------------------------------------------------
show("6. 什么时候别套模式")

print("Python 里被语言特性吃掉了一部分的模式：")
print("  策略 / 命令   -> 直接传函数")
print("  单例          -> 模块级变量")
print("  迭代器        -> 生成器")
print("  装饰器        -> @语法")
print("  适配器        -> __getattr__ 转发")
print()
print("判断标准：模式是用来给「反复出现的结构」起名字的，")
print("不是用来显得高级的。没有那个痛点，就别引入那层抽象。")


show("练习：去 99_exercises.py 做 ex25")
