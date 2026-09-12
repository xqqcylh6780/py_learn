# -*- coding: utf-8 -*-
"""08 bound、constraints 与受限泛型

bound 表示“某个上界及其子类型”；constraints 表示“只能从给定候选类型中选一个”。
两者语义不同，不要混用。
"""
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
