# -*- coding: utf-8 -*-
"""25 Final、ClassVar、@final、@override"""
from typing import ClassVar, Final, final, override

MAX_RETRY: Final = 3

class Base:
    kind: ClassVar[str] = 'base'
    def run(self) -> str:
        return 'base'

class Child(Base):
    @override
    def run(self) -> str:
        return 'child'

@final
class Closed:
    pass

print(MAX_RETRY, Child.kind, Child().run())
print('这些主要是静态约束；Python 运行时通常不阻止重新赋值或继承。')
