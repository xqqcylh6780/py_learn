# -*- coding: utf-8 -*-
"""22 cProfile / pstats：先找热点，再优化。"""
import cProfile
import pstats
import io


def work():
    total = 0
    for i in range(30_000):
        total += i * i
    return total

prof = cProfile.Profile()
prof.enable()
work()
prof.disable()

buf = io.StringIO()
stats = pstats.Stats(prof, stream=buf).sort_stats("cumtime")
stats.print_stats(8)
print(buf.getvalue())

print("cumtime 包含子调用时间；tottime 是函数自身耗时。")
print("性能优化顺序：测量 -> 找热点 -> 改一处 -> 再测。")
