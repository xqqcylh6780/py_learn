"""04 perf_counter：测经过时间，不要用 wall-clock 做耗时基准。"""
from time import perf_counter, process_time, sleep

start = perf_counter(); cpu0 = process_time(); sleep(0.02)
print('wall elapsed:', perf_counter() - start)
print('cpu elapsed :', process_time() - cpu0)
print('perf_counter 适合 elapsed time；process_time 不统计 sleep 等等待时间。')
