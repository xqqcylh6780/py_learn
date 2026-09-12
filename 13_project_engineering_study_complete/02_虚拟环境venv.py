# -*- coding: utf-8 -*-
"""
02 虚拟环境 venv
============

venv 隔离项目依赖；虚拟环境应被视为可删除、可重建的产物。

它隔离的是解释器环境中的包，不会隔离操作系统库、外部命令或网络服务。
判断环境是否正确，要同时查看解释器路径和安装工具实际关联的解释器。
若环境只能靠手工修补恢复，说明依赖声明或初始化步骤还不完整。
"""

import sys
print('当前解释器:', sys.executable)
print('sys.prefix:', sys.prefix)
print('sys.base_prefix:', sys.base_prefix)
print('是否处于 venv:', sys.prefix != sys.base_prefix)
print('\n创建: python -m venv .venv')
print(r'Windows PowerShell: .\.venv\Scripts\Activate.ps1')
print(r'Windows cmd: .venv\Scripts\activate.bat')
print('POSIX: source .venv/bin/activate')
print('\n原则: .venv 不提交 Git；不跨机器复制；需要时重新创建。')
