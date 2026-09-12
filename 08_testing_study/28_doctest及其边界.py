# -*- coding: utf-8 -*-
"""
28 doctest 及其边界
===============

直接运行本文件即可观察示例。
"""
import doctest

def slugify(text):
    """
    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("  A   B  ")
    'a-b'
    """
    return "-".join(text.strip().lower().split())

failures, tests = doctest.testmod(verbose=False)
print("doctest cases:", tests)
print("failures:", failures)

# doctest 优点：文档示例能被验证。
# 局限：
# - 对输出格式很敏感
# - 大型测试可读性差
# - 不适合复杂 fixture
# 因此常作为文档示例测试，而不是整个测试体系。
