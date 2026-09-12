"""07 容器、缓存与惰性求值

字符串拼接、推导式、生成器、`lru_cache` 和 `__slots__` 都是在不同场景下
控制分配或重复工作。不要把它们当作通用加速开关。

大量已知片段可先收集后用 `join`；一次遍历可用生成器降低峰值内存；纯函数
且重复输入多时可缓存。缓存必须有失效策略和大小上限。
"""
from functools import lru_cache


def render(parts: list[str]) -> str:
    return "".join(parts)


@lru_cache(maxsize=128)
def fibonacci(number: int) -> int:
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


numbers = (value * value for value in range(10))
print(render(["Python", " ", "performance"]))
print("sum:", sum(numbers))
print("fibonacci:", fibonacci(20), fibonacci.cache_info())
print("结论：减少不必要的工作和分配，但先定义缓存边界与可读性要求。")
