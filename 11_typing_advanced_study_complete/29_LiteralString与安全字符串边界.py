# -*- coding: utf-8 -*-
"""29 LiteralString：标记“来自字面量/可信拼接”的字符串

它可用于 SQL、shell、模板等 API 的静态安全边界，但不能替代参数化查询或真实安全措施。
"""
from typing import LiteralString

def trusted_template(template: LiteralString, /, *values: object) -> str:
    return template.format(*values)

print(trusted_template('user={}', 'Alice'))
print('LiteralString 是静态防线；涉及 SQL 仍应使用数据库参数绑定。')
