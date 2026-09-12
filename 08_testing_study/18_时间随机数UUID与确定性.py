# -*- coding: utf-8 -*-
"""
18 时间、随机数、UUID 与确定性
===================

直接运行本文件即可观察示例。
"""
import random
from unittest.mock import patch

def roll():
    return random.randint(1, 6)

with patch("random.randint", return_value=4):
    print("固定随机结果:", roll())

rng1 = random.Random(123)
rng2 = random.Random(123)
print([rng1.randint(1, 9) for _ in range(5)])
print([rng2.randint(1, 9) for _ in range(5)])

print("原则：测试应该尽可能确定性。")
print("时间、随机数、UUID、网络、系统环境都是常见不确定性来源。")
print("更好的设计通常是把 clock/rng/id_generator 作为依赖传入。")
