# -*- coding: utf-8 -*-
"""
10 分发名、包名与导入名
=============

distribution 名称、import 名称、Git 仓库名称可以不同。

安装器处理的是分发名，Python import 查找的是顶层包或模块名，两者没有强制一一对应。
一个分发还可能提供多个 import 包，因此应以项目文档和安装元数据为准。
排查“已安装但无法导入”时，先确认这两个名称，而不是反复重新安装。
"""

examples=[('beautifulsoup4','bs4'),('Pillow','PIL')]
for dist, imp in examples:
    print(f'distribution={dist!r}, import={imp!r}')
print('\n不要从 PyPI 项目名想当然推导 import 名。')

def find_import_name(distribution):
    return next((imp for dist, imp in examples if dist.casefold() == distribution.casefold()), None)

print('Pillow 的导入名:', find_import_name('pillow'))
print('未知分发名:', find_import_name('unknown'))
print('真实项目应查文档或 packages_distributions() 等安装元数据，而不是维护猜测规则。')
