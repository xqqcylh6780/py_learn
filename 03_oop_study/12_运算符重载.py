# -*- coding: utf-8 -*-
"""
12 运算符重载 —— 让你的对象支持 + - * / 和比较
================================================

运行：  python 12_运算符重载.py

重载不是「随便定义」，而是「实现 Python 已经定好的那些协议」：
    a + b   ->  a.__add__(b)，不行就试 b.__radd__(a)
    a < b   ->  a.__lt__(b)
    -a      ->  a.__neg__()
"""

from functools import total_ordering


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 一个能算的向量
# ---------------------------------------------------------------
show("1. 让对象支持加减乘")


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented          # 关键：别抛异常，交给 Python
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Vector(self.x * k, self.y * k)

    def __rmul__(self, k):
        """支持 3 * v 这种「数字在左边」的写法。"""
        return self.__mul__(k)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print("v1 + v2   =", v1 + v2)
print("v1 - v2   =", v1 - v2)
print("v1 * 3    =", v1 * 3)
print("3 * v1    =", 3 * v1, " <- 走的是 __rmul__")
print("-v1       =", -v1)
print("abs(v1)   =", round(abs(v1), 4))


# ---------------------------------------------------------------
# 2. NotImplemented 到底在干什么
# ---------------------------------------------------------------
show("2. 为什么必须返回 NotImplemented，而不是抛异常")


class Strict:
    def __add__(self, other):
        return NotImplemented


class Sloppy:
    def __add__(self, other):
        return None                        # 错误示范


try:
    Strict() + 1
except TypeError as e:
    print("返回 NotImplemented :", e)

print("返回 None           :", Sloppy() + 1, " <- 静默返回 None，bug 藏起来了")
print()
print("原因：返回 NotImplemented 是告诉 Python「我这类型不会算，你去问问右边那个」。")
print("只有所有类型都说不会，Python 才抛出清晰的 TypeError。")
print()
print("所以 v1 + 3 会报错，但 3 * v1 能用 —— 因为 * 有 __rmul__ 兜着。")
try:
    v1 + 3
except TypeError as e:
    print("  v1 + 3 ->", e)


# ---------------------------------------------------------------
# 3. 就地运算 __iadd__
# ---------------------------------------------------------------
show("3. += 是原地改还是造新的")


class Box:
    def __init__(self, items):
        self.items = list(items)

    def __iadd__(self, other):             # b += x
        self.items.extend(other)
        return self                        # 必须返回 self

    def __add__(self, other):              # b + x
        return Box(self.items + list(other))

    def __repr__(self):
        return f"Box({self.items})"


b1 = Box([1])
b1_id = id(b1)
b1 += [2, 3]
print("b1 += [2,3] 后 b1 =", b1)
print("id 变了吗          :", id(b1) != b1_id, " <- 没变，说明是原地改的")

b2 = Box([1])
b2_id = id(b2)
b2 = b2 + [2, 3]
print("b2 = b2 + [2,3] 后  =", b2)
print("id 变了吗          :", id(b2) != b2_id, " <- 变了，造了个新对象")


# ---------------------------------------------------------------
# 4. 比较运算符与 total_ordering
# ---------------------------------------------------------------
show("4. 比较：只写两个，补齐六个")


@total_ordering
class Version:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def _key(self):
        return (self.major, self.minor)

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key() == other._key()

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key() < other._key()

    def __repr__(self):
        return f"v{self.major}.{self.minor}"


a, b, c = Version(1, 9), Version(2, 0), Version(2, 0)
print("a < b :", a < b)
print("b == c:", b == c)
print("b >= c:", b >= c, " <- 你没写 __ge__，@total_ordering 自动补的")
print("b > a :", b > a)
print("排序  :", sorted([b, a, c]))
print()
print("@total_ordering 的用法：写 __eq__ 和 __lt__（或 __le__），")
print("它自动补出 __le__ __gt__ __ge__，省掉四份重复代码。")


# ---------------------------------------------------------------
# 5. __bool__ 和 __len__ 影响真假判断
# ---------------------------------------------------------------
show("5. if obj: 走的是谁")


class Wallet:
    def __init__(self, money):
        self.money = money

    def __bool__(self):
        return self.money > 0

    def __repr__(self):
        return f"Wallet({self.money})"


print("bool(Wallet(0))  :", bool(Wallet(0)))
print("bool(Wallet(100)):", bool(Wallet(100)))
print("if Wallet(0)     :", "有钱" if Wallet(0) else "没钱")
print()
print("顺序：先找 __bool__，没有才退回去看 __len__，再没有就恒为 True。")


# ---------------------------------------------------------------
# 6. 常用运算符对照表
# ---------------------------------------------------------------
show("6. 对照表")

rows = [
    ("obj + other", "__add__ / __radd__"),
    ("obj - other", "__sub__ / __rsub__"),
    ("obj * other", "__mul__ / __rmul__"),
    ("obj / other", "__truediv__"),
    ("obj // other", "__floordiv__"),
    ("obj % other", "__mod__"),
    ("obj += x", "__iadd__（没有就用 __add__）"),
    ("-obj", "__neg__"),
    ("abs(obj)", "__abs__"),
    ("obj < other", "__lt__"),
    ("obj == other", "__eq__"),
    ("if obj", "__bool__"),
    ("obj[key]", "__getitem__"),
    ("obj[key] = v", "__setitem__"),
]
for syntax, method in rows:
    print(f"  {syntax:<18} {method}")


show("练习：去 99_exercises.py 做 ex20")
