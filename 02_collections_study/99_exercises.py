# -*- coding: utf-8 -*-
"""
collections 练习册 —— 自动判分
================================

运行：  python 99_exercises.py

现在直接跑，你会看到一堆 [FAIL]，那是正常的：它们就是待办清单。
逐个把 TODO 填掉，再跑一次，通过数会一点一点涨上去。

卡住了怎么办：翻到本文件最底下的「参考答案」，但建议先自己想 5 分钟。
"""

import traceback
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap

_checks = []


def check(fn):
    """把一个函数登记为一道题。"""
    _checks.append(fn)
    return fn


# =================================================================
# 第 1 节  Counter
# =================================================================

@check
def ex1_top_words():
    """返回出现次数最多的前 2 个单词（按次数从多到少）。"""
    words = "a b a c a b d".split()
    result = None                      # TODO
    assert result == ["a", "b"], f"期望 ['a', 'b']，实际是 {result!r}"


@check
def ex2_is_anagram():
    """忽略大小写和空格，判断两个字符串是否互为字母异位词。"""
    def is_anagram(s1, s2):
        return None                    # TODO

    assert is_anagram("Silent", "Listen") is True
    assert is_anagram("Hello", "World") is False
    assert is_anagram("Dormitory", "dirty room") is True


@check
def ex3_common_items():
    """找出两个列表都有的元素，取两边出现次数的较小值。"""
    a = ["a", "a", "b", "c", "c", "c"]
    b = ["a", "c", "c", "d"]
    result = None                      # TODO：提示用 Counter 的 & 运算
    assert result == {"a": 1, "c": 2}, f"期望 {{'a': 1, 'c': 2}}，实际是 {result!r}"


# =================================================================
# 第 2 节  defaultdict
# =================================================================

@check
def ex4_group_by_first_letter():
    """按首字母把单词分组，返回一个 defaultdict(list)。"""
    words = ["apple", "avocado", "banana", "cherry", "blueberry"]
    result = None                      # TODO
    assert isinstance(result, defaultdict), "要求返回 defaultdict"
    assert result == {
        "a": ["apple", "avocado"],
        "b": ["banana", "blueberry"],
        "c": ["cherry"],
    }


@check
def ex5_inverted_index():
    """建立倒排索引：单词 -> 它出现过的行号集合（行号从 1 开始）。"""
    lines = ["the cat sat", "the dog ran", "a cat and a dog"]
    result = None                      # TODO：提示 defaultdict(set)
    assert result is not None, "还没开始写"
    assert result["the"] == {1, 2}
    assert result["cat"] == {1, 3}
    assert result["dog"] == {2, 3}
    assert result["sat"] == {1}


@check
def ex6_degree():
    """用 defaultdict(int) 统计无向图中每个节点的度数。"""
    edges = [("A", "B"), ("A", "C"), ("B", "D")]
    result = None                      # TODO
    assert result == {"A": 2, "B": 2, "C": 1, "D": 1}, f"实际是 {result!r}"


# =================================================================
# 第 3 节  deque
# =================================================================

@check
def ex7_recent():
    """返回列表里最近的 n 个元素，最新的排在最后。"""
    def recent(items, n):
        return None                    # TODO：提示 deque(maxlen=n)

    assert recent([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert recent([1, 2], 5) == [1, 2]
    assert recent([], 3) == []


@check
def ex8_palindrome():
    """用 deque 从两端向中间比较，判断是否回文（忽略大小写和空格）。"""
    def is_palindrome(s):
        return None                    # TODO

    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


@check
def ex9_sliding_max():
    """挑战题：返回每个长度为 k 的窗口里的最大值。"""
    def sliding_max(nums, k):
        return None                    # TODO

    assert sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_max([1], 1) == [1]


# =================================================================
# 第 4 节  namedtuple
# =================================================================

@check
def ex10_distance():
    """用 namedtuple 定义 Point，并计算两点距离。"""
    Point = namedtuple("Point", ["x", "y"])

    def distance(p1, p2):
        return None                    # TODO：提示 import math; math.hypot(...)

    assert distance(Point(0, 0), Point(3, 4)) == 5.0
    assert distance(Point(1, 1), Point(1, 1)) == 0.0


@check
def ex11_replace_and_dict():
    """用 _replace 造一个新对象，再用 _asdict 转成字典。"""
    Movie = namedtuple("Movie", ["title", "year", "rating"])
    m = Movie("Inception", 2010, 8.8)

    new_movie = None                   # TODO：把 year 改成 2011
    movie_dict = None                  # TODO：把 new_movie 转成字典

    assert new_movie is not None, "还没开始写"
    assert movie_dict is not None, "还没开始写"
    assert new_movie.year == 2011
    assert m.year == 2010, "原来的对象不应该被改动"
    assert movie_dict == {"title": "Inception", "year": 2011, "rating": 8.8}


# =================================================================
# 第 5 节  OrderedDict / ChainMap
# =================================================================

@check
def ex12_lru():
    """实现一个容量为 capacity 的 LRU 缓存。"""

    class LRU:
        def __init__(self, capacity):
            self.capacity = capacity
            self.data = OrderedDict()   # 已经给好了，直接用

        def get(self, key):
            return None                # TODO

        def put(self, key, value):
            pass                       # TODO

    c = LRU(2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")          # 访问 a，让 a 变新鲜
    c.put("c", 3)       # 应该淘汰最久没用的 b

    assert c.get("b") is None, "b 应该已经被淘汰"
    assert c.get("a") == 1
    assert c.get("c") == 3


@check
def ex13_merge_config():
    """用 ChainMap 合并配置：override 覆盖 base。"""
    base = {"host": "localhost", "port": 8000, "debug": False}
    override = {"port": 9000}

    cfg = None                         # TODO：提示 ChainMap(override, base)

    assert cfg is not None, "还没开始写"
    assert cfg["host"] == "localhost"
    assert cfg["port"] == 9000
    assert cfg["debug"] is False

    cfg["debug"] = True                # 写操作会落到最前面那层
    assert override == {"port": 9000, "debug": True}, "写入应该落到 override"
    assert base["debug"] is False, "base 不应该被污染"


# =================================================================
# 判分器
# =================================================================

def run_all():
    print("=" * 62)
    print("collections 练习册")
    print("=" * 62)
    passed = 0
    for fn in _checks:
        name = f"{fn.__name__:<28}"
        try:
            fn()
        except AssertionError as e:
            msg = str(e) or "断言没通过"
            print(f"[FAIL] {name} {msg}")
        except Exception as e:
            print(f"[ERR ] {name} {type(e).__name__}: {e}")
            traceback.print_exc()
        else:
            passed += 1
            print(f"[ OK ] {name}")
    total = len(_checks)
    print("-" * 62)
    print(f"通过 {passed}/{total}")
    if passed == total:
        print("全部通过，这一轮 collections 就算拿下了。")


if __name__ == "__main__":
    run_all()


# =================================================================
# 参考答案（建议先自己写）
# =================================================================
"""
ex1_top_words
    result = [w for w, _ in Counter(words).most_common(2)]

ex2_is_anagram
    norm = lambda s: s.replace(" ", "").lower()
    return Counter(norm(s1)) == Counter(norm(s2))

ex3_common_items
    result = dict(Counter(a) & Counter(b))

ex4_group_by_first_letter
    result = defaultdict(list)
    for w in words:
        result[w[0]].append(w)

ex5_inverted_index
    result = defaultdict(set)
    for i, line in enumerate(lines, start=1):
        for word in line.split():
            result[word].add(i)

ex6_degree
    deg = defaultdict(int)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    result = dict(deg)

ex7_recent
    return list(deque(items, maxlen=n))

ex8_palindrome
    clean = "".join(s.split()).lower()
    dq = deque(clean)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

ex9_sliding_max（单调队列，窗口是 [i-k+1, i]）
    dq, out = deque(), []                # dq 里存下标，对应的值单调递减
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()                     # 比新来的小的，永远轮不到它当最大值
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()                 # 队首滑出窗口了
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

ex10_distance
    import math
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

ex11_replace_and_dict
    new_movie = m._replace(year=2011)
    movie_dict = new_movie._asdict()

ex12_lru
    def get(self, key):
        if key not in self.data:
            return None
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)

ex13_merge_config
    cfg = ChainMap(override, base)
"""
