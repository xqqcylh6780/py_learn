# -*- coding: utf-8 -*-
"""
07 build-system 与构建后端
=====================

构建前端调用标准构建接口；构建后端真正把源码生成 wheel/sdist。

前端如 build 负责发起构建，后端如 setuptools、hatchling 负责解释项目并产生产物。
构建隔离让声明的构建依赖进入临时环境，从而减少本机已安装包造成的偶然成功。
切换后端会影响配置和产物，不能只替换一个字符串就假设行为完全等价。
"""

print('[build-system]')
print('requires = ["setuptools>=77"]')
print('build-backend = "setuptools.build_meta"')
print('\n构建隔离通常会先创建隔离环境，再安装 build-system.requires。')
print('不要把运行时业务依赖混入 build-system.requires。')
