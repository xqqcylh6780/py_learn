# -*- coding: utf-8 -*-
"""27 Never、NoReturn 与 assert_never

Never 表示“这里不可能有正常值”；assert_never 常用于枚举/联合的穷尽性检查。
"""
# 学习重点：Never/NoReturn 描述不会正常返回的路径。
# - NoReturn 常用于总是抛异常或终止进程的函数返回注解。
# - assert_never 可在联合或枚举分支末尾建立穷尽性检查。
# - 新增联合成员后，检查器会指出遗漏分支。
# 常见误区：在实际可能返回的函数上标 NoReturn 来压制控制流报错。
from typing import Literal, Never, NoReturn, assert_never

def fail(msg: str) -> NoReturn:
    raise RuntimeError(msg)

def render(status: Literal['ok', 'error']) -> str:
    match status:
        case 'ok': return 'OK'
        case 'error': return 'ERROR'
        case other:
            assert_never(other)

print(render('ok'))
print('如果以后 Literal 新增分支而这里没处理，类型检查器能提示遗漏。')
