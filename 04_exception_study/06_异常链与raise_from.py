# -*- coding: utf-8 -*-
"""
06 异常链与 raise ... from ...
==============================

目标：
- 保留底层错误原因
- 把底层异常翻译成更适合当前抽象层的异常
- 理解 __cause__、__context__ 与 `from None`
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 自动异常上下文 __context__")
try:
    try:
        int("x")
    except ValueError:
        raise RuntimeError("上层操作失败")
except RuntimeError as exc:
    print("当前异常:", exc)
    print("隐式 context:", type(exc.__context__).__name__)


show("2. 显式因果：raise NewError(...) from old")
class ConfigError(Exception):
    pass


def parse_port(text):
    try:
        port = int(text)
    except ValueError as exc:
        raise ConfigError("端口必须是整数") from exc
    if not (1 <= port <= 65535):
        raise ConfigError("端口必须在 1~65535")
    return port

try:
    parse_port("abc")
except ConfigError as exc:
    print("业务层异常:", exc)
    print("直接原因:", type(exc.__cause__).__name__, exc.__cause__)


show("3. 为什么异常翻译很重要")
print("调用方不应该为了读取配置，知道底层恰好使用 int()。")
print("它只需要处理 ConfigError；调试时仍能看到原始 ValueError。")


show("4. from None：有意识地隐藏上下文展示")

def public_lookup(mapping, key):
    try:
        return mapping[key]
    except KeyError:
        raise ValueError(f"未知字段: {key}") from None

try:
    public_lookup({"name": "A"}, "age")
except ValueError as exc:
    print(exc)
    print("suppress_context:", exc.__suppress_context__)


show("5. 不要为了‘干净’就到处 from None")
print("隐藏异常链会损失诊断信息；只在底层细节确实不该暴露时使用。")

print("\n练习：99_exercises.py -> ex11 ~ ex12")
