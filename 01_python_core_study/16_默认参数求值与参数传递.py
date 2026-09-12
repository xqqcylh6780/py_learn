# -*- coding: utf-8 -*-
"""
16 默认参数求值与参数传递
========================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. 默认参数在 def 执行时求值一次")
def bad_add(value, bucket=[]):
    bucket.append(value)
    return bucket

print(bad_add(1))
print(bad_add(2))

section("2. 推荐用 None 哨兵")
def good_add(value, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(value)
    return bucket

print(good_add(1))
print(good_add(2))

section("3. 参数传递：对象共享，不是值复制")
def mutate(items):
    items.append(9)


data = [1, 2]
mutate(data)
print(data)

section("4. 形参重新绑定不会替换调用者变量")
def replace(items):
    items = [100]
    return items

original = [1, 2]
returned = replace(original)
print("original:", original)
print("returned:", returned)

section("5. 关键点")
print("Python 常被描述为 call by sharing / object reference sharing。")
print("函数接收的是同一对象的引用绑定；能否观察到修改取决于对象是否被原地修改。")
