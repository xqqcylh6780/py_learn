# -*- coding: utf-8 -*-
"""
06 pyproject.toml 总览
====================

现代 Python 项目的核心配置文件，常见部分包括 build-system、project 和 tool.*。

`[build-system]` 决定如何构建，`[project]` 描述可分发项目，`[tool.*]` 保存各工具自己的配置。
字段是否有效由相应规范或工具定义；文件能被 TOML 解析不代表构建配置正确。
修改配置后应分别验证元数据、构建产物和工具行为，避免把三类问题混在一起。
"""

import tomllib
sample = '[build-system]\nrequires=["setuptools>=77"]\nbuild-backend="setuptools.build_meta"\n\n[project]\nname="demo-app"\nversion="0.1.0"\nrequires-python=">=3.11"\n\n[project.scripts]\ndemo-app="demo_app.cli:main"\n'
data = tomllib.loads(sample)
print('backend:', data['build-system']['build-backend'])
print('project:', data['project']['name'], data['project']['version'])
print('script:', data['project']['scripts']['demo-app'])
print('\n[tool.xxx] 由对应工具定义，不是 Python 核心统一规定。')
