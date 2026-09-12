# -*- coding: utf-8 -*-
"""
30 测试架构、AAA 与反模式
================

直接运行本文件即可观察示例。
"""
print("""
一个清晰测试通常可以看成：

Arrange  准备输入、依赖、前置状态
Act      执行一个核心行为
Assert   验证结果

有时再加 Cleanup。
""")

print("好测试常见特征：")
print("- Fast：足够快")
print("- Independent：互相独立")
print("- Repeatable：可重复")
print("- Self-validating：自动判定通过/失败")
print("- Timely：最好和功能一起写")

print("\n高频反模式：")
print("- 一个测试测十几个不相关行为")
print("- 只断言 mock 被调用，不验证业务结果")
print("- 大量 patch 私有实现细节")
print("- 测试依赖执行顺序")
print("- sleep 等待异步/线程")
print("- 捕获 Exception 后什么都不检查")
print("- fixture 比业务代码还复杂")
print("- 为了覆盖率写没有意义的断言")

print("\n最终目标不是“测试数量多”，而是：")
print("关键行为改变时，测试能快速、准确地告诉你哪里坏了。")
