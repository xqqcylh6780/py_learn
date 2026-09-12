# -*- coding: utf-8 -*-
"""
25 测试隔离与顺序依赖
============

直接运行本文件即可观察示例。
"""
STATE = []

def bad_test_a():
    STATE.append("x")

def bad_test_b():
    assert STATE == ["x"]  # 依赖 test_a 先运行

print("上面这种测试是坏味道：单独运行 bad_test_b 会失败。")
print("正确测试应自己建立前置条件，并在结束后恢复共享状态。")

def good_test():
    local_state = []
    local_state.append("x")
    assert local_state == ["x"]

good_test()
print("独立测试通过")

# 每个测试都应该能：
# - 单独运行
# - 任意顺序运行
# - 重复运行
# - 和其他测试并行时尽量互不污染
