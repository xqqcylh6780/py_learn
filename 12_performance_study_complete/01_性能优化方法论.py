"""01 性能优化方法论：不要从“改快”开始，要从“测清楚”开始。"""
from time import perf_counter

print('性能工作流：定义目标 -> 建立基线 -> 找热点 -> 修改 -> 回归验证')

def work(n=100_000):
    return sum(i * i for i in range(n))

t0 = perf_counter(); result = work(); dt = perf_counter() - t0
print('结果:', result, '耗时(秒):', round(dt, 6))
print('原则：没有基线的“优化”，无法证明真的更快。')
print('还要同时看：延迟、吞吐、CPU、内存、I/O、可维护性。')
