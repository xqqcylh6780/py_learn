# -*- coding: utf-8 -*-
"""
05 魔术方法 —— 让你的对象用起来像内置类型
============================================

运行：  python 05_魔术方法.py

魔术方法 = 前后各两个下划线的方法，它们不是你调用的，
而是 Python 在特定语法下替你调用的：
    print(obj)      -> obj.__str__()
    obj == other    -> obj.__eq__(other)
    len(obj)        -> obj.__len__()
    obj[key]        -> obj.__getitem__(key)
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 没有 __repr__ 的世界很糟糕
# ---------------------------------------------------------------
show("1. __repr__ 和 __str__")


class Raw:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        """给开发者看：最好能直接复制粘贴回代码里。"""
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """给用户看：好看就行。"""
        return f"({self.x}, {self.y})"


print("没写 __repr__ :", Raw(1, 2), " <- 毫无信息量")
print("print 用 __str__ :", str(Point(1, 2)))
print("交互式用 __repr__:", repr(Point(1, 2)))
print("列表里显示的也是 repr:", [Point(1, 2), Point(3, 4)])
print()
print("只写 __repr__ 就能同时满足两者（__str__ 会退回去用它），所以先写 __repr__。")


# ---------------------------------------------------------------
# 2. __eq__ 和 __hash__ 的连坐关系（大坑）
# ---------------------------------------------------------------
show("2. 头号大坑：定义了 __eq__ 后，默认哈希通常会被禁用")


class NoHash:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, NoHash) and self.x == other.x


n = NoHash(1)
print("n == NoHash(1) :", n == NoHash(1), " <- 正常工作")
try:
    {n}
except TypeError as e:
    print("放进集合里     :", e)

print()
print("原因：对普通用户类来说，定义 __eq__ 而未显式定义 __hash__ 时，Python 通常会把 __hash__ 设为 None，")
print("于是自动把 __hash__ 设成了 None。想让它可哈希，就得自己补上：")


class Point2:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, Point2):
            return NotImplemented        # 让 Python 去试对方的 __eq__
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))    # 用参与比较的字段一起算

    def __repr__(self):
        return f"Point2({self.x}, {self.y})"


print()
print("补上 __hash__ 之后：")
print("  {Point2(1,2), Point2(1,2)} =", {Point2(1, 2), Point2(1, 2)}, " 去重成功")
print("  {Point2(1,2): 'A'}[Point2(1,2)] =", {Point2(1, 2): "A"}[Point2(1, 2)])
print()
print("铁律：__eq__ 认为相等的两个对象，__hash__ 必须相同。")


# ---------------------------------------------------------------
# 3. __len__ 和 __bool__
# ---------------------------------------------------------------
show("3. __len__ 与 __bool__：让 if obj: 有意义")


class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, i):
        return self.songs[i]

    def __contains__(self, song):
        return song in self.songs

    def __iter__(self):
        return iter(self.songs)

    def __repr__(self):
        return f"Playlist({self.songs})"


pl = Playlist(["夜曲", "晴天", "稻香"])
print("len(pl)              =", len(pl))
print("pl[0]                =", pl[0])
print("'晴天' in pl         =", "晴天" in pl)
print("for x in pl          :", [x for x in pl])
print("bool(pl)             =", bool(pl), " <- 没写 __bool__，就会看 __len__")
print("bool(Playlist([]))   =", bool(Playlist([])))
print()
print("补一句：如果只写了 __getitem__ 没写 __iter__，for 循环也能跑，")
print("因为 Python 会退化成「从下标 0 开始一直取到 IndexError」。")


# ---------------------------------------------------------------
# 4. __call__：让实例能像函数一样被调用
# ---------------------------------------------------------------
show("4. __call__：对象也能「调用」")


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


triple = Multiplier(3)
print("triple(5)        =", triple(5), " <- 实例后面加括号")
print("callable(triple) =", callable(triple))
print()
print("用途：需要「带状态的函数」时，用 __call__ 比闭包更清晰，也比普通函数好调试。")


# ---------------------------------------------------------------
# 5. 常用魔术方法清单
# ---------------------------------------------------------------
show("5. 常用魔术方法速查")

rows = [
    ("__repr__", "repr(obj)、列表里显示、调试"),
    ("__str__", "str(obj)、print(obj)"),
    ("__eq__ / __ne__", "== 和 !="),
    ("__lt__ / __gt__", "< 和 >（排序要用）"),
    ("__hash__", "hash(obj)、当字典键、放集合"),
    ("__len__", "len(obj)、bool(obj) 的回退"),
    ("__bool__", "bool(obj)、if obj"),
    ("__getitem__", "obj[key]"),
    ("__setitem__", "obj[key] = v"),
    ("__contains__", "x in obj"),
    ("__iter__", "for x in obj"),
    ("__call__", "obj(...)"),
    ("__enter__ / __exit__", "with obj（见 15 节）"),
    ("__add__ / __mul__", "obj + other（见 12 节）"),
]
for name, use in rows:
    print(f"  {name:<22} {use}")


show("练习：去 99_exercises.py 做 ex9 ~ ex10")
