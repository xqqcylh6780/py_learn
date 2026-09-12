# -*- coding: utf-8 -*-
"""
17 环境变量与 patch.dict
===================

直接运行本文件即可观察示例。
"""
import os
from unittest.mock import patch

def get_mode():
    return os.environ.get("APP_MODE", "dev")

print("原始:", get_mode())

with patch.dict(os.environ, {"APP_MODE": "test"}):
    print("临时:", get_mode())

print("恢复:", get_mode())

with patch.dict(os.environ, {"ONLY": "1"}, clear=True):
    print("clear=True 后 APP_MODE:", os.environ.get("APP_MODE"))
    print("ONLY:", os.environ["ONLY"])

# 测试环境变量时必须保证测试结束后恢复现场；
# patch.dict 正适合这种场景。
