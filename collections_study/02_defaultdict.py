# -*- coding: utf-8 -*-
"""
collections.defaultdict —— 自带默认值的字典
============================================

运行：  python 02_defaultdict.py
练习：  python 99_exercises.py   （第 2 节）

一句话理解：普通 dict 遇到不存在的键会 KeyError，
defaultdict 会当场给你造一个默认值出来。
"""

from collections import defaultdict


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 痛点：按首字母给单词分组
# ---------------------------------------------------------------
show("1. 先看不用的写法有多啰嗦")

words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]

# 普通 dict 版：每次都要先判断键在不在
groups = {}
for w in words:
    first = w[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(w)
print("普通 dict :", groups)

# defaultdict 版：省掉 if
groups2 = defaultdict(list)
for w in words:
    groups2[w[0]].append(w)
print("defaultdict:", dict(groups2))


# ---------------------------------------------------------------
# 2. 三种最常用的 default_factory
# ---------------------------------------------------------------
show("2. list / int / set 三种默认工厂")

# 2.1 defaultdict(list) —— 分组
by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)
print("按长度分组:", {k: v for k, v in sorted(by_len.items())})

# 2.2 defaultdict(int) —— 计数
counts = defaultdict(int)
for w in words:
    counts[len(w)] += 1
print("长度分布  :", dict(sorted(counts.items())))

# 2.3 defaultdict(set) —— 分组并自动去重
tags = [("python", "语言"), ("python", "解释型"), ("java", "语言")]
by_tag = defaultdict(set)
for name, tag in tags:
    by_tag[name].add(tag)
print("标签集合  :", {k: sorted(v) for k, v in by_tag.items()})


# ---------------------------------------------------------------
# 3. 实战：建一张图的邻接表
# ---------------------------------------------------------------
show("3. 实战：邻接表（图算法里天天用）")

edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)      # 无向图，两边都记

for node in sorted(graph):
    print(f"   {node} -> {sorted(graph[node])}")


def bfs(start):
    seen, order, queue = {start}, [], [start]
    while queue:
        node = queue.pop(0)
        order.append(node)
        for nxt in graph[node]:     # graph[node] 一定存在，哪怕是空列表
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return order


print("从 A 开始遍历:", bfs("A"))


# ---------------------------------------------------------------
# 4. 必须知道的坑
# ---------------------------------------------------------------
show("4. 坑：只要用 [] 读，就会创建键")

d = defaultdict(list)
print("刚创建时:", dict(d), "-> len =", len(d))

_ = d["hello"]                  # 只是读了一下
print("读了一次 d['hello'] 之后:", dict(d), "-> len =", len(d), " <- 凭空多了一个键！")

print()
print("不会创建键的安全读法：")
print("  'hello' in d   ->", "hello" in d)
print("  d.get('world') ->", d.get("world"), " 且 d 里没多出 world:", "world" not in d)
print("  d.setdefault(k, v) -> 会创建，但默认值由你显式决定")

print()
print("第二个坑：default_factory 要传「类本身」，不是实例")
print("  对：defaultdict(list)")
print("  错：defaultdict(list())  —— 好在这个 Python 会当场报错，帮你挡住了：")

try:
    defaultdict(list())
except TypeError as e:
    print("    TypeError:", e)

print()
print("  但下面这种「悄悄共享同一个对象」的写法，Python 不会拦你：")
shared = [[]] * 3               # 三行是同一个列表的三个引用
shared[0].append("x")
print("    [[]] * 3 然后改第一行 ->", shared, " <- 三行全变了")
print("    正确写法：[[ ] for _ in range(3)]")


# ---------------------------------------------------------------
# 5. defaultdict vs Counter，怎么选
# ---------------------------------------------------------------
show("5. 什么时候用 defaultdict，什么时候用 Counter")

print("只数数、还要排名/取前 N  -> Counter")
print("要数数但也可能做别的事    -> defaultdict(int)")
print("要把元素归类成列表/集合   -> defaultdict(list) / defaultdict(set)")
print()

# 补充：default_factory 为 None 时，行为退化成普通 dict
d2 = defaultdict(None)
try:
    d2["nope"]
except KeyError as e:
    print("default_factory=None 时依然会 KeyError:", e)


show("做完了？去 99_exercises.py 做第 2 节练习")
