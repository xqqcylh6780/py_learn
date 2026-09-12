# -*- coding: utf-8 -*-
"""30 collections.abc / types：协议检查与运行时类型工具"""
from collections.abc import Iterable, Iterator, Mapping, Sequence
from types import MappingProxyType, SimpleNamespace

print("=== collections.abc ===")
for obj in [[1, 2], iter([1, 2]), {"a": 1}, "abc"]:
    print(
        type(obj).__name__,
        "Iterable=", isinstance(obj, Iterable),
        "Iterator=", isinstance(obj, Iterator),
        "Mapping=", isinstance(obj, Mapping),
        "Sequence=", isinstance(obj, Sequence),
    )

print("\n注意：判断“能不能 iter(obj)”最直接的方式仍是实际调用 iter；ABC 是结构/注册式协议视图。")

print("\n=== MappingProxyType：只读视图 ===")
source = {"debug": False}
proxy = MappingProxyType(source)
print(proxy)
source["debug"] = True
print(proxy, "<- 是视图，不是副本")
try:
    proxy["x"] = 1
except TypeError as e:
    print(type(e).__name__, e)

print("\n=== SimpleNamespace ===")
ns = SimpleNamespace(host="127.0.0.1", port=8000)
print(ns, ns.host)
