# -*- coding: utf-8 -*-
"""24 inspect：签名、成员与运行时反射"""
import inspect

class Service:
    def run(self, x: int, *, verbose: bool = False) -> str:
        """执行任务。"""
        return str(x)

def f(a, b=2, *args, c=3, **kwargs):
    pass

print("signature:", inspect.signature(f))
for name, p in inspect.signature(f).parameters.items():
    print(name, p.kind, p.default)

print("\n=== bind ===")
sig = inspect.signature(f)
bound = sig.bind(1, 9, 10, c=4, extra=5)
print(bound.arguments)

print("\n=== members ===")
print([name for name, obj in inspect.getmembers(Service, inspect.isfunction)])

print("\n=== predicates ===")
print(inspect.isclass(Service), inspect.isfunction(f), inspect.ismethod(Service().run))

print("\n反射很强，但大量依赖私有属性/源码结构会增加耦合；优先稳定公开接口。")
