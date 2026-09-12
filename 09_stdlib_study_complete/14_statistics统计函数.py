# -*- coding: utf-8 -*-
"""14 statistics：标准库描述统计"""
from statistics import mean, fmean, median, multimode, variance, stdev, quantiles, NormalDist

values = [1, 2, 2, 3, 10]
print("mean:", mean(values))
print("fmean:", fmean(values))
print("median:", median(values))
print("multimode:", multimode(values))
print("variance:", variance(values))
print("stdev:", stdev(values))
print("quartiles:", quantiles(values, n=4, method="inclusive"))

print("\n=== NormalDist ===")
normal = NormalDist(mu=100, sigma=15)
print("CDF(115):", normal.cdf(115))
print("90% quantile:", normal.inv_cdf(0.9))

print("\n注意：statistics 是轻量统计工具，不替代 NumPy/Pandas/SciPy 的大规模分析能力。")
print("variance/stdev 计算样本统计量；pvariance/pstdev 用于完整总体，含义不能混用。")
print("空数据、单元素方差和 NaN 都需要业务层先定义处理规则。")
