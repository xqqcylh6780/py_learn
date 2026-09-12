# -*- coding: utf-8 -*-
"""
10 Enum 枚举 —— 别再到处撒魔法字符串
======================================

运行：  python 10_Enum枚举.py

如果你在代码里写过 status = "pending" / status = "pendign" 这种，
枚举就是来救你的：它把「一组有限的合法取值」变成一个真正的类型。
"""

from enum import Enum, IntEnum, StrEnum, Flag, auto, unique


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 魔法字符串的痛
# ---------------------------------------------------------------
show("1. 为什么需要枚举")


def handle_bad(status):
    if status == "pendding":          # 拼错了，但没人会报错
        return "处理中"
    return "未知状态"


print("handle_bad('pending')  =", handle_bad("pending"), " <- 悄悄走错分支")
print()
print("字符串的问题：拼错不报错、IDE 补全不出来、合法取值散落在各处。")


# ---------------------------------------------------------------
# 2. 基本用法
# ---------------------------------------------------------------
show("2. 定义和使用")


class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"


print("成员        :", Status.PENDING)
print("名字 .name  :", Status.PENDING.name)
print("值   .value :", Status.PENDING.value)
print("类型        :", type(Status.PENDING))
print()
print("按值反查    :", Status("running"), " <- 用 Status(...) 从值找成员")
print("相等比较    :", Status.DONE == Status.DONE)
print("和字符串比  :", Status.DONE == "done", " <- False！枚举成员不等于它的值")
print()
print("想和字符串比，得显式写 Status.DONE.value == 'done'。")
print("这种「不自动相等」是故意的，逼你把类型用对。")


# ---------------------------------------------------------------
# 3. 不可变、可哈希
# ---------------------------------------------------------------
show("3. 不可变 + 可哈希")

try:
    Status.DONE.value = "finished"
except AttributeError as e:
    print("改成员的值 :", e)

print("能当字典键 :", {Status.PENDING: "排队中", Status.DONE: "已完成"}[Status.DONE])
print("能放集合   :", {Status.PENDING, Status.DONE, Status.PENDING})


# ---------------------------------------------------------------
# 4. 遍历、auto()、别名
# ---------------------------------------------------------------
show("4. 遍历、auto()、别名")

print("遍历所有成员：")
for s in Status:
    print(f"   {s.name:<8} = {s.value!r}")


class Priority(Enum):
    LOW = auto()                     # 自动给 1
    MEDIUM = auto()                  # 2
    HIGH = auto()                    # 3


print()
print("auto() 自动编号:", [(p.name, p.value) for p in Priority])


class Shape(Enum):
    SQUARE = 1
    BOX = 1                          # 值相同 -> 变成别名
    CIRCLE = 2


print()
print("别名现象：")
print("  Shape.BOX is Shape.SQUARE =", Shape.BOX is Shape.SQUARE)
print("  遍历时只出现一次           =", [x.name for x in Shape])
print("  但别名仍能查到             =", Shape.BOX.name)

try:
    @unique
    class Strict(Enum):
        A = 1
        B = 1
except ValueError as e:
    print()
    print("加 @unique 就会禁止别名:", e)


# ---------------------------------------------------------------
# 5. 几个常用变体
# ---------------------------------------------------------------
show("5. IntEnum / StrEnum / Flag")


class Code(IntEnum):
    OK = 200
    NOT_FOUND = 404


print("IntEnum 是 int 的子类：")
print("  Code.OK == 200      :", Code.OK == 200, " <- 这个为 True，方便和数字打交道")
print("  Code.OK + 1         :", Code.OK + 1)
print("  可以和普通数字混排  :", sorted([Code.NOT_FOUND, Code.OK]))


class Color(StrEnum):
    RED = "red"
    GREEN = "green"


print()
print("StrEnum 是 str 的子类：")
print("  Color.RED == 'red'  :", Color.RED == "red", " <- 为 True")
print("  直接能拼字符串      :", Color.RED.upper(), " ", f"颜色是 {Color.RED}")


class Perm(Flag):
    R = auto()
    W = auto()
    X = auto()
    ALL = R | W | X


print()
print("Flag 用来表示「可组合的开关」：")
p = Perm.R | Perm.W
print("  Perm.R | Perm.W  =", p)
print("  含 R 吗           :", Perm.R in p)
print("  含 X 吗           :", Perm.X in p)
print("  撤销 W 权限       :", p & ~Perm.W)


# ---------------------------------------------------------------
# 6. 什么时候用
# ---------------------------------------------------------------
show("6. 什么时候该上枚举")

print("该用：一组有限、固定的取值。状态机、订单状态、星期、权限位、错误码。")
print("别用：取值是开放的、来自外部数据且无法穷举的，那还是用字符串加校验。")
print()
print("最大的收益不是省字符串，是拼错时立刻 AttributeError，")
print("而且 IDE 能给你补全出所有合法取值。")


show("练习：去 99_exercises.py 做 ex17")
