# -*- coding: utf-8 -*-
"""18 Concatenate：包装器主动增加前置参数

Concatenate 与 ParamSpec 配合，描述包装器添加或消费固定的前置位置参数。
典型场景包括依赖注入、锁包装器和给方法添加上下文。

它只能在 Callable 的参数位置使用，固定参数放在 ParamSpec 前面。若包装器
改变关键字参数结构，通常需要回调 Protocol 表达更精确的契约。
"""
from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

class Request:
    def __init__(self, user: str): self.user = user

def with_request(fn: Callable[Concatenate[Request, P], R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        req = Request('system')
        return fn(req, *args, **kwargs)
    return wrapper

@with_request
def hello(req: Request, name: str) -> str:
    return f'{req.user}->{name}'

print(hello('Alice'))
