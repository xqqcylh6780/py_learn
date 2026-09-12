# -*- coding: utf-8 -*-
"""15 random：伪随机、可复现与抽样"""
import random

print("=== 独立 Random 实例便于测试复现 ===")
rng = random.Random(42)
print([rng.randint(1, 10) for _ in range(5)])

rng = random.Random(42)
print("choice:", rng.choice(["A", "B", "C"]))
print("choices:", rng.choices(["A", "B", "C"], weights=[1, 2, 7], k=5))
print("sample:", rng.sample(range(100), k=5))

items = [1, 2, 3, 4, 5]
rng.shuffle(items)
print("shuffle:", items)

print("\n=== 分布 ===")
print("uniform:", rng.uniform(0, 1))
print("gauss:", rng.gauss(0, 1))

print("\n重要：random 不是密码学安全随机数。Token、验证码、重置链接用 secrets。")
