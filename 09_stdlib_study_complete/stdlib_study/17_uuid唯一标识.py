# -*- coding: utf-8 -*-
"""17 uuid：随机 UUID 与命名空间 UUID（面向 Python 3.13）"""
import uuid

u4 = uuid.uuid4()
print("uuid4:", u4)
print("hex:", u4.hex)
print("bytes len:", len(u4.bytes))
print("version:", u4.version)

print("\n=== 确定性的 uuid5 ===")
a = uuid.uuid5(uuid.NAMESPACE_URL, "https://example.com/users/123")
b = uuid.uuid5(uuid.NAMESPACE_URL, "https://example.com/users/123")
print(a, a == b)

print("\n=== 解析 ===")
parsed = uuid.UUID(str(u4))
print(parsed == u4)

print("\nPython 3.13 常用 uuid1/3/4/5；一般随机业务 ID 常见 uuid4。")
print("uuid1 可能暴露与节点/时间相关的信息；不要把“唯一”误认为“不可猜/保密”。")
