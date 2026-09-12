# -*- coding: utf-8 -*-
"""
04 requirements 与 constraints
=============================

requirements 描述要安装什么；constraints 主要限制解析出的版本，本身不会让未请求的包自动安装。

requirements 是安装请求，constraints 是解析护栏；两者解决的是不同问题。
约束文件适合多个环境共享上限或临时规避坏版本，但不能代替项目元数据。
版本限制过宽可能引入未经验证的变化，过窄则会制造不必要的依赖冲突。
"""

print('requirements.txt 示例:')
print('requests>=2.32,<3')
print('httpx~=0.28')
print('\nconstraints.txt 示例:')
print('urllib3<3')
print('certifi>=2025.1')
print('\n安装: python -m pip install -r requirements.txt -c constraints.txt')
print('\n库通常声明兼容范围；应用部署通常还需要更强的可复现锁定。')
