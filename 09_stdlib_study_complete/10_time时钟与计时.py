# -*- coding: utf-8 -*-
"""10 time：墙上时间、单调时钟与性能计时"""
import time

print("time.time():", time.time(), "<- Unix 时间戳，可能受系统时钟调整影响")
print("time.monotonic():", time.monotonic(), "<- 只保证单调，适合超时")
print("time.perf_counter():", time.perf_counter(), "<- 高分辨率性能计时")
print("time.process_time():", time.process_time(), "<- 当前进程 CPU 时间")

start = time.perf_counter()
sum(i * i for i in range(10000))
elapsed = time.perf_counter() - start
print("elapsed:", elapsed)

print("\n=== timeout 正确思路 ===")
deadline = time.monotonic() + 0.02
while time.monotonic() < deadline:
    pass
print("timeout reached")

print("\n不要用 time.time() 计算超时期限；系统时间可以被 NTP/用户调整。")
