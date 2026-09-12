# -*- coding: utf-8 -*-
"""
16 warnings 与异常的边界
========================

warning：操作还能继续，但需要提醒调用方。
exception：当前操作无法按契约正常完成。
"""

import warnings


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 发出 warning")
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    warnings.warn("旧接口将在未来版本移除", DeprecationWarning, stacklevel=2)
    print("捕获 warning 数:", len(caught))
    print("类别:", caught[0].category.__name__)
    print("消息:", caught[0].message)


show("2. 常见 warning 类别")
for cls in (UserWarning, DeprecationWarning, RuntimeWarning, ResourceWarning):
    print(cls.__name__)


show("3. stacklevel 很重要")
def old_api():
    warnings.warn("请改用 new_api()", DeprecationWarning, stacklevel=2)

print("库作者通常希望 warning 指向调用者代码，而不是 warn() 所在的库内部行。")


show("4. warning 可以被过滤，甚至升级成异常")
with warnings.catch_warnings():
    warnings.simplefilter("error", UserWarning)
    try:
        warnings.warn("测试", UserWarning)
    except UserWarning:
        print("warning 被策略升级成异常")


show("5. 什么时候用哪个")
print("参数非法/文件读取失败/操作无法完成 -> exception")
print("API 即将废弃/结果可用但存在风险 -> warning")

print("\n练习：99_exercises.py -> ex31 ~ ex32")
