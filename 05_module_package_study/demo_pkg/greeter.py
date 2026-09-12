"""演示模块：被导入时只定义对象，不做昂贵副作用。"""


def greet(name: str) -> str:
    return f"Hello, {name}!"
