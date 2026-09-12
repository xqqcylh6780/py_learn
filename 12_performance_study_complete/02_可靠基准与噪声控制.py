"""02 可靠基准与噪声控制

`timeit` 适合重复执行一小段确定代码；`perf_counter()` 适合包围一个完整
工作负载。两者都需要多次运行并比较分布，而不是相信一次最快或最慢的值。

基准前固定输入规模、预热代码路径、避免把打印和随机 I/O 放进被测区间。
比较两个实现时，必须让它们完成完全相同的工作。

常见误区：在循环中创建测试数据；只测太快的操作；把不同机器、不同
Python 版本的数字直接比较。
"""
from statistics import median
from time import perf_counter


def measure(fn, repeats: int = 7) -> list[float]:
    samples: list[float] = []
    for _ in range(repeats):
        start = perf_counter()
        fn()
        samples.append(perf_counter() - start)
    return samples


data = list(range(20_000))


def workload() -> None:
    sum(value * value for value in data)


samples = measure(workload)
print("samples:", [f"{value * 1_000:.2f}ms" for value in samples])
print(f"median: {median(samples) * 1_000:.2f}ms")
print("结论：报告中应说明工作负载、重复次数、Python 版本和统计口径。")
