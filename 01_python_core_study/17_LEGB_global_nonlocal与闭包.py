# -*- coding: utf-8 -*-
"""
17 LEGB、global、nonlocal 与闭包
===============================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


GLOBAL_NAME = "G"

section("1. LEGB 查找顺序")
def outer():
    enclosing = "E"
    def inner():
        local = "L"
        print(local, enclosing, GLOBAL_NAME, len)
    inner()

outer()

section("2. 一旦函数体里对名字赋值，它默认被视为局部名字")
x = 10
def demo_unbound():
    try:
        print(x)
        x = 20
    except UnboundLocalError as exc:
        print("UnboundLocalError:", exc)

demo_unbound()

section("3. global 修改模块级绑定")
count = 0
def inc_global():
    global count
    count += 1
inc_global()
print(count)

section("4. nonlocal 修改最近外层函数绑定")
def make_counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

counter = make_counter()
print(counter(), counter(), counter())

section("5. 闭包保存外层环境")
print(counter.__closure__)
print("外层函数返回后，被内部函数引用的变量仍然存在。")
