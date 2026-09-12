"""验证 ParamSpec 保留签名，以及 overload 对返回类型的精确描述。"""

from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar, assert_type, overload


P = ParamSpec("P")
R = TypeVar("R")


def traced(fn: Callable[P, R]) -> Callable[P, R]:
    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return fn(*args, **kwargs)

    return wrapper


@traced
def repeat(text: str, count: int) -> str:
    return text * count


assert_type(repeat("a", 3), str)
repeat(3, "a")  # expected type-check error


@overload
def parse(value: bytes) -> str: ...


@overload
def parse(value: str) -> list[str]: ...


def parse(value: bytes | str) -> str | list[str]:
    return value.decode() if isinstance(value, bytes) else value.split(",")


assert_type(parse(b"ok"), str)
assert_type(parse("a,b"), list[str])

