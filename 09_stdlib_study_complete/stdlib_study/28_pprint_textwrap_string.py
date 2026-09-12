# -*- coding: utf-8 -*-
"""28 pprint / textwrap / string：文本与展示辅助工具"""
from pprint import pprint, pformat
import textwrap
import string

print("=== pprint ===")
data = {"users": [{"id": i, "tags": ["python", "study"]} for i in range(3)]}
pprint(data, width=50, sort_dicts=False)
print("pformat ->", pformat(data, width=40)[:60], "...")

print("\n=== textwrap ===")
paragraph = "Python standard library provides many batteries included utilities for everyday programming."
print(textwrap.fill(paragraph, width=28))
sample = "\n        line1\n        line2\n"
print(textwrap.dedent(sample))
print(textwrap.shorten(paragraph, width=30, placeholder="..."))

print("\n=== string ===")
print(string.ascii_letters[:10])
print(string.digits)
tpl = string.Template("Hello $name, balance=$balance")
print(tpl.safe_substitute(name="Alice"))
print("复杂展示优先 f-string/模板引擎；string.Template 适合简单、受限的占位替换。")
