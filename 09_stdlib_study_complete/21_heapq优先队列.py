# -*- coding: utf-8 -*-
"""21 heapq：最小堆、Top K 与优先队列"""
import heapq

print("=== heapify / heappush / heappop ===")
data = [5, 1, 9, 3]
heapq.heapify(data)
print("heap内部:", data)
heapq.heappush(data, 2)
while data:
    print(heapq.heappop(data), end=" ")
print()

print("\n=== nsmallest / nlargest ===")
values = [8, 1, 5, 3, 9, 2]
print(heapq.nsmallest(3, values))
print(heapq.nlargest(2, values))

print("\n=== 带优先级任务 ===")
heap = []
heapq.heappush(heap, (2, 0, "normal"))
heapq.heappush(heap, (1, 1, "urgent"))
heapq.heappush(heap, (2, 2, "normal-2"))
while heap:
    print(heapq.heappop(heap))

print("元组后续字段会参与比较；真实任务对象不可比较时常加入自增序号作为 tie-breaker。")
