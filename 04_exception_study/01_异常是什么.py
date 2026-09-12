# -*- coding: utf-8 -*-
"""
01 异常是什么 —— Python 的错误传播模型
======================================

目标：
- 理解异常对象、抛出（raise）与栈展开（stack unwinding）
- 区分“返回错误码”和“抛异常”
- 知道异常不是程序崩溃的同义词，而是一种控制流机制
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 最基本的异常")
try:
    int("abc")
except ValueError as exc:
    print("类型:", type(exc).__name__)
    print("消息:", exc)


show("2. 异常会沿调用栈向上传播")

def level3():
    return 10 / 0


def level2():
    return level3()


def level1():
    return level2()


try:
    level1()
except ZeroDivisionError:
    print("level3 没处理 -> level2 没处理 -> level1 没处理 -> 这里捕获")


show("3. 异常与普通返回值")

def parse_age_bad(text):
    # -1 既可能是“解析失败”，也可能是业务数据，语义容易混在一起。
    try:
        return int(text)
    except ValueError:
        return -1


def parse_age(text):
    # 让调用方决定怎么处理解析失败。
    return int(text)


print("错误码方案:", parse_age_bad("abc"))
try:
    parse_age("abc")
except ValueError:
    print("异常方案: 调用方能明确区分失败路径")


show("4. 异常对象本身可以携带数据")
try:
    raise ValueError("年龄必须是整数")
except ValueError as exc:
    print("args:", exc.args)
    print("str(exc):", str(exc))


show("5. 异常适合处理异常路径，不应替代所有分支")
print("文件不存在、解析失败、网络超时等通常适合异常。")
print("普通业务分支（例如用户是否是会员）通常直接 if/else 更清晰。")

print("\n练习：99_exercises.py -> ex01 ~ ex02")
