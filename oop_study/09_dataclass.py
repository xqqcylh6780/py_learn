# -*- coding: utf-8 -*-
"""
09 dataclass —— 写「数据容器类」的标准姿势
============================================

运行：  python 09_dataclass.py

它解决的是这个问题：一个类主要用来"装几个字段"，
却要手写一大堆 __init__ / __repr__ / __eq__。
"""

from dataclasses import dataclass, field, fields, asdict, astuple


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 先看不用的写法
# ---------------------------------------------------------------
show("1. 手写 vs dataclass")


class ManualEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"ManualEmployee(name={self.name!r}, salary={self.salary!r})"

    def __eq__(self, other):
        if not isinstance(other, ManualEmployee):
            return NotImplemented
        return (self.name, self.salary) == (other.name, other.salary)


@dataclass
class Employee:
    name: str
    salary: float


m = ManualEmployee("张三", 12000)
e = Employee("张三", 12000)

print("手写版   :", m)
print("dataclass:", e)
print("相等比较 :", Employee("张三", 12000) == Employee("张三", 12000))
print()
print("@dataclass 帮你生成了 __init__、__repr__、__eq__，你只管列字段。")
print("注意字段上的 str / float 只是「类型注解」，运行时不强制检查。")


# ---------------------------------------------------------------
# 2. 可变默认值必须用 default_factory
# ---------------------------------------------------------------
show("2. 坑：列表当默认值")

try:
    @dataclass
    class Bad:
        items: list = []
except ValueError as ex:
    print("直接写 = [] :", ex)


@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)     # 每个实例各建一个
    tags: set = field(default_factory=set)


t1 = Team("A组")
t2 = Team("B组")
t1.members.append("张三")
print()
print("t1 =", t1)
print("t2 =", t2, " <- 没有互相污染")
print()
print("原因和 01 节的类属性坑一模一样：可变对象被共享了。")
print("dataclass 干脆直接报错，逼你用 default_factory。")


# ---------------------------------------------------------------
# 3. frozen：不可变 + 可哈希
# ---------------------------------------------------------------
show("3. frozen=True —— 变成不可变、可哈希")


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(1, 2)
print("p =", p)

try:
    p.x = 99
except Exception as ex:
    print("改字段 :", type(ex).__name__, "-", ex)

print("能放进集合去重:", {Point(1, 2), Point(1, 2), Point(3, 4)})
print("能当字典键    :", {Point(1, 2): "起点"}[Point(1, 2)])
print()
print("对比：默认的 dataclass 因为有 __eq__ 没 __hash__，是不可哈希的。")


# ---------------------------------------------------------------
# 4. order：自动生成比较方法
# ---------------------------------------------------------------
show("4. order=True —— 能直接比大小、能排序")


@dataclass(order=True)
class Version:
    major: int
    minor: int
    label: str = field(compare=False)      # 不参与比较


vs = [Version(2, 0, "stable"), Version(1, 9, "beta"), Version(1, 10, "rc")]
for v in sorted(vs):
    print("   ", v)

print()
print("比较是按字段声明顺序来的：先比 major，相同再比 minor。")
print("label 写成 compare=False，就不参与比较了。")


# ---------------------------------------------------------------
# 5. __post_init__：需要派生字段或校验时
# ---------------------------------------------------------------
show("5. __post_init__ —— 构造完后的收尾")


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)        # 不给构造参数

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("长宽必须为正")
        self.area = self.width * self.height


r = Rectangle(3, 4)
print("r =", r)
print("area 不在构造参数里，是算出来的: init=False")

try:
    Rectangle(-1, 4)
except ValueError as ex:
    print("校验生效:", ex)


# ---------------------------------------------------------------
# 6. slots=True 与继承
# ---------------------------------------------------------------
show("6. slots=True 和继承")


@dataclass(slots=True)
class Fast:
    a: int
    b: int


print("slots=True 的实例:", Fast(1, 2))
try:
    Fast(1, 2).__dict__
except AttributeError:
    print("它没有 __dict__，和 08 节的 __slots__ 是同一回事")


@dataclass
class Base:
    a: int
    b: int = 10


@dataclass
class Derived(Base):
    c: int = 20


print()
print("Derived(1)     =", Derived(1))
print("Derived(1, 2, 3) =", Derived(1, 2, 3))
print("字段顺序       :", [f.name for f in fields(Derived)])
print()
print("坑：子类如果加一个「没有默认值」的字段，而父类字段有默认值，会报 TypeError。")
print("因为参数顺序上，无默认值的不能排在有默认值的后面。")


# ---------------------------------------------------------------
# 7. 导出与对比
# ---------------------------------------------------------------
show("7. 转字典 / 转元组 / 和 namedtuple 对比")

emp = Employee("李四", 9000)
print("asdict(emp)  =", asdict(emp))
print("astuple(emp) =", astuple(emp))

print()
print("和 namedtuple 怎么选：")
print("  namedtuple  不可变、支持解包、是元组、更省内存")
print("  dataclass   可变（除非 frozen）、能写方法、能继承、字段能带默认值")
print()
print("粗糙判断：只是「一条只读记录」用 namedtuple；")
print("要当正经对象用、要加方法、要可变，用 dataclass。")


show("练习：去 99_exercises.py 做 ex16")
