# -*- coding: utf-8 -*-
"""
24 线程并发代码怎么测
============

直接运行本文件即可观察示例。
"""
import threading

class SafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
    def inc(self):
        with self._lock:
            self.value += 1

counter = SafeCounter()
threads = [threading.Thread(target=lambda: [counter.inc() for _ in range(1000)])
           for _ in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join(timeout=2)
    assert not t.is_alive()

print("value:", counter.value)
assert counter.value == 4000

# 并发测试原则：
# - 不要用 sleep 猜时序
# - 用 Event/Barrier/Queue 建立确定同步点
# - join 要有 timeout，避免测试永久挂住
# - 一次通过不能证明没有竞态；竞态测试需要设计可控交错
