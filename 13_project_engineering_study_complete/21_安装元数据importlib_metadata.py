# -*- coding: utf-8 -*-
"""
21 importlib.metadata 与安装元数据
============================

运行时查询已安装 distribution 的版本、依赖和 entry points，不需要猜 site-packages 文件布局。

元数据属于已安装分发，不应通过扫描目录名或导入私有实现来推断。
entry points 适合松耦合插件发现，但发现对象后仍需校验接口并隔离加载失败。
源码工作区、editable 安装和普通 wheel 安装可能呈现不同状态，诊断时要说明运行环境。
"""

from importlib.metadata import metadata, PackageNotFoundError
try:
    m=metadata('pip')
except PackageNotFoundError:
    print('pip metadata unavailable')
else:
    print('Name:',m.get('Name'))
    print('Version:',m.get('Version'))
    print('Requires-Python:',m.get('Requires-Python'))
print('\n插件系统也可通过 entry points 做发现。')
