# -*- coding: utf-8 -*-
"""
04 字符串、Unicode 与 bytes
==========================

Python 3 的 str 是 Unicode 文本；bytes 是原始字节序列。
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. str 保存 Unicode 文本")
s = "你好🙂"
print(s)
print("字符数:", len(s))
for ch in s:
    print(ch, "U+%04X" % ord(ch))

section("2. encode: str -> bytes")
data = s.encode("utf-8")
print(data)
print("UTF-8 字节数:", len(data))

section("3. decode: bytes -> str")
text = data.decode("utf-8")
print(text)

section("4. 编码必须匹配")
try:
    b"\xff".decode("utf-8")
except UnicodeDecodeError as exc:
    print("解码失败:", exc)

section("5. 字符串常用方法")
raw = "  Alice,Bob,Charlie  "
print(raw.strip())
print(raw.strip().split(","))
print("-".join(["2026", "09", "12"]))
print("hello".replace("he", "HE"))

section("6. 字符串不可变")
name = "alice"
upper = name.upper()
print(name, upper)
print("upper() 返回新字符串，不会修改原字符串。")

section("7. bytes 和 str 不应混用")
try:
    print("abc" + b"def")
except TypeError as exc:
    print("类型错误:", exc)
