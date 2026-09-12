"""15 抽象有成本，但可维护性通常比纳秒级函数调用更重要。"""
import timeit

def inc(x): return x+1
print('direct expr:', timeit.timeit('x+1', setup='x=1', number=100000))
print('function   :', timeit.timeit('inc(1)', globals=globals(), number=100000))
print('只有热点内层循环才值得考虑减少调用层级；先 profiler。')
