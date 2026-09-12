# -*- coding: utf-8 -*-
"""
01 名字、对象与引用
==================

目标：建立 Python 最重要的心智模型：变量不是“装值的盒子”，而是绑定到对象的名字。
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. 赋值是名字绑定")
a = [1, 2]
b = a
print("a:", a)
print("b:", b)
print("a is b:", a is b)

b.append(3)
print("b 修改后 a:", a)

section("2. 重新绑定和修改对象不是一回事")
x = [1, 2]
y = x
x = [9, 9]
print("x:", x)
print("y:", y)
print("重新赋值 x 只是让 x 改绑到另一个对象。")

section("3. id() 表示对象身份")
p = {"name": "Alice"}
q = p
r = {"name": "Alice"}
print("id(p) == id(q):", id(p) == id(q))
print("id(p) == id(r):", id(p) == id(r))
print("p == r:", p == r)
print("p is r:", p is r)

section("4. 函数参数也遵守名字绑定")
def mutate(items):
    items.append("changed")


def rebind(items):
    items = ["new"]
    print("函数内部重新绑定:", items)


data = ["old"]
mutate(data)
print("mutate 后:", data)
rebind(data)
print("rebind 后外部仍是:", data)

section("5. 多重赋值可能共享同一对象")
a = b = []
a.append(1)
print("a:", a)
print("b:", b)
print("a is b:", a is b)

section("结论")
print("赋值绑定名字；原地修改作用于对象；重新赋值只改变当前名字的绑定。")
