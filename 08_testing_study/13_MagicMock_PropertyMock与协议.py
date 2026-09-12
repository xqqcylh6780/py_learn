# -*- coding: utf-8 -*-
"""
13 MagicMock、PropertyMock 与协议
=============================

直接运行本文件即可观察示例。
"""
from unittest.mock import MagicMock, PropertyMock, patch

m = MagicMock()
m.__enter__.return_value = "resource"
with m as value:
    print("上下文管理器值:", value)
m.__enter__.assert_called_once()
m.__exit__.assert_called_once()

class User:
    @property
    def name(self):
        return "real"

with patch.object(User, "name", new_callable=PropertyMock) as p:
    p.return_value = "mocked"
    print(User().name)

# MagicMock 支持很多魔术方法；
# PropertyMock 用于描述符/property。
# 仍然应优先测试公开行为，避免把对象模型内部细节全部 mock 掉。
