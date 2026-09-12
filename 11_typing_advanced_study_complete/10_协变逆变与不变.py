# -*- coding: utf-8 -*-
"""10 协变、逆变与不变

直觉：只“产出 T”的只读接口往往可以协变；只“消费 T”的接口往往可以逆变；
既读又写的可变容器通常必须不变。PEP 695 新语法可让检查器推断 variance。
"""
# 学习重点：variance 描述容器的子类型关系是否可随元素类型安全变化。
# - 只读 Sequence[Cat] 可作为 Sequence[Animal] 使用。
# - 可写 list[Cat] 不能作为 list[Animal]，否则可能被写入 Dog。
# - 回调参数常呈逆变，返回值常呈协变。
# 常见误区：把继承关系直接套到所有泛型容器上。
from collections.abc import Sequence

class Animal: pass
class Cat(Animal): pass

cats: Sequence[Cat] = [Cat()]
animals: Sequence[Animal] = cats  # Sequence 是协变的只读视图
print(len(animals))
print('而 list[Cat] 不能安全地当作 list[Animal]：否则别人可能 append(Dog)。')
print('variance 是“类型构造器与子类型关系”的规则，不是运行时转换。')
