# -*- coding: utf-8 -*-
"""
面向对象练习册 —— 30 道题，自动判分
======================================

运行：  python 99_exercises.py

一开始全是 [FAIL] 是正常的，那就是你的待办清单。
把 TODO 填掉再跑，看通过数往上涨。

卡住了翻到本文件最底下的「参考答案」，但建议先自己想 5 分钟。
"""

import copy
import functools
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Generic, Protocol, TypeVar, runtime_checkable

_checks = []


def check(fn):
    _checks.append(fn)
    return fn


# =================================================================
# 01 类与对象
# =================================================================

@check
def ex1_class_and_object():
    """定义 Book：__init__(title, author, pages)，并有类属性 category = "图书"。"""

    class Book:
        category = "图书"

        def __init__(self, title, author, pages):
            pass                       # TODO

    b = Book("Python编程", "张三", 300)
    assert b.title == "Python编程"
    assert b.author == "张三"
    assert b.pages == 300
    assert Book.category == "图书"
    assert b.category == "图书", "实例应该能读到类属性"


@check
def ex2_instance_attribute_isolation():
    """让每个 Library 都有自己独立的 books 列表（别被类属性共享）。"""

    class Library:
        books = []

        def __init__(self, name):
            self.name = name
            pass                       # TODO

    a, b = Library("A馆"), Library("B馆")
    a.books.append("书1")
    assert a.books == ["书1"]
    assert b.books == [], f"b 不该被影响，实际是 {b.books}"


# =================================================================
# 02 方法三兄弟
# =================================================================

@check
def ex3_classmethod_factory():
    """用类方法给 Temperature 加一个从华氏度构造的入口。"""

    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius

        @classmethod
        def from_fahrenheit(cls, f):
            return None                # TODO

    t = Temperature.from_fahrenheit(212)
    assert round(t.celsius, 6) == 100
    assert isinstance(t, Temperature)


@check
def ex4_staticmethod():
    """写一个静态方法判断字符串是不是邮箱格式（够用就行，不用严格）。"""

    class Validator:
        @staticmethod
        def is_email(text):
            return None                # TODO：含 @、@ 两边都非空、后面有 .

    assert Validator.is_email("a@b.com") is True
    assert Validator.is_email("nope") is False
    assert Validator.is_email("@b.com") is False
    assert Validator.is_email("a@bcom") is False


# =================================================================
# 03 封装与 property
# =================================================================

@check
def ex5_property_validation():
    """用 property 让 Person.age 只能是非负整数。"""

    class Person:
        def __init__(self, age):
            self.age = age
        # TODO: 加 property（getter + setter）

    p = Person(20)
    assert p.age == 20

    for bad in (-1, -100):
        try:
            p.age = bad
        except ValueError:
            pass
        else:
            raise AssertionError(f"设置 {bad} 应该抛 ValueError")

    try:
        p.age = "二十"
    except (TypeError, ValueError):
        pass
    else:
        raise AssertionError("非整数也该拒绝")


@check
def ex6_readonly_computed_property():
    """给 Rectangle 加两个只读的计算属性：area 和 perimeter。"""

    class Rectangle:
        def __init__(self, w, h):
            self.w, self.h = w, h
        # TODO

    r = Rectangle(3, 4)
    assert r.area == 12
    assert r.perimeter == 14

    try:
        r.area = 100
    except AttributeError:
        pass
    else:
        raise AssertionError("area 应该是只读的")


# =================================================================
# 04 继承与 MRO
# =================================================================

@check
def ex7_inheritance_super():
    """用 super() 补全子类。"""

    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "..."

    class Dog(Animal):
        def __init__(self, name, breed):
            pass                       # TODO：用 super() 初始化 name，并记住 breed

        def speak(self):
            return None                # TODO：返回 "汪汪"

    d = Dog("旺财", "柴犬")
    assert d.name == "旺财"
    assert d.breed == "柴犬"
    assert d.speak() == "汪汪"
    assert isinstance(d, Animal)


@check
def ex8_predict_mro():
    """别急着写代码 —— 先猜，再让答案来纠正你。"""

    class A:
        def who(self):
            return ["A"]

    class B(A):
        def who(self):
            return ["B"] + super().who()

    class C(A):
        def who(self):
            return ["C"] + super().who()

    class D(B, C):
        def who(self):
            return ["D"] + super().who()

    mro_names = None                   # TODO：你猜的类名顺序
    who_result = None                  # TODO：你猜的 D().who()

    real_mro = [c.__name__ for c in D.__mro__]
    assert mro_names == real_mro, f"MRO 猜错了，实际是 {real_mro}"
    assert who_result == D().who(), f"who() 猜错了，实际是 {D().who()}"


# =================================================================
# 05 魔术方法
# =================================================================

@check
def ex9_repr_eq_hash():
    """给 Money 补上 __repr__、__eq__、__hash__。"""

    class Money:
        def __init__(self, amount, currency="CNY"):
            self.amount, self.currency = amount, currency
        # TODO

    assert repr(Money(100)) == "Money(100, 'CNY')", f"实际是 {repr(Money(100))}"
    assert Money(100) == Money(100)
    assert Money(100) != Money(100, "USD")
    assert len({Money(100), Money(100), Money(50)}) == 2, "必须可哈希才能去重"


@check
def ex10_container_protocol():
    """给 Bag 补上容器协议，让它用起来像个列表。"""

    class Bag:
        def __init__(self, items):
            self.items = list(items)
        # TODO: __len__ / __contains__ / __getitem__ / __iter__

    bag = Bag(["a", "b", "c"])
    assert len(bag) == 3
    assert "b" in bag
    assert "z" not in bag
    assert bag[0] == "a"
    assert list(bag) == ["a", "b", "c"]
    assert [x for x in bag] == ["a", "b", "c"]


# =================================================================
# 06 生命周期与拷贝
# =================================================================

@check
def ex11_singleton():
    """用 __new__ 实现单例。"""

    class Singleton:
        _instance = None

        def __new__(cls, *args, **kwargs):
            return None                # TODO

    a = Singleton()
    assert isinstance(a, Singleton), "应该返回 Singleton 实例，而不是 None"
    assert a is Singleton()
    assert a is Singleton()


@check
def ex12_deep_copy():
    """在嵌套结构上使用深拷贝。"""

    original = {"tags": ["a", "b"], "meta": {"n": 1}}

    deep = None                        # TODO
    assert deep is not None, "还没开始写"
    deep["tags"].append("c")
    deep["meta"]["n"] = 999

    assert original["tags"] == ["a", "b"], "原对象的列表被改到了，说明不是深拷贝"
    assert original["meta"]["n"] == 1, "原对象的字典被改到了"


# =================================================================
# 07 描述符
# =================================================================

@check
def ex13_descriptor_validation():
    """写一个描述符，保证字段必须是正数。"""

    class Positive:
        # TODO: 实现 __set_name__ / __get__ / __set__
        pass

    class Order:
        qty = Positive()

        def __init__(self, qty):
            self.qty = qty

    o = Order(5)
    assert o.qty == 5
    assert o.__dict__.get("_qty") == 5, "值应该存在实例上，键名用 _qty"

    try:
        Order(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("负数应该抛 ValueError")

    try:
        Order(0)
    except ValueError:
        pass
    else:
        raise AssertionError("0 也应该被拒绝")


@check
def ex14_cached_property():
    """用 property 实现「只算一次」的缓存属性。"""

    class Heavy:
        def __init__(self):
            self._cache = None
            self.compute_count = 0

        @property
        def result(self):
            return None                # TODO：第一次算 42 并缓存，之后直接返回缓存

    h = Heavy()
    assert h.result == 42
    assert h.result == 42
    assert h.result == 42
    assert h.compute_count == 1, f"不该重复计算，实际算了 {h.compute_count} 次"


# =================================================================
# 08 __slots__
# =================================================================

@check
def ex15_slots():
    """给 Point 加上 __slots__，只允许 x 和 y。"""

    class Point:
        # TODO
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __repr__(self):
            return f"Point({self.x}, {self.y})"

    p = Point(1, 2)
    assert repr(p) == "Point(1, 2)"
    assert not hasattr(p, "__dict__"), "用了 __slots__ 就不该有 __dict__"

    try:
        p.z = 3
    except AttributeError:
        pass
    else:
        raise AssertionError("不该允许加新属性")


# =================================================================
# 09 dataclass
# =================================================================

@check
def ex16_dataclass():
    """用 @dataclass 定义 Product(name, price, tags)。"""
    # TODO

    p1 = Product("苹果", 3.5)
    p2 = Product("香蕉", 2.0)
    p1.tags.append("水果")

    assert p1.name == "苹果"
    assert p1.price == 3.5
    assert p1.tags == ["水果"]
    assert p2.tags == [], "两个实例的 tags 不能共享，用 default_factory"
    assert Product("x", 1.0) == Product("x", 1.0), "dataclass 应该自动生成 __eq__"
    assert "Product" in repr(p1), "应该自动生成 __repr__"


# =================================================================
# 10 Enum
# =================================================================

@check
def ex17_enum():
    """定义订单状态枚举 OrderStatus。"""
    # TODO

    assert OrderStatus.PENDING.value == "pending"
    assert OrderStatus.RUNNING.value == "running"
    assert OrderStatus.DONE.value == "done"
    assert OrderStatus("done") is OrderStatus.DONE
    assert OrderStatus.PENDING.name == "PENDING"
    assert len(list(OrderStatus)) == 3


# =================================================================
# 11 抽象基类与协议
# =================================================================

@check
def ex18_abstract_base_class():
    """用 ABC 定义 Shape（抽象方法 area），再实现 Square。"""
    # TODO

    assert Square(2).area() == 4

    try:
        Shape()
    except TypeError:
        pass
    else:
        raise AssertionError("抽象类不该能实例化")

    class Incomplete(Shape):
        pass

    try:
        Incomplete()
    except TypeError:
        pass
    else:
        raise AssertionError("没实现抽象方法的子类也不该能实例化")


@check
def ex19_protocol():
    """用 Protocol 定义 Speaker（有 speak 方法），让没继承它的类也能通过。"""
    # TODO

    class Dog:
        def speak(self):
            return "汪"

    class Stone:
        pass

    assert isinstance(Dog(), Speaker)
    assert not isinstance(Stone(), Speaker)
    assert issubclass(Dog, Speaker)


# =================================================================
# 12 运算符重载
# =================================================================

@check
def ex20_operator_overload():
    """给 Money 实现加法，但不同币种不能相加。"""

    class Money:
        def __init__(self, amount, currency="CNY"):
            self.amount, self.currency = amount, currency
        # TODO: __add__ / __repr__

    total = Money(10) + Money(5)
    assert total.amount == 15
    assert total.currency == "CNY"

    try:
        Money(10) + Money(5, "USD")
    except (TypeError, ValueError):
        pass
    else:
        raise AssertionError("不同币种不该能相加")


# =================================================================
# 13 反射
# =================================================================

@check
def ex21_reflection():
    """实现 get_field：安全地按名字取值。"""

    def get_field(obj, name, default=None):
        return None                    # TODO：提示 getattr 的第三个参数

    class A:
        x = 1

    a = A()
    assert get_field(a, "x") == 1
    assert get_field(a, "nope") is None
    assert get_field(a, "nope", 0) == 0


# =================================================================
# 14 元类 / __init_subclass__
# =================================================================

@check
def ex22_auto_register():
    """用 __init_subclass__ 实现子类自动注册。"""

    class Base:
        registry = {}
        # TODO

    class Alpha(Base):
        pass

    class Beta(Base):
        pass

    assert set(Base.registry) == {"Alpha", "Beta"}, f"实际是 {set(Base.registry)}"
    assert Base.registry["Alpha"] is Alpha
    assert "Base" not in Base.registry, "基类自己不该被注册"


# =================================================================
# 15 上下文管理器
# =================================================================

@check
def ex23_context_manager():
    """写一个计时用的上下文管理器。"""

    class Timer:
        # TODO: __enter__ 返回 self 并记下开始时间；__exit__ 设置 self.elapsed
        pass

    with Timer() as t:
        time.sleep(0.02)

    assert hasattr(t, "elapsed"), "退出后应该有 elapsed"
    assert t.elapsed >= 0.02, f"耗时算错了: {t.elapsed}"


# =================================================================
# 16 生成器
# =================================================================

@check
def ex24_generator():
    """写一个生成器函数，产出前 n 个斐波那契数（从 0 开始）。"""

    def fibonacci(n):
        return None                    # TODO：记得用 yield

    assert list(fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8]
    assert list(fibonacci(1)) == [0]
    assert list(fibonacci(0)) == []


# =================================================================
# 17 设计模式
# =================================================================

@check
def ex25_decorator():
    """写一个装饰器，统计函数被调用了多少次，存在 func.calls 上。"""

    def count_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return None                # TODO
        return wrapper

    @count_calls
    def hello():
        return "hi"

    assert hello() == "hi"
    assert hello() == "hi"
    assert hello() == "hi"
    assert hello.calls == 3, f"计数器不对: {getattr(hello, 'calls', None)}"
    assert hello.__name__ == "hello", "别忘了 functools.wraps"


# =================================================================
# 18 类型注解与泛型
# =================================================================

@check
def ex26_generic_box():
    """实现一个泛型容器 Box[T]。"""

    T = TypeVar("T")

    class Box(Generic[T]):
        def __init__(self):
            self._value = None

        def put(self, value):
            pass                       # TODO

        def get(self):
            return None                # TODO

    b = Box()
    b.put(123)
    assert b.get() == 123
    b.put("文本")
    assert b.get() == "文本"
    b.put(None)
    assert b.get() is None


# =================================================================
# 19 装饰器深入
# =================================================================

@check
def ex27_decorator_with_args():
    """写一个带参数的装饰器 repeat(n)：重复调用 n 次，返回最后一次的结果。"""

    def repeat(times):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return None                # TODO
            return wrapper
        return decorator

    calls = []

    @repeat(times=3)
    def record(x):
        calls.append(x)
        return x * 10

    assert record(5) == 50
    assert calls == [5, 5, 5], f"应该调 3 次，实际调用记录是 {calls}"
    assert record.__name__ == "record", "别忘了 functools.wraps"


@check
def ex28_decorator_order():
    """先猜：下面 target() 的执行顺序是什么？猜完让代码告诉你答案。"""

    order = []

    def first(func):
        @functools.wraps(func)
        def w(*a, **k):
            order.append("进入 first")
            r = func(*a, **k)
            order.append("离开 first")
            return r
        return w

    def second(func):
        @functools.wraps(func)
        def w(*a, **k):
            order.append("进入 second")
            r = func(*a, **k)
            order.append("离开 second")
            return r
        return w

    @first
    @second
    def target():
        order.append("本体")

    predicted = None                   # TODO：你猜的顺序，字符串列表

    target()
    assert predicted == order, f"猜错了，实际顺序是 {order}"


# =================================================================
# 20 迭代器深入
# =================================================================

@check
def ex29_reusable_iterator():
    """写一个「可以反复遍历」的可迭代类。"""

    class RepeatableRange:
        def __init__(self, n):
            self.n = n
        # TODO: 实现 __iter__，注意每次都要返回一个全新的迭代器

    r = RepeatableRange(3)
    assert list(r) == [0, 1, 2]
    assert list(r) == [0, 1, 2], "第二次遍历变空，说明 __iter__ 返回了 self"
    assert not hasattr(RepeatableRange(3), "__next__"), "可迭代对象本身不该是迭代器"


@check
def ex30_generator_pipeline():
    """用生成器把「读 -> 筛 -> 转换」串成流水线。"""

    lines = ["1", "2", "3", "4", "5", "6"]

    def read_numbers(lines):
        return None                    # TODO：yield 出 int

    def only_even(nums):
        return None                    # TODO：只 yield 偶数

    def doubled(nums):
        return None                    # TODO：yield 出两倍

    assert hasattr(read_numbers(lines), "__next__"), "要用 yield 写生成器，不是返回列表"

    result = list(doubled(only_even(read_numbers(lines))))
    assert result == [4, 8, 12], f"实际是 {result}"


# =================================================================
# 判分器
# =================================================================

def run_all():
    print("=" * 62)
    print("面向对象练习册")
    print("=" * 62)
    passed = 0
    for fn in _checks:
        name = f"{fn.__name__:<34}"
        try:
            fn()
        except AssertionError as e:
            print(f"[FAIL] {name} {e or '断言没通过'}")
        except Exception as e:
            print(f"[ERR ] {name} {type(e).__name__}: {e}")
        else:
            passed += 1
            print(f"[ OK ] {name}")
    total = len(_checks)
    print("-" * 62)
    print(f"通过 {passed}/{total}")
    if passed == total:
        print("全书通关。到这一步，Python 的面向对象基本没有盲区了。")


if __name__ == "__main__":
    run_all()


# =================================================================
# 参考答案（建议先自己写）
# =================================================================
"""
ex1_class_and_object
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

ex2_instance_attribute_isolation
    def __init__(self, name):
        self.name = name
        self.books = []                # 在 __init__ 里建，每个实例各一份

ex3_classmethod_factory
    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

ex4_staticmethod
    @staticmethod
    def is_email(text):
        if text.count("@") != 1:
            return False
        local, _, domain = text.partition("@")
        return bool(local) and "." in domain and not domain.startswith(".") \\
               and not domain.endswith(".")

ex5_property_validation
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("年龄必须是整数")
        if value < 0:
            raise ValueError("年龄不能为负")
        self._age = value

ex6_readonly_computed_property
    @property
    def area(self):
        return self.w * self.h

    @property
    def perimeter(self):
        return 2 * (self.w + self.h)

ex7_inheritance_super
    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name)
            self.breed = breed

        def speak(self):
            return "汪汪"

ex8_predict_mro
    mro_names  = ["D", "B", "C", "A", "object"]
    who_result = ["D", "B", "C", "A"]
    # 要点：super() 走的是 MRO 的下一个，B 的下一个是 C，不是 A

ex9_repr_eq_hash
    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self.amount, self.currency) == (other.amount, other.currency)

    def __hash__(self):
        return hash((self.amount, self.currency))

ex10_container_protocol
    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, i):
        return self.items[i]

    def __iter__(self):
        return iter(self.items)

ex11_singleton
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

ex12_deep_copy
    deep = copy.deepcopy(original)

ex13_descriptor_validation
    class Positive:
        def __set_name__(self, owner, name):
            self.private = "_" + name

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            return getattr(obj, self.private)

        def __set__(self, obj, value):
            if value <= 0:
                raise ValueError("必须是正数")
            setattr(obj, self.private, value)

ex14_cached_property
    @property
    def result(self):
        if self._cache is None:
            self.compute_count += 1
            self._cache = 42
        return self._cache

ex15_slots
    class Point:
        __slots__ = ("x", "y")

ex16_dataclass
    @dataclass
    class Product:
        name: str
        price: float
        tags: list = field(default_factory=list)

ex17_enum
    class OrderStatus(Enum):
        PENDING = "pending"
        RUNNING = "running"
        DONE = "done"

ex18_abstract_base_class
    class Shape(ABC):
        @abstractmethod
        def area(self): ...

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

ex19_protocol
    @runtime_checkable
    class Speaker(Protocol):
        def speak(self) -> str: ...

ex20_operator_overload
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"币种不同: {self.currency} vs {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

ex21_reflection
    def get_field(obj, name, default=None):
        return getattr(obj, name, default)

ex22_auto_register
    class Base:
        registry = {}

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            Base.registry[cls.__name__] = cls

ex23_context_manager
    class Timer:
        def __enter__(self):
            self.start = time.perf_counter()
            return self

        def __exit__(self, exc_type, exc_value, tb):
            self.elapsed = time.perf_counter() - self.start
            return False

ex24_generator
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

ex25_decorator
    def count_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper

ex26_generic_box
    def put(self, value):
        self._value = value

    def get(self):
        return self._value

ex27_decorator_with_args
    def repeat(times):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = None
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    # 注意三层：repeat 收参数 -> decorator 收函数 -> wrapper 被调用

ex28_decorator_order
    predicted = ["进入 first", "进入 second", "本体", "离开 second", "离开 first"]
    # @first 在最外层，进入时从外往里，退出时从里往外
    # 展开就是 first(second(target))

ex29_reusable_iterator
    def __iter__(self):
        return iter(range(self.n))
    # 关键：返回「新的」迭代器，而不是 self。
    # 也可以写成 return (i for i in range(self.n))

ex30_generator_pipeline
    def read_numbers(lines):
        for line in lines:
            yield int(line)

    def only_even(nums):
        for n in nums:
            if n % 2 == 0:
                yield n

    def doubled(nums):
        for n in nums:
            yield n * 2
    # 三环各管一件事，中间不产生临时列表
"""
