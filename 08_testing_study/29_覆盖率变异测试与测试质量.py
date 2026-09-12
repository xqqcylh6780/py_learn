# -*- coding: utf-8 -*-
"""
29 覆盖率、变异测试与测试质量
================

直接运行本文件即可观察示例。
"""
print("覆盖率回答：哪些代码被执行过。")
print("它不回答：断言是否真的能发现错误。")

def classify(x):
    if x > 0:
        return "positive"
    return "non-positive"

print("\n即使两条分支都跑过，下面这种测试也没有价值：")
print("classify(1)")
print("classify(0)")
print("因为没有断言。")

assert classify(1) == "positive"
assert classify(0) == "non-positive"

print("\n更高阶的测试质量问题：")
print("- branch coverage：分支是否覆盖")
print("- mutation testing：故意修改代码，测试是否能把错误抓出来")
print("- boundary coverage：边界值有没有测试")
print("- requirement coverage：重要需求有没有对应证据")

print("\ncoverage.py、mutation testing 工具通常是第三方工具；")
print("这一仓库先掌握概念，后续项目工程化再接入。")
