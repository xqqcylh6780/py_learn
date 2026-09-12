# -*- coding: utf-8 -*-
"""24 cast、assert_type、reveal_type

cast 不做运行时转换；它只是告诉检查器“把这里视为某类型”。
assert_type 用于检查类型推导测试；reveal_type 用于诊断推导结果。
"""
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
