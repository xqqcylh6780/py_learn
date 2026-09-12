# -*- coding: utf-8 -*-
"""18 Concatenate：包装器主动增加前置参数"""
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
