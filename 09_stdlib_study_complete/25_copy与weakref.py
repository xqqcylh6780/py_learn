# -*- coding: utf-8 -*-
"""25 copy / weakref：复制语义与弱引用"""
import copy
import weakref
import gc

print("=== shallow vs deep ===")
a = {"items": [[1], [2]]}
b = copy.copy(a)
c = copy.deepcopy(a)
a["items"][0].append(9)
print("a:", a)
print("shallow:", b)
print("deep:", c)

print("\n=== 自定义 __copy__/__deepcopy__ 是高级扩展点 ===")
print("一般先明确对象所有权和共享关系，再决定是否真的需要 deepcopy。")

print("\n=== weakref ===")
class CacheValue:
    pass

obj = CacheValue()
r = weakref.ref(obj)
print("alive:", r() is obj)
del obj
gc.collect()
print("after del:", r())

print("\n=== WeakValueDictionary ===")
cache = weakref.WeakValueDictionary()
x = CacheValue()
cache["x"] = x
print("before:", list(cache))
del x
gc.collect()
print("after:", list(cache))
print("弱引用常用于缓存/观察者等“不拥有对象生命周期”的关系。")
