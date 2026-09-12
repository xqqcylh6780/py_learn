"""验证 TypeIs 双向缩窄和 assert_never 穷尽检查。"""

from collections.abc import Sequence
from typing import Literal, TypeIs, assert_never, assert_type


def is_str_sequence(items: Sequence[object]) -> TypeIs[Sequence[str]]:
    return all(isinstance(item, str) for item in items)


def consume(items: Sequence[object]) -> None:
    if is_str_sequence(items):
        assert_type(items, Sequence[str])
    else:
        assert_type(items, Sequence[object])


Mode = Literal["read", "write"]


def permission(mode: Mode) -> int:
    match mode:
        case "read":
            return 4
        case "write":
            return 2
        case _:
            assert_never(mode)

