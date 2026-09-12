# -*- coding: utf-8 -*-
"""
22 sdist 与 wheel
================

sdist 是源码分发；wheel 是预构建分发格式。发布项目常根据项目性质提供两者。

从 sdist 安装通常要在目标环境再次构建，wheel 则携带已经组织好的安装内容。
纯 Python wheel 可跨平台，含本地扩展的 wheel 必须用标签声明兼容范围。
发布前应分别检查两类产物，并验证从 sdist 重建不会依赖仓库中的遗漏文件。
"""

print('典型构建: python -m build')
print('dist/project-1.0.0.tar.gz              # sdist')
print('dist/project-1.0.0-py3-none-any.whl  # pure Python wheel')
print('\nwheel 安装时通常不需要重新运行项目构建流程。')
print('带扩展模块的 wheel 可能绑定 Python ABI、OS 和 CPU 架构。')
