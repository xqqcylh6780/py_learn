# -*- coding: utf-8 -*-
"""
24 editable install
===================

`pip install -e .` 让开发源码以 editable 方式安装；它适合开发，不是生产部署方式。

editable 安装让 import 指向工作区，同时仍保留分发元数据和入口点的安装语义。
它会掩盖某些打包遗漏，因为源码文件存在并不代表普通 wheel 中也包含它们。
因此发布前必须另建干净环境安装真实 wheel，而不能把 editable 测试当成交付验证。
"""

print('开发: python -m pip install -e .')
print("带开发 extra: python -m pip install -e '.[dev]'")
print('\n优势: import 走已安装项目语义，改源码通常无需重装。')
print('但改 pyproject 元数据、entry point、依赖后通常仍需重新安装。')

import sys
def editable_command(project='.', extra=None):
    target = f'{project}[{extra}]' if extra else project
    return [sys.executable, '-m', 'pip', 'install', '-e', target]

print('基础命令:', editable_command())
print('开发依赖:', editable_command(extra='dev'))
print('发布前仍要从干净环境安装普通 wheel，检查 editable 模式可能掩盖的漏打包文件。')
