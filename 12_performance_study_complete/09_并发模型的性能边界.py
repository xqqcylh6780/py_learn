"""09 并发模型的性能边界

线程、进程和 asyncio 解决的问题不同。CPython 的 GIL 意味着纯 Python 的
CPU 密集线程通常不能并行执行字节码；线程和 asyncio 常用于等待 I/O，进程
可用于可序列化且计算足够重的 CPU 工作。

并发也有成本：任务调度、上下文切换、进程启动、IPC、序列化和背压都可能
超过收益。先估算任务粒度和等待比例。
"""
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def fetch_simulated(identifier: int) -> int:
    sleep(0.01)  # 模拟等待 I/O；真实代码应使用真实客户端。
    return identifier * 2


with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch_simulated, range(4)))

print("I/O-like results:", results)
print("结论：根据工作负载选择并发模型，并测量吞吐、延迟和资源成本。")
