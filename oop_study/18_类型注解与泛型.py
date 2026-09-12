# -*- coding: utf-8 -*-
"""
18 类型注解与泛型 —— 让类型信息帮你看代码
============================================

运行：  python 18_类型注解与泛型.py

先说最重要的一件事：Python 的类型注解在运行时基本不做检查。
它的价值在于给「读代码的人」和「IDE / mypy 这类工具」看的。
"""

from typing import Generic, TypeVar, Optional, Callable, get_type_hints


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 注解只是写着玩的（运行时）
# ---------------------------------------------------------------
show("1. 注解不会阻止你做傻事")


def add(a: int, b: int) -> int:
    return a + b


print("add(1, 2)          =", add(1, 2))
print("add('a', 'b')      =", add("a", "b"), " <- 传字符串照样跑，没人拦你")
print()
print("想真正检查，得用 IDE 的实时提示，或者命令行跑 mypy / pyright。")
print("注解是「给人看的文档」，不是「运行时的约束」。")
print()
print("但有个例外：dataclass、pydantic 这类库会去读注解来干活（09 节）。")


# ---------------------------------------------------------------
# 2. 常用写法
# ---------------------------------------------------------------
show("2. 常用类型写法")


def process(
    name: str,
    scores: list[int],
    meta: dict[str, int],
    pair: tuple[int, str],
    tags: set[str],
    note: Optional[str] = None,
    callback: Callable[[int], str] | None = None,
) -> dict[str, object]:
    return {"name": name, "total": sum(scores), "n": len(meta)}


print("list[int]       一列整数")
print("dict[str, int]  键是字符串、值是整数")
print("tuple[int, str] 定长元组，第一位 int 第二位 str")
print("tuple[int, ...] 变长元组，全是 int")
print("set[str]        字符串集合")
print("Optional[str]   等价于 str | None")
print("Callable[[int], str]  接收一个 int、返回 str 的函数")
print("str | None      3.10+ 的新写法，比 Optional 简洁")
print()
print("实际调用:", process("张三", [90, 85], {"age": 28}, (1, "a"), {"x"}))


# ---------------------------------------------------------------
# 3. 泛型：让类型跟着输入走
# ---------------------------------------------------------------
show("3. TypeVar + Generic")

T = TypeVar("T")


class Stack(Generic[T]):
    """一个类型安全的栈：丢进 int，取出来也是 int。"""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("栈是空的")
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


s: Stack[int] = Stack()          # 声明这是装 int 的栈
s.push(1)
s.push(2)
print("pop() =", s.pop(), "| 剩下的长度 =", len(s))

print()
print("为什么需要泛型？看对比：")
print("  不加泛型：def first(items: list) -> object   调用方不知道拿到什么类型")
print("  加泛型  ：def first(items: list[T]) -> T     传 list[int] 就推出返回 int")


def first(items: list[T]) -> T:
    return items[0]


print()
print("first([1, 2, 3])     -> 类型被推导为 int")
print("first(['a', 'b'])    -> 类型被推导为 str")
print("实际跑一下:", first([1, 2, 3]), first(["a", "b"]))


# ---------------------------------------------------------------
# 4. 把函数类型也约束起来
# ---------------------------------------------------------------
show("4. 用 Protocol 描述「可调用对象」的形状")

from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other) -> bool: ...

    def __gt__(self, other) -> bool: ...


def max_of(items: list[Comparable]) -> Comparable:
    best = items[0]
    for x in items:
        if x > best:
            best = x
    return best


print("max_of([3, 1, 4, 1, 5]) =", max_of([3, 1, 4, 1, 5]))
print("max_of(['b', 'a', 'c']) =", max_of(["b", "a", "c"]))
print()
print("Protocol 在这里的作用：不要求传入的东西继承谁，")
print("只要求「支持 > 运算」，类型检查器就能验证你用得对不对。")


# ---------------------------------------------------------------
# 5. 运行时读取注解
# ---------------------------------------------------------------
show("5. 注解在运行时是能读到的")

print("add.__annotations__ =", add.__annotations__)
print()
print("get_type_hints(Stack) 也能取出来 —— dataclass、ORM 就是靠这个工作的。")
print()


# ---------------------------------------------------------------
# 6. 前后向引用
# ---------------------------------------------------------------
show("6. 引用还没定义的类")


class Node2:
    def __init__(self, value: int, next_node: "Node2 | None" = None):
        self.value = value
        self.next_node = next_node


n = Node2(1)
print("Node2(1) =", vars(n))
print()
print("因为 Node2 在写注解时还没定义完，所以要用字符串包起来：'Node2 | None'")
print()
print("或者干脆在整个文件最上面加一行：")
print("    from __future__ import annotations")
print("这样所有注解都会自动变成字符串，不用手动加引号。")
print("Python 3.14 会把它变成默认行为，现在写上也没坏处。")


# ---------------------------------------------------------------
# 7. 什么时候写注解
# ---------------------------------------------------------------
show("7. 什么时候该写注解")

print("该写：")
print("  - 函数签名：参数和返回值，这是收益最大的地方")
print("  - 公共 API、库代码")
print("  - 团队协作的项目，或者你自己隔两周会再看一遍的代码")
print()
print("别纠结：")
print("  - 局部变量的类型通常能一眼看出来，不必全写")
print("  - 一次写不全也没关系，增量加注解是正常做法")
print()
print("注解最大的回报不是检查错误，是让 IDE 的补全变准。")


show("练习：去 99_exercises.py 做 ex26")
