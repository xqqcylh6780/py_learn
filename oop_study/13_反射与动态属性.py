# -*- coding: utf-8 -*-
"""
13 反射与动态属性 —— 按名字访问属性
====================================

运行：  python 13_反射与动态属性.py

反射 = 用字符串去操作属性。getattr(obj, "name") 等价于 obj.name，
区别是那个 "name" 可以在运行时才决定。
"""


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


class User:
    role = "普通用户"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"你好，我是 {self.name}"


u = User("张三", 28)


# ---------------------------------------------------------------
# 1. 四个内置函数
# ---------------------------------------------------------------
show("1. getattr / setattr / hasattr / delattr")

print("getattr(u, 'name')        =", getattr(u, "name"), " <- 等价于 u.name")
print("getattr(u, 'role')        =", getattr(u, "role"), " <- 类属性也能取")

method = getattr(u, "greet")            # 取出方法
print("getattr(u, 'greet')()     =", method(), " <- 取出来还能调用")

print("getattr(u, '不存在', '兜底') =", getattr(u, "不存在", "兜底"), " <- 给默认值不报错")

setattr(u, "email", "a@b.com")          # 等价于 u.email = ...
print("setattr 之后              =", u.__dict__)

print("hasattr(u, 'email')       =", hasattr(u, "email"))
delattr(u, "email")
print("delattr 之后 hasattr      =", hasattr(u, "email"))


# ---------------------------------------------------------------
# 2. 看一眼对象里到底有什么
# ---------------------------------------------------------------
show("2. vars() 和 dir()")

print("vars(u)  =", vars(u), " <- 就是 u.__dict__")
print("dir(u) 的前 12 个 =", dir(u)[:12])
print()
print("vars 只看实例自己的数据；dir 会把类和基类的方法一起列出来，范围大得多。")


# ---------------------------------------------------------------
# 3. __getattr__ vs __getattribute__
# ---------------------------------------------------------------
show("3. 两个长得像但完全不同的大招")


class Config:
    def __init__(self):
        self.debug = True

    def __getattr__(self, name):
        # 只在「正常查找也找不到」时才调用
        print(f"   [__getattr__] 找不到 {name}，给个默认值")
        return None


c = Config()
print("c.debug        =", c.debug, " <- 正常存在，不走 __getattr__")
print("c.whatever     =", c.whatever)
print("c.anything_else=", c.anything_else)


class Loud:
    def __getattribute__(self, name):
        # 每次访问属性都会走这里，包括访问方法
        if not name.startswith("__"):
            print(f"   [__getattribute__] 有人访问 {name}")
        return object.__getattribute__(self, name)


l = Loud()
l.x = 1
print("读取 l.x:")
_ = l.x

print()
print("区别一句话：")
print("  __getattr__       -> 找不到时才调用（补默认值专用）")
print("  __getattribute__  -> 每次访问都调用（能拦截一切，但要小心）")
print()
print("warning：__getattribute__ 里千万别写 self.xxx，那会无限递归。")
print("必须用 object.__getattribute__(self, name) 绕过自己。")


# ---------------------------------------------------------------
# 4. __setattr__ 的递归陷阱
# ---------------------------------------------------------------
show("4. __setattr__ 一写就递归")


class Bad:
    def __setattr__(self, name, value):
        self.name = value                  # 错：又调用自己，无限递归


try:
    Bad().x = 1
except RecursionError as e:
    print("错误写法 :", type(e).__name__, "-", e)


class Good:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("年龄不能为负")
        object.__setattr__(self, name, value)   # 用基类的实现收尾


g = Good()
g.age = 20
print("正确写法 :", g.__dict__)
try:
    g.age = -1
except ValueError as e:
    print("校验生效 :", e)


# ---------------------------------------------------------------
# 5. 实战：用 getattr 做命令分发
# ---------------------------------------------------------------
show("5. 实战：命令分发")


class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def run(self, command, a, b):
        func = getattr(self, command, None)
        if func is None or not callable(func):
            return f"没有这个命令: {command}"
        return func(a, b)


calc = Calculator()
for cmd in ["add", "mul", "div"]:
    print(f"   run('{cmd}', 6, 3) = {calc.run(cmd, 6, 3)}")

print()
print("好处：加新命令只要加个方法，分发逻辑一行都不用改。")
print("提醒：如果 command 来自用户输入，记得用白名单，")
print("否则 getattr 可能被用来调用到不该调的方法（getattr 的经典安全问题）。")


show("练习：去 99_exercises.py 做 ex21")
