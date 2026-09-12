# -*- coding: utf-8 -*-
"""01 functools：cache、lru_cache、cached_property、partial

目标：掌握高频的“函数增强”工具，并理解缓存的边界。
Python 3.13 标准库。
"""
from functools import cache, lru_cache, cached_property, partial

print("=== 1. cache：无上限记忆化 ===")
_calls = 0

@cache
def fib(n: int) -> int:
    global _calls
    _calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("fib(20) =", fib(20), "实际函数执行次数 =", _calls)
print("cache_info =", fib.cache_info())

print("\n=== 2. lru_cache：可限制大小 ===")
@lru_cache(maxsize=2)
def load_user(uid: int) -> str:
    print("真正加载:", uid)
    return f"user-{uid}"

for uid in [1, 2, 1, 3, 2]:
    print(load_user(uid))
print(load_user.cache_info())
load_user.cache_clear()

print("\n=== 3. 缓存参数必须可哈希 ===")
try:
    load_user([1])
except TypeError as e:
    print(type(e).__name__, e)

print("\n=== 4. cached_property：实例级惰性缓存 ===")
class Report:
    def __init__(self, values):
        self.values = values

    @cached_property
    def average(self):
        print("计算 average")
        return sum(self.values) / len(self.values)

r = Report([10, 20, 30])
print(r.average)
print(r.average, "<- 第二次不再计算")
del r.average
print(r.average, "<- 删除缓存后重新计算")

print("\n=== 5. partial：预绑定部分参数 ===")
def request(url, *, timeout=5, retry=1):
    return url, timeout, retry

fast_request = partial(request, timeout=1, retry=0)
print(fast_request("https://example.com"))

print("\n注意：缓存适合“相同输入 -> 相同输出”的纯函数式场景。")
print("不要直接缓存依赖当前时间、外部文件、数据库实时状态的函数，除非你设计了失效策略。")
