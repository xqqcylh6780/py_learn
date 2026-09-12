# -*- coding: utf-8 -*-
"""15 warnings：警告不是异常。"""
import warnings
import logging

print("发出一个自定义警告：")
warnings.warn("旧接口将在未来移除", DeprecationWarning, stacklevel=1)

print("\n临时把 UserWarning 当异常：")
try:
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        warnings.warn("配置风险", UserWarning)
except UserWarning as e:
    print("捕获为异常:", e)

print("\n测试中可用 catch_warnings(record=True) 检查是否发出了预期警告。")
print("应用也可以 logging.captureWarnings(True) 把 warnings 路由到 logging。")
