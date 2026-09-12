# -*- coding: utf-8 -*-
"""23 tracemalloc：追踪 Python 内存分配来源。"""
import tracemalloc

tracemalloc.start()
before = tracemalloc.take_snapshot()

data = [str(i) * 10 for i in range(5000)]

after = tracemalloc.take_snapshot()
stats = after.compare_to(before, "lineno")
print("内存增长 Top 5:")
for stat in stats[:5]:
    print(stat)

current, peak = tracemalloc.get_traced_memory()
print("current:", current, "peak:", peak)
tracemalloc.stop()

print("\ntracemalloc 主要追踪 Python 分配器可见的内存；并不等于进程 RSS 的全部来源。")
