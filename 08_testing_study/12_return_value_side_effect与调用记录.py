# -*- coding: utf-8 -*-
"""
12 return_value、side_effect 与调用记录
=================================

直接运行本文件即可观察示例。
"""
from unittest.mock import Mock, call

api = Mock()
api.fetch.side_effect = [
    TimeoutError("first"),
    {"ok": True},
]

try:
    api.fetch()
except TimeoutError as e:
    print("第一次:", type(e).__name__)

print("第二次:", api.fetch())
print("calls:", api.fetch.call_args_list)
api.fetch.assert_has_calls([call(), call()])

def answer(x):
    return x * 10

m = Mock(side_effect=answer)
print("side_effect 也可以是函数:", m(3))

# side_effect 常见三种用法：
# 1. 一个异常
# 2. 一个可迭代对象（每次调用取下一个结果）
# 3. 一个函数（根据参数动态返回）
