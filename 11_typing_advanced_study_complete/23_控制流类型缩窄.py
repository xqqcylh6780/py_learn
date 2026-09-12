# -*- coding: utf-8 -*-
"""23 控制流类型缩窄

isinstance、is None、字面量比较、提前 return/raise、match 等都能帮助检查器缩小可能类型。
好的类型设计往往能减少 cast。
"""

# 学习重点：检查器沿控制流排除不可能的类型。
# - 提前处理 None 能让后续主路径保持简单。
# - isinstance、判别字段、match 和不可达分支都可以参与缩窄。
# - 变量被重新赋值或逃逸到可变位置后，缩窄结果可能失效。
# 常见误区：大量使用 cast 掩盖本可由清晰控制流证明的类型关系。
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
