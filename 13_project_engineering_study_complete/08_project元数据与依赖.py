# -*- coding: utf-8 -*-
"""
08 project 元数据与依赖
=================

[project] 描述名称、版本、Python 要求、运行时依赖、可选依赖和入口点等。

这些字段会进入分发元数据，安装器和包索引据此判断兼容性与依赖关系。
开发、测试工具通常放在可选依赖组中，不能误列为每个用户都必须安装的运行依赖。
发布前要从构建产物读取元数据核对，因为源码配置正确不等于最终 wheel 正确。
"""

import tomllib
cfg = '[project]\nname="hospital-tools"\nversion="1.2.0"\nrequires-python=">=3.11"\ndependencies=["httpx>=0.28,<1"]\n\n[project.optional-dependencies]\ndev=["pytest>=8", "mypy>=1"]\n'
p = tomllib.loads(cfg)['project']
print('name:', p['name'])
print('requires-python:', p['requires-python'])
print('runtime:', p['dependencies'])
print('dev extra:', p['optional-dependencies']['dev'])
print("安装额外依赖的典型语义: python -m pip install '.[dev]'")
