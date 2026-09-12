# -*- coding: utf-8 -*-
"""
15 console scripts 入口点
======================

[project.scripts] 可以让安装器创建命令行包装器。

包装器最终导入并调用指定对象，因此模块路径、函数名称和返回约定都属于发布接口。
修改入口点元数据后需要重新安装，editable install 也不保证包装器自动刷新。
测试时既要直接测 `main(argv)`，也要对安装后的命令做一次启动冒烟测试。
"""

print('[project.scripts]')
print('hospital-cli = "hospital_tools.cli:main"')
print('\n安装后可以直接运行 hospital-cli。')
print('入口函数应轻量，返回 int/None 作为退出状态。')

import tomllib
raw = b'[project.scripts]\nhospital-cli="hospital_tools.cli:main"\n'
scripts = tomllib.loads(raw.decode())['project']['scripts']
module_name, function_name = scripts['hospital-cli'].split(':', 1)
print('安装器将导入:', module_name, '并调用:', function_name)
print('修改此表后要重新安装，再对生成的命令做启动冒烟测试。')
