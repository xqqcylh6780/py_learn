# -*- coding: utf-8 -*-
"""
01 为什么要测试与测试边界
==============

直接运行本文件即可观察示例。
"""
def show(title):
    print("\n" + "=" * 66)
    print(title)
    print("=" * 66)

show("1. 测试的目标不是证明程序永远正确")
print("测试提供的是可重复的证据：在已覆盖的输入和约束下，行为符合预期。")
print("它尤其擅长防回归，而不是穷举所有未来错误。")

show("2. 测什么")
print("- 公共行为：输入 -> 输出")
print("- 状态变化：调用前后对象/文件/数据库发生什么")
print("- 协作关系：是否调用正确依赖")
print("- 失败行为：错误输入是否以约定方式失败")
print("- 边界：空值、极值、重复、顺序、编码、超时")

show("3. 不要把实现细节全部锁死")
def normalize_name(name):
    return " ".join(name.strip().split()).casefold()

assert normalize_name("  Alice   Wang ") == "alice wang"
print("更稳定的测试关注最终行为，而不是内部到底调用了几次 strip/split。")

show("4. 测试层次")
print("单元测试：快、隔离、定位准")
print("集成测试：多个真实组件协作")
print("端到端测试：最接近真实使用，但慢且定位成本高")

show("5. 一个经验")
print("大多数业务规则应由大量快速单元测试保护；关键集成链路再用少量集成测试确认。")
