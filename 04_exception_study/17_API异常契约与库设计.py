# -*- coding: utf-8 -*-
"""
17 API 异常契约与库设计
======================

高质量 API 不只是“能抛异常”，还要让调用方知道：
- 哪些失败是预期的
- 抛什么类型
- 哪些异常会被翻译
- 哪些数据放在异常属性里
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


class ParseError(ValueError):
    """输入文本符合字符串类型，但格式不满足本 API。"""


show("1. 尽量沿用有语义的内置异常")
def repeat(text, count):
    if not isinstance(text, str):
        raise TypeError("text 必须是 str")
    if not isinstance(count, int):
        raise TypeError("count 必须是 int")
    if count < 0:
        raise ValueError("count 不能小于 0")
    return text * count

print(repeat("a", 3))


show("2. 自定义异常可以继承合适的内置异常")
def parse_hex(text):
    try:
        return int(text, 16)
    except ValueError as exc:
        raise ParseError(f"非法十六进制: {text!r}") from exc

try:
    parse_hex("GG")
except ValueError as exc:
    print("调用方按 ValueError 家族捕获也可以:", type(exc).__name__)


show("3. 错误字符串不是机器接口")
print("不要让调用方写 `if 'not found' in str(exc)`。")
print("需要程序判断的内容应该用异常类型或结构化字段表达。")


show("4. 文档应写明稳定异常")
print("例如：参数类型错 -> TypeError；值越界 -> ValueError；资源不存在 -> ResourceNotFoundError。")


show("5. 不要无意泄漏实现细节")
print("如果库内部从 JSON 改成数据库，公开 API 的异常契约不应被迫全部改变。")


show("6. None、哨兵值还是异常？")
print("‘未找到’是正常情况时可返回 None；按契约必须存在时则更适合抛异常。")
print("关键不是统一答案，而是接口契约稳定、调用方不需要猜。")

print("\n练习：99_exercises.py -> ex33 ~ ex34")
