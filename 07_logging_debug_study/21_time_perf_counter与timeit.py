# -*- coding: utf-8 -*-
"""21 时间测量：time.time / monotonic / perf_counter / timeit。"""
import time
import timeit

start = time.perf_counter()
sum(range(100_000))
elapsed = time.perf_counter() - start
print("perf_counter elapsed:", elapsed)

print("time.time() 适合墙上时钟时间戳，不适合严格测量短耗时。")
print("monotonic()/perf_counter() 不会因系统时钟回拨而倒退。")
print("process_time() 统计当前进程消耗的 CPU 时间，不包含 sleep 等等待时间。")

result = timeit.timeit("sum(range(1000))", number=1000)
print("timeit 1000 次:", result)
print("\n微基准要多次测量、预热，并避免把 I/O/环境噪声误当代码差异。")
print("短代码可用 timeit，完整请求则应同时观察端到端延迟、吞吐和尾延迟。")
