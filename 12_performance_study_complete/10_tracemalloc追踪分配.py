"""10 tracemalloc：定位 Python 内存分配热点。"""
import tracemalloc
tracemalloc.start()
before=tracemalloc.take_snapshot()
data=[str(i)*10 for i in range(3000)]
after=tracemalloc.take_snapshot()
for stat in after.compare_to(before, 'lineno')[:3]: print(stat)
print('当前/峰值:', tracemalloc.get_traced_memory())
tracemalloc.stop()
