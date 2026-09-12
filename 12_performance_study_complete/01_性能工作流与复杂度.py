"""01 性能工作流与复杂度

性能优化从来不是先改代码。先定义工作负载和目标，再测量基线，定位瓶颈，
修改一个变量，最后用同一工作负载复测并防止回归。

观察点：复杂度决定数据规模变大后的趋势；微优化只能改变常数项。对同一
问题，O(n) 与 O(n²) 的选择通常比更换一条语法重要得多。

常见误区：只看一次运行结果；优化未被测量的路径；把解释器实现细节当作
语言保证。下面用查找操作观察线性查找与集合查找的语义差异。
"""
from time import perf_counter


def contains_in_list(items: list[int], needle: int) -> bool:
    return needle in items


def contains_in_set(items: set[int], needle: int) -> bool:
    return needle in items


values = list(range(100_000))
lookup = set(values)

for label, fn, data in (
    ("list", contains_in_list, values),
    ("set", contains_in_set, lookup),
):
    start = perf_counter()
    assert fn(data, 99_999)
    elapsed = perf_counter() - start
    print(f"{label:4}: {elapsed:.8f}s")

print("结论：先选合适的算法和数据结构；再考虑实现层面的优化。")
