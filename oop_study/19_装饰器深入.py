# -*- coding: utf-8 -*-
"""
19 装饰器深入 —— 从 @check 讲到 functools 全家桶
==================================================

运行：  python 19_装饰器深入.py

装饰器就是「接受一个函数，返回一个函数」。
看起来玄，拆开就三行代码。这一节把它彻底拆干净。
"""

import functools
import time


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 拆开 @ 语法
# ---------------------------------------------------------------
show("1. @ 就是语法糖，展开后只有一行")


def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def hello_plain():
    return "hello"


@shout
def hello_decorated():
    return "hello"


print("手动包一层 :", shout(hello_plain)())
print("用 @ 语法  :", hello_decorated())
print()
print("完全等价：")
print("    @shout")
print("    def hello(): ...")
print("  ─────────────────────")
print("    def hello(): ...")
print("    hello = shout(hello)")
print()
print("注意最后一行：函数名被「返回值」覆盖了。这就是装饰器的一切。")


# ---------------------------------------------------------------
# 2. 为什么带参数的装饰器要套三层
# ---------------------------------------------------------------
show("2. 带参数的装饰器：三层不是凑数的")


def repeat(times):
    def decorator(func):                    # 第二层：收到函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):       # 第三层：真正被调用的
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator                        # 第一层：收到参数，返回装饰器


@repeat(times=3)
def say(word):
    print(f"   说: {word}")
    return word


result = say("你好")
print("返回值:", result)
print()
print("对照一下没有参数的版本，看差在哪：")
print("    def shout(func):            <- 直接收函数")
print("    def repeat(times):          <- 先收参数")
print("        def decorator(func):    <- 再收函数")
print()
print("所以 @repeat(times=3) 其实是「先调用 repeat(3)，拿它的返回值当装饰器」。")
print("少一层的话，times 和 func 会抢同一个位置。")


# ---------------------------------------------------------------
# 3. functools.wraps 保住了什么
# ---------------------------------------------------------------
show("3. functools.wraps 不是可有可无的")


def naive(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def proper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def original(a, b):
    """两个数相加。"""
    return a + b


naive_add = naive(original)
proper_add = proper(original)

print(f"{'':<12}{'__name__':<16}{'__doc__':<14}__wrapped__")
for label, fn in [("原函数", original), ("没加 wraps", naive_add), ("加了 wraps", proper_add)]:
    doc = getattr(fn, "__doc__", None)
    wrapped = getattr(fn, "__wrapped__", None)
    print(f"{label:<12}{fn.__name__:<16}{str(doc):<14}{wrapped is not None}")

print()
print("看出来了吗：没加 wraps 的版本，名字变成了 wrapper、文档没了。")
print("加了 wraps 之后，元信息全部保留，还多了个 __wrapped__ 指回原函数。")
print()
print("这不只是好看：调试器、IDE 提示、pytest 收集测试用例都依赖 __name__。")
print("你要是用装饰器包了测试函数却忘了 wraps，pytest 会把它们认成同一个。")


# ---------------------------------------------------------------
# 4. 多个装饰器叠加：谁先谁后
# ---------------------------------------------------------------
show("4. 叠加顺序（最容易搞反的地方）")


def outer_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("   进入 OUTER")
        r = func(*args, **kwargs)
        print("   离开 OUTER")
        return r
    return wrapper


def inner_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("   进入 inner")
        r = func(*args, **kwargs)
        print("   离开 inner")
        return r
    return wrapper


@outer_deco
@inner_deco
def target():
    print("   >>> 执行 target 本体")


target()
print()
print("记住两句话：")
print("  1. 离函数最近的（inner）先被包进去，所以最先「进入」的是 outer")
print("  2. @a @b 展开就是 a(b(target))")
print()
print("换个记法：装饰器像套娃，最上面的在最外层。进入时从外往里，")
print("退出时从里往外 —— 和调用栈完全一致。")


# ---------------------------------------------------------------
# 5. 用类做装饰器
# ---------------------------------------------------------------
show("5. 类也能当装饰器（靠 __call__）")


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)    # 类版本用这个保留元信息
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"   第 {self.count} 次调用")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    return f"你好，{name}"


print(greet("张三"))
print(greet("李四"))
print("计数存在哪:", greet.count, " <- 存在装饰器实例上")
print()
print("什么时候用类而不是函数：需要保存状态、或者需要额外的方法/属性时。")
print("函数版得用 wrapper.calls = 0 这种土办法（练习 ex25 就是这么写的）。")


# ---------------------------------------------------------------
# 6. 装饰类本身
# ---------------------------------------------------------------
show("6. 装饰器也能套在类上")


def add_repr(cls):
    """给类自动生成 __repr__。"""
    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{cls.__name__}({fields})"

    cls.__repr__ = __repr__
    return cls


@add_repr
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


print(Point(1, 2))
print()
print("修饰类的装饰器：收类、改类、返回类。")
print("dataclass 就是这么干的 —— @dataclass 接到类，加一堆方法再还给你。")


# ---------------------------------------------------------------
# 7. 注册器：@check 的真实身份
# ---------------------------------------------------------------
show("7. 注册器模式（练习册里那个 @check）")

REGISTRY = {}


def register(name):
    def decorator(func):
        REGISTRY[name] = func
        return func                       # 注意：原样返回，不包装
    return decorator


@register("add")
def do_add(a, b):
    return a + b


@register("mul")
def do_mul(a, b):
    return a * b


print("注册表:", list(REGISTRY))
print("按名字调用:", REGISTRY["add"](2, 3))
print()
print("注意这个装饰器和前面的不一样：它不包 wrapper，直接把原函数返回。")
print("因为它的目的不是「改变行为」，而是「登记一下」。")
print("99_exercises.py 里的 @check 就是这一种。")


# ---------------------------------------------------------------
# 8. 标准库里的现成装饰器
# ---------------------------------------------------------------
show("8. 别重复造轮子")


@functools.lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


t0 = time.perf_counter()
print("   fib(200) =", fib(200))
print(f"   耗时 {time.perf_counter() - t0:.6f} 秒（带缓存）")
print("   缓存信息:", fib.cache_info())


class Config:
    @functools.cached_property
    def heavy_value(self):
        print("   （真的算了一次）")
        return sum(range(100_000))


c = Config()
_ = c.heavy_value
_ = c.heavy_value
print("   cached_property 第二次访问不会重算")


@functools.singledispatch
def describe(x):
    return f"不知道这是什么: {x!r}"


@describe.register(int)
def _(x):
    return f"整数 {x}"


@describe.register(list)
def _(x):
    return f"列表，有 {len(x)} 项"


print()
print("   singledispatch 按第一个参数的类型分派：")
print("    ", describe(42))
print("    ", describe([1, 2]))
print("    ", describe("文本"))


# ---------------------------------------------------------------
# 9. 常见的坑
# ---------------------------------------------------------------
show("9. 五个高频坑")

print("坑 1：忘了 return func(...)")


def forgot_return(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # 忘了 return，调用方永远拿到 None
    return wrapper


@forgot_return
def add(a, b):
    return a + b


print("   add(1, 2) =", add(1, 2), " <- 变成 None 了，而且不报错")

print()
print("坑 2：忘了 functools.wraps")
print("   后果见第 3 节，排查起来特别费劲。")

print()
print("坑 3：装饰器在「函数定义时」就执行了")
print("   @shout 那两行在模块加载时就跑完了，不是调用 hello() 时才跑。")
print("   所以别在装饰器体里做耗时的事，否则 import 会变慢。")

print()
print("坑 4：装饰器无法装饰「部分参数」")
print("   装饰器只能整包整个函数，不能只包某几个参数。")
print("   那种需求要在函数体里处理。")

print()
print("坑 5：不小心丢掉签名")
print("   加了 wraps 能保住 __name__，但 IDE 还是可能看不懂参数。")
print("   想更严格可以用 inspect.signature 显式复制，但多数情况 wraps 就够。")


show("练习：去 99_exercises.py 做 ex27 ~ ex28")
