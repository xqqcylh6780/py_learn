# -*- coding: utf-8 -*-
"""
10 patch 必须补在使用处
================

直接运行本文件即可观察示例。
"""
from unittest.mock import patch

# 用一个最小动态模块演示“在哪里查找，就在哪里 patch”
import types, sys
service = types.ModuleType("_demo_service")
service.get_rate = lambda: 0.1
sys.modules["_demo_service"] = service

consumer = types.ModuleType("_demo_consumer")
exec("from _demo_service import get_rate\n\ndef price(x):\n    return x * (1 + get_rate())", consumer.__dict__)
sys.modules["_demo_consumer"] = consumer

print("原始:", consumer.price(100))

with patch("_demo_consumer.get_rate", return_value=0.2):
    print("正确 patch consumer 使用的名字:", consumer.price(100))

with patch("_demo_service.get_rate", return_value=0.5):
    print("patch 定义处未必影响已导入名字:", consumer.price(100))

# 核心规则：
# patch “被测代码查找这个名字的位置”，不是机械 patch 原定义位置。
