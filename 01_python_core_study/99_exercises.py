# -*- coding: utf-8 -*-
"""
Python 核心语法练习册 —— 52 题，自动判分
========================================

运行：
    python 99_exercises.py

规则：
- 每题独立；未完成只会显示 FAIL/ERR，不影响后面的题。
- 参考答案在文件最底部。
- 建议先自己做，再看答案。
"""

from __future__ import annotations

import inspect
import math
from copy import deepcopy

_CHECKS = []


def check(fn):
    _CHECKS.append(fn)
    return fn


# 01 名字、对象与引用 ---------------------------------------------------------
@check
def ex01_shared_reference():
    a = [1, 2]
    b = None  # TODO：让 b 与 a 指向同一个对象
    assert b is a
    b.append(3)
    assert a == [1, 2, 3]


@check
def ex02_rebind_does_not_replace():
    def rebind(items):
        # TODO：让局部 items 指向一个新列表 [9]，并返回它
        pass

    data = [1, 2]
    returned = rebind(data)
    assert data == [1, 2]
    assert returned == [9]


# 02 类型、可变性、可哈希性 -------------------------------------------------
@check
def ex03_hashable_coordinate():
    key = None  # TODO：用可哈希对象表示坐标 3,4
    mapping = {key: "P"}
    assert mapping[(3, 4)] == "P"


@check
def ex04_tuple_hashability():
    good = None  # TODO：创建一个可以 hash 的 tuple，内容为 1, 2
    assert good == (1, 2)
    assert isinstance(hash(good), int)


# 03 数值 -------------------------------------------------------------------
@check
def ex05_floor_division():
    result = None  # TODO：计算 -7 // 2
    assert result == -4


@check
def ex06_float_compare():
    result = None  # TODO：用正确方式判断 0.1 + 0.2 是否接近 0.3
    assert result is True


# 04 字符串 / Unicode / bytes ------------------------------------------------
@check
def ex07_utf8_roundtrip():
    text = "中文🙂"
    raw = None      # TODO：UTF-8 编码
    restored = None # TODO：再解码回来
    assert isinstance(raw, bytes)
    assert restored == text


@check
def ex08_string_processing():
    raw = "  alice,bob,charlie  "
    result = None  # TODO：得到 ['alice', 'bob', 'charlie']
    assert result == ["alice", "bob", "charlie"]


# 05 序列 -------------------------------------------------------------------
@check
def ex09_reverse_slice():
    data = [1, 2, 3, 4, 5]
    result = None  # TODO：用切片反转
    assert result == [5, 4, 3, 2, 1]


@check
def ex10_independent_grid():
    grid = None  # TODO：创建 3x3 的 0，三行互相独立
    grid[0][0] = 9
    assert grid == [[9, 0, 0], [0, 0, 0], [0, 0, 0]]


@check
def ex11_slice_every_second():
    data = list(range(10))
    result = None  # TODO：取出 1,3,5,7,9
    assert result == [1, 3, 5, 7, 9]


# 06 dict / set --------------------------------------------------------------
@check
def ex12_dict_merge():
    base = {"host": "localhost", "port": 8000}
    override = {"port": 9000, "debug": True}
    result = None  # TODO：合并，override 覆盖 base
    assert result == {"host": "localhost", "port": 9000, "debug": True}


@check
def ex13_set_common():
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    result = None  # TODO：交集
    assert result == {3, 4}


@check
def ex14_missing_vs_none():
    data = {"x": None}
    # TODO：分别判断 x 存在、y 不存在，不要只靠 get()
    x_exists = False
    y_exists = True
    assert x_exists is True
    assert y_exists is False


# 07 truthiness / None -------------------------------------------------------
@check
def ex15_preserve_zero():
    def default(value):
        # TODO：只有 None 才返回 100；0 必须保留
        return 100

    assert default(None) == 100
    assert default(0) == 0
    assert default(5) == 5


@check
def ex16_all_positive():
    def all_positive(values):
        return None  # TODO：所有元素 > 0 才 True

    assert all_positive([1, 2, 3]) is True
    assert all_positive([1, 0, 3]) is False


# 08 comparisons ------------------------------------------------------------
@check
def ex17_value_not_identity():
    a = [1, 2]
    b = [1, 2]
    result = None  # TODO：判断“值相等”
    assert result is True
    assert a is not b


@check
def ex18_chain_compare():
    x = 5
    result = None  # TODO：判断 x 在闭区间 [1, 10] 内
    assert result is True


# 09 unpacking / walrus ------------------------------------------------------
@check
def ex19_unpack_middle():
    data = [1, 2, 3, 4, 5]
    first = middle = last = None
    # TODO：一条解包赋值
    assert first == 1
    assert middle == [2, 3, 4]
    assert last == 5


@check
def ex20_swap():
    a, b = 10, 20
    # TODO：不用临时变量交换
    assert (a, b) == (20, 10)


@check
def ex21_walrus_single_call():
    calls = {"count": 0}

    def length(value):
        calls["count"] += 1
        return len(value)

    text = "abcdef"
    n = None
    ok = False
    # TODO：用 := 调一次 length；长度 > 5 时 ok=True
    assert ok is True
    assert n == 6
    assert calls["count"] == 1


# 10 if / match --------------------------------------------------------------
@check
def ex22_match_status():
    def status(code):
        # TODO：match/case: 200 -> OK, 404 -> NOT_FOUND, 其他 -> OTHER
        return None

    assert status(200) == "OK"
    assert status(404) == "NOT_FOUND"
    assert status(500) == "OTHER"


@check
def ex23_match_point():
    def kind(value):
        # TODO：[0,0] -> origin；[x,0] -> x-axis；任意二维点 -> point；其他 -> other
        return None

    assert kind([0, 0]) == "origin"
    assert kind([3, 0]) == "x-axis"
    assert kind([1, 2]) == "point"
    assert kind([1, 2, 3]) == "other"


# 11 loops ------------------------------------------------------------------
@check
def ex24_enumerate_start_one():
    values = ["a", "b", "c"]
    result = None  # TODO：[(1,'a'), (2,'b'), (3,'c')]
    assert result == [(1, "a"), (2, "b"), (3, "c")]


@check
def ex25_zip_to_dict():
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    result = None  # TODO：组合为字典
    assert result == {"a": 1, "b": 2, "c": 3}


@check
def ex26_zip_strict():
    caught = False
    try:
        # TODO：使用 strict=True，让长度不一致时抛 ValueError
        list(zip([1, 2], ["a"]))
    except ValueError:
        caught = True
    assert caught is True


# 12 break / continue / else -------------------------------------------------
@check
def ex27_find_first_even():
    values = [1, 3, 7, 8, 10]
    found = None
    # TODO：找到第一个偶数后 break
    assert found == 8


@check
def ex28_for_else_prime():
    def is_prime(n):
        # TODO：用 for...else 判断 n 是否为 >=2 的素数
        return None

    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(1) is False


# 13 comprehensions ----------------------------------------------------------
@check
def ex29_even_squares():
    result = None  # TODO：0~9 中偶数的平方
    assert result == [0, 4, 16, 36, 64]


@check
def ex30_flatten_matrix():
    matrix = [[1, 2], [3, 4], [5]]
    result = None  # TODO：一层展开
    assert result == [1, 2, 3, 4, 5]


@check
def ex31_dict_comprehension():
    words = ["a", "bb", "ccc"]
    result = None  # TODO：{单词: 长度}
    assert result == {"a": 1, "bb": 2, "ccc": 3}


# 14 first-class functions ---------------------------------------------------
@check
def ex32_return_function():
    def make_adder(n):
        # TODO：返回一个函数，该函数把参数加 n
        pass

    add10 = make_adder(10)
    assert callable(add10)
    assert add10(5) == 15


@check
def ex33_function_dispatch():
    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    ops = None  # TODO：构造 {'+': add, '*': mul}
    assert ops["+"](2, 3) == 5
    assert ops["*"](2, 3) == 6


# 15 parameter rules ---------------------------------------------------------
@check
def ex34_keyword_only():
    # TODO：修改签名，使 timeout 成为仅关键字参数
    def connect(host, timeout=5):
        return host, timeout

    sig = inspect.signature(connect)
    assert sig.parameters["timeout"].kind is inspect.Parameter.KEYWORD_ONLY
    assert connect("x", timeout=10) == ("x", 10)


@check
def ex35_positional_only():
    # TODO：修改签名，使 a/b 只能按位置传
    def divide(a, b):
        return a / b

    sig = inspect.signature(divide)
    assert sig.parameters["a"].kind is inspect.Parameter.POSITIONAL_ONLY
    assert divide(8, 2) == 4


@check
def ex36_args_kwargs():
    def collect(*args, **kwargs):
        return None  # TODO：返回 (位置参数之和, kwargs)

    assert collect(1, 2, 3, x=4) == (6, {"x": 4})


# 16 defaults / argument sharing --------------------------------------------
@check
def ex37_safe_default():
    def add(value, bucket=None):
        # TODO：每次 bucket 未提供时创建新 list，再 append value
        return bucket

    assert add(1) == [1]
    assert add(2) == [2]


@check
def ex38_mutate_argument():
    def append_value(items, value):
        # TODO：原地修改调用方 list
        pass

    data = [1]
    append_value(data, 2)
    assert data == [1, 2]


# 17 scope / closure ---------------------------------------------------------
@check
def ex39_nonlocal_counter():
    def make_counter():
        n = 0

        def inc():
            # TODO：nonlocal 修改 n
            return None

        return inc

    counter = make_counter()
    assert [counter(), counter(), counter()] == [1, 2, 3]


@check
def ex40_global_not_needed():
    tax = 0.1

    def total(price):
        # TODO：只读取外层 tax，不需要 global
        return None

    assert math.isclose(total(100), 110)


# 18 lambda / late binding ---------------------------------------------------
@check
def ex41_fix_late_binding():
    funcs = None  # TODO：三个函数分别返回 0、1、2
    assert [fn() for fn in funcs] == [0, 1, 2]


@check
def ex42_sort_with_key():
    data = [("A", 3), ("B", 1), ("C", 2)]
    result = None  # TODO：按第二项升序
    assert result == [("B", 1), ("C", 2), ("A", 3)]


# 19 builtins / sorting ------------------------------------------------------
@check
def ex43_min_by_key():
    users = [{"name": "A", "age": 30}, {"name": "B", "age": 20}]
    result = None  # TODO：找 age 最小的用户
    assert result == {"name": "B", "age": 20}


@check
def ex44_stable_sort():
    records = [("A", 2), ("B", 1), ("C", 2)]
    result = None  # TODO：按第二项排序
    assert result == [("B", 1), ("A", 2), ("C", 2)]


# 20 formatting --------------------------------------------------------------
@check
def ex45_money_format():
    value = 12345.6
    result = None  # TODO：格式化成 '12,345.60'
    assert result == "12,345.60"


@check
def ex46_debug_repr():
    text = "a\nb"
    result = None  # TODO：得到 text 的 repr 字符串
    assert result == "'a\\nb'"


# 21 iteration ---------------------------------------------------------------
@check
def ex47_manual_iteration():
    it = iter([10, 20, 30])
    result = None  # TODO：用 next 取前三个，组成 list
    assert result == [10, 20, 30]
    try:
        next(it)
    except StopIteration:
        pass
    else:
        raise AssertionError("迭代器应该已经耗尽")


@check
def ex48_is_iterable():
    def is_iterable(obj):
        # TODO：尝试 iter(obj)，TypeError 时 False，否则 True
        return None

    assert is_iterable([1, 2]) is True
    assert is_iterable("abc") is True
    assert is_iterable(123) is False


# 22 pitfalls ----------------------------------------------------------------
@check
def ex49_deep_copy_nested():
    original = [[1], [2]]
    copied = None  # TODO：真正独立复制嵌套可变对象
    copied[0].append(9)
    assert original == [[1], [2]]
    assert copied == [[1, 9], [2]]


@check
def ex50_filter_without_mutating_during_iteration():
    items = [1, 2, 3, 4, 5, 6]
    result = None  # TODO：得到所有奇数，不要边遍历原列表边 remove
    assert result == [1, 3, 5]
    assert items == [1, 2, 3, 4, 5, 6]


# 23 operators ---------------------------------------------------------------
@check
def ex51_bitmask_permission():
    READ = 0b001
    WRITE = 0b010
    permissions = READ | WRITE
    can_write = None  # TODO：使用位运算判断 WRITE 是否存在
    assert can_write is True


@check
def ex52_precedence_with_parentheses():
    # TODO：通过加括号，让表达式结果为 20
    result = 2 + 3 * 4
    assert result == 20


def run_all():
    print("=" * 72)
    print("Python Core Study - 52 道练习")
    print("=" * 72)
    passed = 0
    for fn in _CHECKS:
        try:
            fn()
        except AssertionError as exc:
            print(f"[FAIL] {fn.__name__:<32} {exc or '断言未通过'}")
        except Exception as exc:
            print(f"[ERR ] {fn.__name__:<32} {type(exc).__name__}: {exc}")
        else:
            passed += 1
            print(f"[ OK ] {fn.__name__}")
    print("-" * 72)
    print(f"通过 {passed}/{len(_CHECKS)}")
    if passed == len(_CHECKS):
        print("全部通过：Python 核心语法通关。")


if __name__ == "__main__":
    run_all()


# =============================================================================
# 参考答案（先做再看）
# =============================================================================
"""
ex01
    b = a

ex02
    items = [9]
    return items

ex03
    key = (3, 4)

ex04
    good = (1, 2)

ex05
    result = -7 // 2

ex06
    result = math.isclose(0.1 + 0.2, 0.3)

ex07
    raw = text.encode("utf-8")
    restored = raw.decode("utf-8")

ex08
    result = raw.strip().split(",")

ex09
    result = data[::-1]

ex10
    grid = [[0] * 3 for _ in range(3)]

ex11
    result = data[1::2]

ex12
    result = base | override

ex13
    result = a & b

ex14
    x_exists = "x" in data
    y_exists = "y" in data

ex15
    return 100 if value is None else value

ex16
    return all(x > 0 for x in values)

ex17
    result = (a == b)

ex18
    result = 1 <= x <= 10

ex19
    first, *middle, last = data

ex20
    a, b = b, a

ex21
    if (n := length(text)) > 5:
        ok = True

ex22
    match code:
        case 200: return "OK"
        case 404: return "NOT_FOUND"
        case _: return "OTHER"

ex23
    match value:
        case [0, 0]: return "origin"
        case [_, 0]: return "x-axis"
        case [_, _]: return "point"
        case _: return "other"

ex24
    result = list(enumerate(values, start=1))

ex25
    result = dict(zip(keys, values))

ex26
    list(zip([1, 2], ["a"], strict=True))

ex27
    for value in values:
        if value % 2 == 0:
            found = value
            break

ex28
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        return True
    return False

ex29
    result = [x * x for x in range(10) if x % 2 == 0]

ex30
    result = [x for row in matrix for x in row]

ex31
    result = {word: len(word) for word in words}

ex32
    return lambda x: x + n

ex33
    ops = {"+": add, "*": mul}

ex34
    def connect(host, *, timeout=5):

ex35
    def divide(a, b, /):

ex36
    return sum(args), kwargs

ex37
    if bucket is None:
        bucket = []
    bucket.append(value)
    return bucket

ex38
    items.append(value)

ex39
    nonlocal n
    n += 1
    return n

ex40
    return price * (1 + tax)

ex41
    funcs = [lambda i=i: i for i in range(3)]

ex42
    result = sorted(data, key=lambda item: item[1])

ex43
    result = min(users, key=lambda user: user["age"])

ex44
    result = sorted(records, key=lambda row: row[1])

ex45
    result = f"{value:,.2f}"

ex46
    result = repr(text)

ex47
    result = [next(it), next(it), next(it)]

ex48
    try:
        iter(obj)
    except TypeError:
        return False
    return True

ex49
    copied = deepcopy(original)

ex50
    result = [x for x in items if x % 2 == 1]

ex51
    can_write = bool(permissions & WRITE)

ex52
    result = (2 + 3) * 4
"""
