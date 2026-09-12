# -*- coding: utf-8 -*-
"""
31 测试替身：Stub、Fake、Spy、Mock
==========================

直接运行本文件即可观察示例。
"""
from unittest.mock import Mock

print("测试替身（test double）不是一个单一概念。")
print("""
Dummy：只是为了填参数，测试根本不使用它
Stub：预先提供固定答案
Fake：有可工作的简化实现，例如内存仓库
Spy：执行真实行为，同时记录调用
Mock：通常用于验证交互是否符合预期
""")

class FakeStore:
    def __init__(self):
        self.data = {}
    def put(self, key, value):
        self.data[key] = value
    def get(self, key):
        return self.data[key]

store = FakeStore()
store.put("x", 1)
print("Fake:", store.get("x"))

def real_double(x):
    return x * 2

spy = Mock(wraps=real_double)
print("Spy result:", spy(3))
spy.assert_called_once_with(3)

gateway = Mock()
gateway.charge.return_value = True
print("Mock/stubbed result:", gateway.charge(100))
gateway.charge.assert_called_once_with(100)

print("\n选择原则：")
print("- 只需要固定结果：Stub")
print("- 需要轻量但真实的行为：Fake")
print("- 要观察真实函数怎么被调用：Spy")
print("- 交互本身就是契约：Mock")
print("不要把所有依赖都机械地换成 Mock。")
