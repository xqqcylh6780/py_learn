# -*- coding: utf-8 -*-
"""07 泛型类与 PEP 695 新语法

泛型类让实例在创建时携带一致的类型参数。Box[int] 与 Box[str] 共用同一套
运行时实现，但静态检查器会分别跟踪 get() 的返回类型。

PEP 695 的 class Box[T] 需要 Python 3.12+。兼容旧版本时使用 Generic[T]。
常见误区：以为不同特化会生成不同的运行时类，或能自动校验构造参数。
"""

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
