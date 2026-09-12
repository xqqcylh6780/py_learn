"""28 性能回归：性能指标也要像功能一样持续观察。"""
import statistics
baseline=[1.00, 0.98, 1.02, 1.01, 0.99]
current=[1.03, 1.05, 1.04, 1.02, 1.06]
print('baseline median:', statistics.median(baseline))
print('current median :', statistics.median(current))
print('CI 上做性能测试要控制机器噪声，设合理阈值，最好看趋势而不是单次失败。')
