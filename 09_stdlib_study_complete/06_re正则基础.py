# -*- coding: utf-8 -*-
"""06 re：正则表达式基础

重点：raw string、search/match/fullmatch、findall/finditer、group。
"""
import re

text = "订单 A-102，订单 B-305，邮箱 user@example.com"

print("=== raw string ===")
pattern = r"[A-Z]-\d+"
print(re.findall(pattern, text))

print("\n=== search / match / fullmatch ===")
print(re.search(r"B-\d+", text).group())
print(re.match(r"订单", text).group())
print(re.fullmatch(r"\d{4}-\d{2}-\d{2}", "2026-09-12"))

print("\n=== 捕获组与命名组 ===")
m = re.search(r"(?P<user>[\w.]+)@(?P<domain>[\w.]+)", text)
print(m.group(0), m.group("user"), m.groupdict())

print("\n=== finditer 保留 Match 信息 ===")
for m in re.finditer(r"([A-Z])-(\d+)", text):
    print(m.group(), m.span(), m.groups())

print("\n=== compile ===")
order_re = re.compile(r"^[A-Z]-\d+$")
for value in ["A-1", "bad", "C-999"]:
    print(value, bool(order_re.fullmatch(value)))
