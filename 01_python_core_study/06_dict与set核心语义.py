# -*- coding: utf-8 -*-
"""
06 dict 与 set 核心语义
======================
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. dict 是 key -> value 映射")
user = {"name": "Alice", "age": 20}
print(user["name"])
print(user.get("city"))
print(user.get("city", "未知"))

section("2. [] 与 get 的语义不同")
try:
    print(user["city"])
except KeyError as exc:
    print("[] 缺失时抛 KeyError:", exc)
print("get 缺失时可以返回默认值。")

section("3. set 去重并支持集合运算")
a = {1, 2, 3}
b = {3, 4, 5}
print("union:", a | b)
print("intersection:", a & b)
print("difference:", a - b)
print("symmetric difference:", a ^ b)

section("4. dict/set 成员测试通常是查 key")
print("name" in user)
print("Alice" in user)
print("Alice" in user.values())

section("5. dict 保持插入顺序，但不是排序容器")
d = {}
d["b"] = 2
d["a"] = 1
print(list(d))
print("需要按 key 排序时显式 sorted(d)。")

section("6. 合并字典")
a = {"host": "localhost", "port": 8000}
b = {"port": 9000, "debug": True}
print(a | b)
print("右侧同名 key 覆盖左侧。")

section("7. set 元素必须可哈希")
try:
    {[]}
except TypeError as exc:
    print("list 不能放进 set:", exc)
