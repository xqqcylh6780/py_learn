# -*- coding: utf-8 -*-
"""07 泛型类与 PEP 695 新语法"""

class Box[T]:
    def __init__(self, value: T) -> None:
        self.value = value
    def get(self) -> T:
        return self.value
    def set(self, value: T) -> None:
        self.value = value

b1 = Box[int](10)
b2 = Box[str]('hello')
print(b1.get(), b2.get())
print('type params:', Box.__type_params__)
print('运行时通常仍然是同一个类:', type(b1) is type(b2) is Box)
