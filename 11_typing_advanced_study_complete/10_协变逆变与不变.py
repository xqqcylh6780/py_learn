# -*- coding: utf-8 -*-
"""10 协变、逆变与不变

直觉：只“产出 T”的只读接口往往可以协变；只“消费 T”的接口往往可以逆变；
既读又写的可变容器通常必须不变。PEP 695 新语法可让检查器推断 variance。
"""
from collections.abc import Sequence

class Animal: pass
class Cat(Animal): pass

cats: Sequence[Cat] = [Cat()]
animals: Sequence[Animal] = cats  # Sequence 是协变的只读视图
print(len(animals))
print('而 list[Cat] 不能安全地当作 list[Animal]：否则别人可能 append(Dog)。')
print('variance 是“类型构造器与子类型关系”的规则，不是运行时转换。')
