# -*- coding: utf-8 -*-
"""23 控制流类型缩窄

isinstance、is None、字面量比较、提前 return/raise、match 等都能帮助检查器缩小可能类型。
好的类型设计往往能减少 cast。
"""

def length(value: str | bytes | None) -> int:
    if value is None:
        return 0
    # 这里静态类型已缩窄到 str | bytes
    return len(value)

def upper(value: object) -> str:
    if not isinstance(value, str):
        raise TypeError('need str')
    # 经过 raise 后，这里就是 str
    return value.upper()

print(length(None), length('abc'))
print(upper('hello'))
