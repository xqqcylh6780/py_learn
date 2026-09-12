"""检查 TypedDict 的必需键、可选键、只读键和多余键。"""

from typing import NotRequired, ReadOnly, TypedDict


class UserRow(TypedDict):
    id: ReadOnly[int]
    name: str
    email: NotRequired[str]


good: UserRow = {"id": 1, "name": "Alice"}
missing: UserRow = {"id": 2}  # expected type-check error：缺少 name
extra: UserRow = {"id": 3, "name": "Bob", "role": "admin"}  # expected type-check error
good["id"] = 9  # expected type-check error：id 是 ReadOnly

