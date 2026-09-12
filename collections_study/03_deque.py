# -*- coding: utf-8 -*-
"""
collections.deque —— 两头都能 O(1) 进出的队列
================================================

运行：  python 03_deque.py
练习：  python 99_exercises.py   （第 3 节）

一句话理解：list 只在「尾部」增删很快，从「头部」增删要搬动整个列表。
deque 把两端都做成 O(1)，代价是不能随机访问（d[i] 是 O(n)）。
"""

import time
from collections import deque


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 先感受一下 list 从头部取走元素有多慢
# ---------------------------------------------------------------
show("1. 性能对比：list.pop(0) vs deque.popleft()")

N = 20_000

lst = list(range(N))
t0 = time.perf_counter()
while lst:
    lst.pop(0)              # 每弹一个，后面所有元素都要往前挪一格
t1 = time.perf_counter()
print(f"list.pop(0)     弹出 {N} 次: {t1 - t0:.3f} 秒")

dq = deque(range(N))
t0 = time.perf_counter()
while dq:
    dq.popleft()            # O(1)，挪都不用挪
t1 = time.perf_counter()
print(f"deque.popleft() 弹出 {N} 次: {t1 - t0:.3f} 秒")

print()
print("复杂度：list.pop(0) 是 O(n)，整体 O(n^2)；deque.popleft() 是 O(1)，整体 O(n)")


# ---------------------------------------------------------------
# 2. 四个基本动作
# ---------------------------------------------------------------
show("2. 四个基本动作：append / appendleft / pop / popleft")

d = deque([2, 3, 4])
print("初始          :", list(d))

d.append(5)             # 右边进
print("append(5)     :", list(d))

d.appendleft(1)         # 左边进
print("appendleft(1) :", list(d))

print("pop()         :", d.pop(), "->", list(d), " 右边出")
print("popleft()     :", d.popleft(), "->", list(d), " 左边出")

print()
print("记住口诀：append/appendleft 是「进」，pop/popleft 是「出」")
print("deque 可以直接当「栈」用（只 append + pop），也可以当「队列」用（append + popleft）")


# ---------------------------------------------------------------
# 3. maxlen：满了自动从另一头丢弃
# ---------------------------------------------------------------
show("3. maxlen —— 天生的「只保留最近 N 条」")

recent = deque(maxlen=3)
for page in ["首页", "商品页", "购物车", "结算页", "支付页"]:
    recent.append(page)
    print(f"  浏览 {page:<6} -> 历史记录 {list(recent)}")

print()
print("注意：maxlen 已经固定，不能再改。满了之后 append 会把最老的挤出去。")
print("另一个用法：从左边进，自动丢掉右边最老的 -> 正好是「倒序最近 N 条」")

backlog = deque(maxlen=3)
for log in ["L1", "L2", "L3", "L4"]:
    backlog.appendleft(log)
print("  appendleft 的记录:", list(backlog))


# ---------------------------------------------------------------
# 4. 滑动窗口：用 maxlen 算最近 3 个数的平均值
# ---------------------------------------------------------------
show("4. 实战：滑动窗口平均")

window = deque(maxlen=3)
data = [10, 20, 30, 40, 50, 60]
for x in data:
    window.append(x)
    print(f"  新数据 {x:<3} 窗口 {list(window):<14} 平均 {sum(window) / len(window):.1f}")


# ---------------------------------------------------------------
# 5. rotate：整体旋转
# ---------------------------------------------------------------
show("5. rotate —— 整体转圈")

r = deque([1, 2, 3, 4, 5])
print("原始          :", list(r))

r.rotate(1)
print("rotate(1)     :", list(r), " 每个元素往右移一位（末尾跑到开头）")

r.rotate(-2)
print("rotate(-2)    :", list(r), " 负数就是往左")
print("用途：轮询调度、把某个元素挪到队首")


# ---------------------------------------------------------------
# 6. 坑：extendleft 的顺序是反的
# ---------------------------------------------------------------
show("6. 坑：extendleft 会倒序插入")

a = deque([1, 2])
a.extend([3, 4])
print("extend([3, 4])     :", list(a), " 正常顺序接到右边")

b = deque([1, 2])
b.extendleft([3, 4])
print("extendleft([3, 4]) :", list(b), " <- 变成 4, 3，是倒着的")

print()
print("原因：extendleft 是把元素一个个 appendleft 进去，后进的排在更前面。")
print("想要正序，就自己反一下：d.extendleft(reversed([3, 4]))")

b2 = deque([1, 2])
b2.extendleft(reversed([3, 4]))
print("  extendleft(reversed(...)) :", list(b2))


# ---------------------------------------------------------------
# 7. 实战：把 02 里那个慢 BFS 换掉
# ---------------------------------------------------------------
show("7. 实战：BFS 队列（对比 02_defaultdict.py 里的 list.pop(0)）")

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}


def bfs(start):
    seen = {start}
    queue = deque([start])          # 用 deque 而不是 list
    order = []
    while queue:
        node = queue.popleft()      # O(1)，替代 list.pop(0)
        order.append(node)
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return order


print("遍历顺序:", bfs("A"))


# ---------------------------------------------------------------
# 8. 什么时候别用 deque
# ---------------------------------------------------------------
show("8. 什么时候别用 deque")

print("需要按下标随机访问或切片  -> 用 list（deque[500] 是 O(n)）")
print("需要排序                  -> 用 list（deque 没有 sort）")
print("需要按位置插入            -> 用 list（deque 只擅长两端）")
print("需要大量在头部增删        -> 用 deque")
print()
print("要排序的话，转一下就好： sorted(dq)")


show("做完了？去 99_exercises.py 做第 3 节练习")
