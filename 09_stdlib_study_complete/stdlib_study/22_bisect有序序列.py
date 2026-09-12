# -*- coding: utf-8 -*-
"""22 bisect：在已排序序列中二分定位与插入"""
from bisect import bisect_left, bisect_right, insort

scores = [60, 70, 70, 80, 90]
print("left 70 :", bisect_left(scores, 70))
print("right 70:", bisect_right(scores, 70))

insort(scores, 75)
print(scores)

print("\n=== 区间分类 ===")
breakpoints = [60, 70, 80, 90]
labels = ["F", "D", "C", "B", "A"]
for score in [59, 60, 75, 95]:
    print(score, labels[bisect_right(breakpoints, score)])

print("\n=== key 参数 ===")
records = [{"id": 1, "score": 60}, {"id": 2, "score": 80}]
pos = bisect_left(records, 70, key=lambda r: r["score"])
print("insert position:", pos)

print("查找 O(log n)，但 list 中间插入仍是 O(n) 搬移。高频插入需考虑其他数据结构。")
