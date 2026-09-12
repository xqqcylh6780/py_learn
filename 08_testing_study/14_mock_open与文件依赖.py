# -*- coding: utf-8 -*-
"""
14 mock_open 与文件依赖
==================

直接运行本文件即可观察示例。
"""
from unittest.mock import mock_open, patch

def load_title(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readline().strip()

m = mock_open(read_data="Hello\nSecond\n")
with patch("builtins.open", m):
    print(load_title("fake.txt"))

m.assert_called_once_with("fake.txt", "r", encoding="utf-8")

# 何时更适合真正 tempfile？
# 当你需要验证编码、seek、真实 Path 行为、权限、目录关系时，
# 临时目录通常比过度模拟 open 更可靠。
