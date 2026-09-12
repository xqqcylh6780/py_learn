# -*- coding: utf-8 -*-
"""25 Final、ClassVar、@final、@override

Final 表示名字不应重新绑定，ClassVar 区分类属性与实例字段；@final 限制继承
或覆盖，@override 则要求父类中确实存在对应成员。

这些约束主要由静态检查器执行。它们让维护者更早发现拼错方法名、意外覆盖
和把类级配置误当实例数据等问题。
"""
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
