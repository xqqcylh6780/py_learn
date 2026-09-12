# -*- coding: utf-8 -*-
"""29 subprocess / shlex：安全启动子进程"""
import subprocess
import sys
import shlex

print("=== 推荐：参数列表 + shell=False（默认）===")
cp = subprocess.run(
    [sys.executable, "-c", 'print("child ok")'],
    capture_output=True,
    text=True,
    check=True,
)
print("stdout:", cp.stdout.strip())
print("returncode:", cp.returncode)

print("\n=== check=True ===")
try:
    subprocess.run(
        [sys.executable, "-c", "raise SystemExit(3)"],
        check=True,
        capture_output=True,
    )
except subprocess.CalledProcessError as e:
    print("returncode:", e.returncode)

print("\n=== timeout ===")
try:
    subprocess.run(
        [sys.executable, "-c", "import time; time.sleep(1)"],
        timeout=0.05,
    )
except subprocess.TimeoutExpired:
    print("timeout caught")

print("\n=== shlex ===")
cmd = 'tool --name "hello world" --count 3'
print(shlex.split(cmd))
print(shlex.join(["tool", "--name", "hello world"]))

print("\n不要把不可信字符串拼成 shell 命令再 shell=True 执行。")
print("如果确实需要 shell 语法，必须明确平台差异与注入风险。")
