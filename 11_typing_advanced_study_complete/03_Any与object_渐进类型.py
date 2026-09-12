# -*- coding: utf-8 -*-
"""03 Any 与 object：两者不是一回事

Any 基本等于“告诉类型检查器这里放弃检查”；object 则表示“任意 Python 对象，
但使用前只能做 object 保证存在的操作，或先缩窄类型”。
"""
from typing import Any

def unsafe(value: Any) -> Any:
    # 静态检查器通常不会阻止这一行，即使 value 可能没有 upper。
    return value.upper()

def safe(value: object) -> str:
    if isinstance(value, str):
        return value.upper()
    return repr(value)

print(safe('abc'))
print(safe(123))
try:
    print(unsafe(123))
except AttributeError as e:
    print('Any 把错误推迟到了运行时:', type(e).__name__)
