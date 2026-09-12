# -*- coding: utf-8 -*-
"""
10 assert 与异常 —— 不要拿断言做输入校验
========================================
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. assert 的本质")
x = 10
assert x > 0, "程序内部假设被破坏"
print("断言通过")


show("2. assert 适合检查开发者认为‘理论上不可能失败’的不变量")
def internal_algorithm(items):
    result = sorted(items)
    assert len(result) == len(items)
    return result

print(internal_algorithm([3, 1, 2]))


show("3. 用户输入校验必须显式 raise")
def set_age(age):
    if age < 0:
        raise ValueError("age 不能小于 0")
    return age

try:
    set_age(-1)
except ValueError as exc:
    print(exc)


show("4. 为什么不能用 assert 做业务校验")
print("Python 可用 -O 运行，普通 assert 语句可能被移除。")
print("所以权限检查、参数验证、数据完整性检查不能依赖 assert。")


show("5. 测试里的 assert 又是另一回事")
print("测试框架通常使用 assert 来表达预期结果，这是开发期检查。")

print("\n练习：99_exercises.py -> ex19 ~ ex20")
