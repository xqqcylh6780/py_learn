# -*- coding: utf-8 -*-
"""18 pdb、breakpoint() 与事后调试。"""
import pdb


def buggy_total(values):
    total = 0
    for value in values:
        total += value
    return total

print("示例结果:", buggy_total([1, 2, 3]))
print("\n常用 pdb 命令：")
for cmd, meaning in [
    ("n", "next：执行下一行"),
    ("s", "step：进入函数"),
    ("c", "continue：继续运行"),
    ("p expr", "打印表达式"),
    ("pp expr", "pretty-print"),
    ("bt", "查看调用栈"),
    ("u/d", "在栈帧中向上/向下"),
    ("q", "退出调试器"),
]:
    print(f"{cmd:8s} {meaning}")

print("\n代码中可以写 breakpoint()；默认会进入 pdb。")
print("本教程不自动进入交互调试，避免脚本卡住。")
print("异常发生后也可以 pdb.post_mortem(tb) 做事后调试。")
