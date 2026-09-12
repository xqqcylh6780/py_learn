# -*- coding: utf-8 -*-
"""07 re：替换、split、flags、边界、性能与安全"""
import re

print("=== sub 可以使用函数 ===")
def mask(m):
    s = m.group()
    return s[:3] + "****" + s[-2:]

print(re.sub(r"1\d{10}", mask, "手机号 13812345678"))

print("\n=== split ===")
print(re.split(r"[,;，；]\s*", "a,b；c，d"))

print("\n=== flags ===")
multiline = "INFO start\nERROR boom\nINFO end"
print(re.findall(r"^ERROR.*$", multiline, flags=re.MULTILINE))

print("\n=== word boundary ===")
print(re.findall(r"\bcat\b", "cat scatter concatenate cat"))

print("\n=== greedy / non-greedy ===")
html = "<b>one</b><b>two</b>"
print(re.findall(r"<b>.*</b>", html))
print(re.findall(r"<b>.*?</b>", html))

print("\n=== 安全提醒 ===")
print("复杂嵌套量词可能造成灾难性回溯。不要把未经审查的正则直接交给不可信用户。")
print("正则也不是 HTML/XML/JSON 的通用解析器；结构化格式应优先使用对应解析器。")
