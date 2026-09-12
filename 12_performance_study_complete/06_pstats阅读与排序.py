"""06 pstats：正确读 profiler 输出。"""
import cProfile, pstats

def a():
    return sum(range(1000))
def b():
    for _ in range(10): a()

pr = cProfile.Profile(); pr.runcall(b)
stats = pstats.Stats(pr)
stats.sort_stats('calls').print_stats(4)
print('常用排序：cumtime、tottime、calls。不要只盯总耗时。')
