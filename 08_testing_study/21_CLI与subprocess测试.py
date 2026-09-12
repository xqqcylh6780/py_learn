# -*- coding: utf-8 -*-
"""
21 CLI 与 subprocess 测试
======================

直接运行本文件即可观察示例。
"""
import subprocess
import sys

code = "import sys; print(sys.argv[1].upper())"
proc = subprocess.run(
    [sys.executable, "-c", code, "hello"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    check=True,
)

print("returncode:", proc.returncode)
print("stdout:", proc.stdout.strip())
print("stderr:", proc.stderr.strip())

# CLI 测试可分两层：
# 1. 把 argparse 后的业务函数当普通函数单测
# 2. 少量 subprocess 集成测试确认入口、退出码、stdout/stderr
