# -*- coding: utf-8 -*-
"""
17 importlib.resources —— 正确读取包内资源
=========================================

包内 JSON、模板、默认配置等资源，不应总是假设能用：
    Path(__file__).parent / "resources" / ...

因为包可能来自 zip、特殊 loader 或安装布局。
标准库 importlib.resources 提供了“以包为单位”访问资源的抽象。
"""

from importlib import resources
import json
import demo_pkg.resources


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. files() 得到 Traversable")
root = resources.files(demo_pkg.resources)
print(root)
config = root.joinpath("config.json")
print("config:", config)

show("2. 读取文本")
text = config.read_text(encoding="utf-8")
print(text.strip())
print(json.loads(text))

show("3. 资源与普通用户文件要区分")
print("包内只读模板/默认配置适合 importlib.resources。")
print("用户生成的数据、日志、数据库不应该写回安装包目录。")

show("4. as_file")
print("某些 API 强制需要真实 Path 时，可了解 resources.as_file() 的临时物化语义。")
