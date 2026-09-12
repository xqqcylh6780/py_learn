"""此文件故意包含静态类型错误，用来观察 pyright/mypy 报告；不要当运行时教程执行。"""
from typing import Final

LIMIT: Final = 3
LIMIT = 4  # expected type-check error

x: int = 'not int'  # expected type-check error
