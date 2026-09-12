# -*- coding: utf-8 -*-
"""
08 比较、身份、成员关系与链式比较
================================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. == 比较值，is 比较身份")
a = [1, 2]
b = [1, 2]
c = a
print("a == b:", a == b)
print("a is b:", a is b)
print("a is c:", a is c)

section("2. 不要用 is 比普通数字或字符串")
x = 100
print("x == 100:", x == 100)
print("对象缓存是实现细节，值比较应使用 ==。")

section("3. in / not in")
print(2 in [1, 2, 3])
print("name" in {"name": "Alice"})
print("ice" in "Alice")

section("4. 链式比较只求值中间项一次")
x = 5
print(1 < x < 10)
print("等价语义接近 1 < x and x < 10，但中间表达式只求值一次。")

section("5. NotImplemented 与比较协议")
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

print(Temperature(20) == Temperature(20))
print(Temperature(20) == 20)
