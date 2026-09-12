"""03 CPU 热点分析与优化

性能分析先回答“时间花在哪里”，而不是猜测。`cProfile` 提供调用次数、
函数自身耗时（tottime）与含子调用的累计耗时（cumtime）。

从 cumtime 靠前的业务入口向下钻取；若一个函数调用次数异常多，优先思考
能否减少工作量或批处理。不要因为一个函数出现在报告里就立即内联它。

常见误区：对微小样本 profile；只看 tottime 而忽略调用树；在优化后不复测。
"""
import cProfile
import io
import pstats


def normalize(rows: list[str]) -> list[str]:
    return [row.strip().lower() for row in rows if row.strip()]


def workload() -> int:
    rows = ["  Python  ", "", "Performance", " profiling "] * 2_000
    return len(normalize(rows))


profiler = cProfile.Profile()
profiler.enable()
count = workload()
profiler.disable()

report = io.StringIO()
pstats.Stats(profiler, stream=report).sort_stats("cumtime").print_stats(5)
print("processed:", count)
print(report.getvalue())
print("结论：让 profile 报告决定下一步，而不是凭直觉优化。")
