# -*- coding: utf-8 -*-
"""
09 Mock 基础
==========

直接运行本文件即可观察示例。
"""
from unittest.mock import Mock

sender = Mock()
sender.send.return_value = {"ok": True}

result = sender.send("alice", "hello")
print("返回值:", result)

sender.send.assert_called_once_with("alice", "hello")
print("call_count:", sender.send.call_count)
print("call_args:", sender.send.call_args)

# Mock 适合替代“协作者”：
# 邮件客户端、支付网关、HTTP 客户端、时钟等。
#
# 不要为了 mock 而 mock：
# 一个纯函数 2+3=5 没有必要把内部加法替换掉。
