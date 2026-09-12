# -*- coding: utf-8 -*-
"""
20 子进程调用的工程写法
=============

调用外部工具时明确参数列表、退出码、编码、超时和 stderr；不要为了方便默认 shell=True。

参数列表可以避免额外 shell 解析，并清楚表达每个参数的边界；用户输入更不能直接拼命令字符串。
`check=True` 适合失败即异常的调用，若非零码属于协议的一部分则应显式判断。
超时后还要考虑子进程树、部分输出和重试是否安全，不能只捕获异常后忽略。
"""

import subprocess, sys
cp=subprocess.run([sys.executable,'-c',"print('child-ok')"],text=True,capture_output=True,timeout=5,check=True)
print('returncode:',cp.returncode)
print('stdout:',cp.stdout.strip())
print('\n检查项: 参数 list、timeout、check、stderr、编码、取消/终止策略。')
