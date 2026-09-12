# -*- coding: utf-8 -*-
"""
29 CI 持续集成
==========

CI 的核心不是某份 YAML，而是每次变更都在干净、可重复环境自动执行同一套检查。

版本矩阵验证声明的兼容范围，跨平台任务发现路径、编码和系统依赖差异。
缓存只能加速可重建步骤，不能成为构建成功所必需的隐藏状态。
第三方 Action 和令牌都属于供应链边界，应固定可信版本并授予最小权限。
"""

print('GitHub Actions 示意:')
for line in [
'name: test','on: [push, pull_request]','jobs:','  test:','    runs-on: ubuntu-latest',
'    steps:','      - uses: actions/checkout@v4','      - uses: actions/setup-python@v5',
'      - run: python -m pip install -e ".[dev]"','      - run: python -m unittest discover']:
    print(line)
print('\n真实项目还要考虑版本矩阵、Windows/Linux、缓存、最小权限和 secrets。')
