"""05 cProfile：先找热点函数。"""
import cProfile, pstats, io

def inner(n):
    return sum(i*i for i in range(n))
def workload():
    for _ in range(30): inner(1000)

pr = cProfile.Profile(); pr.enable(); workload(); pr.disable()
buf = io.StringIO()
pstats.Stats(pr, stream=buf).sort_stats('cumtime').print_stats(5)
print(buf.getvalue())
print('tottime 看函数自身；cumtime 包含其调用的子函数。')
