# -*- coding: utf-8 -*-
"""05 operator：把运算符和取值操作变成可传递函数"""
from operator import itemgetter, attrgetter, methodcaller, add, mul

print("=== itemgetter ===")
rows = [("Alice", 90), ("Bob", 75), ("Carol", 88)]
print(sorted(rows, key=itemgetter(1), reverse=True))

print("\n=== attrgetter ===")
class User:
    def __init__(self, name, profile):
        self.name = name
        self.profile = profile

class Profile:
    def __init__(self, age):
        self.age = age

users = [User("A", Profile(30)), User("B", Profile(20))]
print([u.name for u in sorted(users, key=attrgetter("profile.age"))])

print("\n=== methodcaller ===")
strip = methodcaller("strip")
print(list(map(strip, [" a ", " b "])))
replace_dash = methodcaller("replace", "-", "_")
print(replace_dash("hello-world"))

print("\n=== add/mul 等 ===")
print(add(2, 3), mul(4, 5))
print("简单 lambda 足够清楚时不必强行 operator；排序/取字段时 itemgetter/attrgetter 很合适。")
