# -*- coding: utf-8 -*-
"""
12 版本号与版本来源
===========

版本号最好有单一事实来源；运行时可通过 importlib.metadata 查询已安装分发版本。

版本同时服务于依赖解析、问题追踪和发布审计，多个手工副本很容易漂移。
查询安装元数据得到的是当前环境中的分发版本，直接运行源码时可能还没有对应分发。
选择静态版本或动态生成版本都可以，但构建、运行和发布页面必须最终一致。
"""

from importlib.metadata import version, PackageNotFoundError
for name in ['pip', 'definitely-not-installed-xyz']:
    try:
        print(name, '=>', version(name))
    except PackageNotFoundError:
        print(name, '=> 未安装')
print('\n避免多个文件手工维护互相矛盾的版本号。')
