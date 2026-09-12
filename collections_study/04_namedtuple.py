# -*- coding: utf-8 -*-
"""
collections.namedtuple —— 给元组的每个位置起个名字
====================================================

运行：  python 04_namedtuple.py
练习：  python 99_exercises.py   （第 4 节）

一句话理解：它就是元组，只是你可以写 point.x 而不用写 point[0]。
本质没变（依然不可变、依然能解包、依然能比较大小），只是更好读。
"""

from collections import namedtuple


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 痛点：一堆 [0] [1] 谁也看不懂
# ---------------------------------------------------------------
show("1. 先看不用的写法")

raw = ("张三", 28, "北京")

print("普通元组 :", raw)
print("读名字   :", raw[0], " <- 不看代码没人知道 0 是名字还是 ID")

Person = namedtuple("Person", ["name", "age", "city"])
p = Person("张三", 28, "北京")

print("namedtuple:", p)
print("读名字   :", p.name, "  <- 一眼就懂")
print("也能用下标:", p[0], "  <- 毕竟是元组，老写法照样能用")


# ---------------------------------------------------------------
# 2. 它真的还是个元组
# ---------------------------------------------------------------
show("2. 它依然是元组：解包、比较、当字典键都行")

name, age, city = p                    # 解包，和普通元组一样
print("解包      :", name, age, city)

print("等于普通元组吗:", p == ("张三", 28, "北京"))
print("长度        :", len(p))
print("下标切片    :", p[1:])

# namedtuple 本身不可变；当所有字段值都可哈希时，实例也可哈希，能当字典键
ages = {Person("李四", 30, "上海"): "VIP"}
print("当字典键    :", ages[Person("李四", 30, "上海")])

# 因为不可变，想改一个字段只能造一个新的
try:
    p.age = 29
except AttributeError as e:
    print("改字段会报错:", e)


# ---------------------------------------------------------------
# 3. 四个下划线开头的工具方法
# ---------------------------------------------------------------
show("3. _fields / _asdict / _replace / _make")

print("_fields      :", Person._fields, " 字段名元组")
print("_asdict()    :", p._asdict(), "  转成字典")

# _replace：复制一份并改动指定字段（原名很贴切，它返回新对象）
p2 = p._replace(age=29)
print("_replace     :", p2, " <- 原来的 p 没变:", p)

# _make：从任意序列造一个（等价于 Person(*seq)）
p3 = Person._make(["王五", 35, "广州"])
print("_make        :", p3)

# 默认值：Python 3.7+ 支持 defaults
Point = namedtuple("Point", ["x", "y", "z"], defaults=[0])
print()
print("默认值 defaults=[0]:")
print("  Point(1, 2)    =", Point(1, 2), " z 自动补 0")
print("  Point(1, 2, 3) =", Point(1, 2, 3))
print("  _field_defaults=", Point._field_defaults)


# ---------------------------------------------------------------
# 4. 实战：把 CSV 里的行变成对象
# ---------------------------------------------------------------
show("4. 实战：CSV 行 -> 好读的记录")

import csv
import io

csv_text = """name,price,qty
apple,3.5,10
banana,2.0,5
cherry,12.0,2
"""

Item = namedtuple("Item", ["name", "price", "qty"])

reader = csv.DictReader(io.StringIO(csv_text))
items = [Item(row["name"], float(row["price"]), int(row["qty"])) for row in reader]

total = 0.0
for it in items:
    subtotal = it.price * it.qty
    total += subtotal
    print(f"   {it.name:<8} 单价 {it.price:>6.2f} x {it.qty:>3} = {subtotal:>7.2f}")
print(f"   {'合计':<8} {'':>19} = {total:>7.2f}")

print()
print("对比一下用字典写的 it['name']，namedtuple 的 it.name 更短也不容易拼错")


# ---------------------------------------------------------------
# 5. 什么时候该换 dataclass
# ---------------------------------------------------------------
show("5. namedtuple 还是 dataclass？")

print("namedtuple：不可变、轻量、能解包；字段都可哈希时能当字典键")
print("           适合「一条记录」这种用完就不改的数据")
print()
print("dataclass ：可变、能写方法、支持继承、字段类型清晰")
print("           适合真正当对象用、需要修改状态的场景")
print()
print("粗糙的判断：字段要不要改？要改 -> dataclass；不改 -> namedtuple")


show("做完了？去 99_exercises.py 做第 4 节练习")
