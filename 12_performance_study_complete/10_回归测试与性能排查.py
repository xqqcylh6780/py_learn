"""10 回归测试与性能排查

优化完成后的风险是回归。性能测试应保留代表性输入、允许合理噪声，并将
基准与功能测试分开。对线上或长期运行问题，结合 profile、tracemalloc、
指标和请求样本定位，而不是只靠一次本地实验。

排查顺序：确认症状和基线 -> 分离 CPU、内存、I/O 或锁等待 -> 缩小到具体
工作负载 -> 改动一个因素 -> 复测并记录结论。
"""
from statistics import median
from time import perf_counter


def benchmark(fn, repeats: int = 5) -> float:
    samples: list[float] = []
    for _ in range(repeats):
        start = perf_counter()
        fn()
        samples.append(perf_counter() - start)
    return median(samples)


baseline = benchmark(lambda: sum(range(50_000)))
candidate = benchmark(lambda: sum(value for value in range(50_000)))
print(f"baseline: {baseline * 1_000:.3f}ms")
print(f"candidate: {candidate * 1_000:.3f}ms")
print("结论：记录可复现基准和阈值，才能分辨真实回归与测量噪声。")
