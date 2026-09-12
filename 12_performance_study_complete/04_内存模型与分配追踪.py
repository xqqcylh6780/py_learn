"""04 内存模型与分配追踪

内存问题至少要区分对象本身大小、对象图的总占用和分配增长。`sys.getsizeof`
只报告一个对象的浅层大小；`tracemalloc` 能比较两个时间点之间的 Python
分配差异，适合定位持续增长的代码位置。

观察点：缓存、全局容器和闭包常使对象存活得比预期久。一次峰值不等于泄漏；
同一请求重复执行后仍单调增长才是更强的信号。
"""
import tracemalloc


def build_records(size: int) -> list[dict[str, int]]:
    return [{"id": index, "square": index * index} for index in range(size)]


tracemalloc.start()
before = tracemalloc.take_snapshot()
records = build_records(5_000)
after = tracemalloc.take_snapshot()

for stat in after.compare_to(before, "lineno")[:3]:
    print(stat)
print("records:", len(records))
tracemalloc.stop()
print("结论：先确认增长来自哪里，再决定是释放、限额还是改变数据表示。")
