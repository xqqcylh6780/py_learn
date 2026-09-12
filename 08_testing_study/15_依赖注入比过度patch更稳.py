# -*- coding: utf-8 -*-
"""
15 依赖注入比过度 patch 更稳
===================

直接运行本文件即可观察示例。
"""
class Clock:
    def now(self):
        import time
        return time.time()

def expired(deadline, clock):
    return clock.now() >= deadline

class FakeClock:
    def __init__(self, value):
        self.value = value
    def now(self):
        return self.value

clock = FakeClock(100)
print(expired(90, clock))
print(expired(110, clock))

# 如果代码把网络、时间、文件系统都藏在函数内部，
# 测试只能大量 patch。
# 把真正的外部依赖显式传进来，测试通常更简单、更稳定。
