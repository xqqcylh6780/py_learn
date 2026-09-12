# -*- coding: utf-8 -*-
"""29 LiteralString：标记“来自字面量/可信拼接”的字符串

它可用于 SQL、shell、模板等 API 的静态安全边界，但不能替代参数化查询或真实安全措施。
"""
# 学习重点：LiteralString 可限制 API 只接收字面量来源的模板字符串。
# - 它能在静态阶段阻止部分动态拼接进入敏感接口。
# - 对 SQL 应继续使用参数绑定，对 shell 应使用参数数组并避免 shell=True。
# - 类型信息无法证明外部数据安全，也不会在运行时净化输入。
# 常见误区：把 LiteralString 当成完整的注入防护方案。
from typing import LiteralString

def trusted_template(template: LiteralString, /, *values: object) -> str:
    return template.format(*values)

print(trusted_template('user={}', 'Alice'))
print('LiteralString 是静态防线；涉及 SQL 仍应使用数据库参数绑定。')
