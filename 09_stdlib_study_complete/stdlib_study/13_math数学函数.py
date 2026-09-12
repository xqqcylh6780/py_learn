# -*- coding: utf-8 -*-
"""13 math：高频数学工具与数值细节"""
import math

print("常量:", math.pi, math.e, math.tau)
print("sqrt/hypot:", math.sqrt(9), math.hypot(3, 4))
print("floor/ceil/trunc:", math.floor(-1.2), math.ceil(-1.2), math.trunc(-1.2))
print("gcd/lcm:", math.gcd(12, 18), math.lcm(12, 18))
print("factorial/comb/perm:", math.factorial(5), math.comb(5, 2), math.perm(5, 2))

print("\n=== fsum 比 sum 更适合浮点累计 ===")
values = [1e16, 1.0, -1e16]
print("sum =", sum(values))
print("fsum=", math.fsum(values))

print("\n=== isclose ===")
print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9, abs_tol=0.0))
print("浮点比较通常不要直接 ==；容差要由业务尺度决定。")

print("\n=== isnan/isinf ===")
for x in [1.0, math.nan, math.inf]:
    print(x, math.isnan(x), math.isinf(x), math.isfinite(x))
