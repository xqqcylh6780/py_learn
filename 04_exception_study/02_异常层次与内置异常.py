# -*- coding: utf-8 -*-
"""
02 异常层次与常见内置异常
========================

重点：
- BaseException 与 Exception 的边界
- 常见内置异常分别表达什么
- 为什么通常捕获 Exception，而不是 BaseException
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 异常继承树的关键部分")
print("BaseException")
print("├─ SystemExit")
print("├─ KeyboardInterrupt")
print("├─ GeneratorExit")
print("└─ Exception")
print("   ├─ ValueError / TypeError / KeyError / ...")
print("   └─ 绝大多数业务异常也应继承 Exception")


show("2. 为什么一般不要 except BaseException")
print("BaseException 还包含 KeyboardInterrupt 和 SystemExit。")
print("粗暴捕获它可能让 Ctrl+C、sys.exit() 都失效。")


show("3. 常见异常的语义")
examples = [
    ("ValueError", "类型没错，但值不合法，例如 int('x')"),
    ("TypeError", "对象类型或调用方式不符合接口要求"),
    ("KeyError", "字典键不存在"),
    ("IndexError", "序列下标越界"),
    ("AttributeError", "对象没有该属性"),
    ("FileNotFoundError", "目标文件不存在"),
    ("PermissionError", "操作系统拒绝权限"),
    ("TimeoutError", "操作超时"),
    ("RuntimeError", "没有更合适的专门异常时的运行期错误"),
    ("NotImplementedError", "接口/分支明确尚未实现，不等于返回 NotImplemented"),
]
for name, meaning in examples:
    print(f"{name:<22} {meaning}")


show("4. OSError 有很多更具体的子类")
for cls in (FileNotFoundError, PermissionError, IsADirectoryError, NotADirectoryError):
    print(f"{cls.__name__} <: OSError ->", issubclass(cls, OSError))


show("5. LookupError 可以同时覆盖 KeyError / IndexError")
print(issubclass(KeyError, LookupError))
print(issubclass(IndexError, LookupError))


show("6. StopIteration 很特殊")
print("它是迭代协议的结束信号，不应随便拿来表示普通业务失败。")

print("\n练习：99_exercises.py -> ex03 ~ ex04")
