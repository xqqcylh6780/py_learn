# -*- coding: utf-8 -*-
"""27 Never、NoReturn 与 assert_never

Never 表示“这里不可能有正常值”；assert_never 常用于枚举/联合的穷尽性检查。
"""
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
