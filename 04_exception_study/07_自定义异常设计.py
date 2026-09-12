# -*- coding: utf-8 -*-
"""
07 自定义异常设计
================

目标：
- 建立稳定的异常层次
- 让调用方按“类别”捕获，而不是解析错误字符串
- 为异常对象添加结构化信息
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 自定义异常通常继承 Exception")
class AppError(Exception):
    """应用异常基类。"""


class ValidationError(AppError):
    pass


class ResourceNotFoundError(AppError):
    pass


print(issubclass(ValidationError, AppError))


show("2. 异常类可以携带结构化字段")
class FieldError(ValidationError):
    def __init__(self, field, value, message):
        self.field = field
        self.value = value
        self.message = message
        super().__init__(f"{field}: {message}; value={value!r}")


try:
    raise FieldError("age", -1, "不能小于 0")
except FieldError as exc:
    print(str(exc))
    print("field =", exc.field)
    print("value =", exc.value)


show("3. 调用方可以按层次选择处理粒度")
try:
    raise ResourceNotFoundError("user 42")
except ValidationError:
    print("数据校验错误")
except AppError as exc:
    print("统一应用错误:", exc)


show("4. 类名要表达语义")
print("BadError / MyException 信息量太低。")
print("ConfigError / AuthenticationError / DataValidationError 更清楚。")


show("5. 不要给每个失败点都造一个异常类")
print("异常类用于稳定的错误类别；临时细节可放 message/属性中。")

print("\n练习：99_exercises.py -> ex13 ~ ex14")
