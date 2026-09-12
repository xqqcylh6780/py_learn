"""05 对象生命周期与垃圾回收

CPython 主要依靠引用计数，循环引用则由垃圾回收器处理。`weakref` 适合
缓存或观察关系：它不会单独延长对象生命周期。不要依赖对象析构时机完成
文件、锁或网络连接的清理，应使用上下文管理器。

观察点：容器互相引用、回调闭包与全局缓存容易形成意外持有。排查时先找
谁仍引用对象，而不是先强制调用 `gc.collect()`。
"""
import gc
import weakref


class Payload:
    pass


payload = Payload()
reference = weakref.ref(payload)
print("weak reference alive:", reference() is not None)

del payload
gc.collect()
print("after deleting strong reference:", reference() is None)

left: list[object] = []
right: list[object] = [left]
left.append(right)
del left, right
print("collected cyclic objects:", gc.collect())
print("结论：资源管理靠明确生命周期；垃圾回收只是内存回收的最后保障。")
