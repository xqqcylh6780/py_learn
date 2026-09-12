# -*- coding: utf-8 -*-
"""08 bound、constraints 与受限泛型

bound 表示“某个上界及其子类型”；constraints 表示“只能从给定候选类型中选一个”。
两者语义不同，不要混用。
"""
# 学习重点：bound 保留具体子类型，constraints 从候选集合中选择结果类型。
# - bound=Base 允许 Base 的任意子类，并尽量返回调用者的具体类型。
# - constraints=(str, bytes) 只允许列出的类型族。
# - 两者都不是运行时校验，函数实现仍要能处理声明的全部输入。
# 常见误区：同时需要“所有子类”和“仅几个精确类型”却混用两种约束。
from typing import TypeVar

class Animal:
    def speak(self) -> str: return '...'
class Dog(Animal):
    def speak(self) -> str: return 'woof'

A = TypeVar('A', bound=Animal)
def echo_animal(x: A) -> A:
    print(x.speak())
    return x

Text = TypeVar('Text', str, bytes)
def concat(a: Text, b: Text) -> Text:
    return a + b

print(type(echo_animal(Dog())).__name__)
print(concat('a', 'b'))
print(concat(b'a', b'b'))
