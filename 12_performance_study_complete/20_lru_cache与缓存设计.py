"""20 functools.cache/lru_cache：用空间换时间。"""
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n<2:return n
    return fib(n-1)+fib(n-2)
print(fib(30)); print(fib.cache_info())
fib.cache_clear()
print('缓存适合纯/近纯函数和重复输入；注意内存、陈旧数据和线程语义。')
