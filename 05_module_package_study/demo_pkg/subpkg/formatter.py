"""演示相对导入。"""

from ..greeter import greet


def excited(name: str) -> str:
    return greet(name).upper()
