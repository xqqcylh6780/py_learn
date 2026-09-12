# -*- coding: utf-8 -*-
"""24 cast、assert_type、reveal_type

cast 不做运行时转换；它只是告诉检查器“把这里视为某类型”。
assert_type 用于检查类型推导测试；reveal_type 用于诊断推导结果。
"""
# 学习重点：这三个工具改变的是检查器认知，不是业务数据。
# - cast(T, value) 原样返回 value，不执行转换或验证。
# - assert_type 用于类型推导的静态测试，不应替代运行时断言。
# - reveal_type 用于排查检查器推导，通常不应留在生产路径。
# 常见误区：用 cast 修复来源不可信的数据；正确做法是解析和校验。
from typing import assert_type, cast, reveal_type

raw: object = 'hello'
text = cast(str, raw)
print(text.upper())
print('cast 后仍是同一个对象:', text is raw)

x = assert_type(1 + 2, int)
print('assert_type runtime:', x)
# reveal_type 在 CPython 运行时会返回参数，并向 stderr 打印运行时类型；主要用途仍是静态检查。
y = reveal_type('abc')
print('reveal_type returned:', y)
