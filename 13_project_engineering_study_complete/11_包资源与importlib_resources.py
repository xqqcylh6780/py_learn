# -*- coding: utf-8 -*-
"""
11 包资源与 importlib.resources
===========================

包内模板、默认配置、静态数据不要依赖当前工作目录拼路径。

资源可能位于 wheel、zip 或安装器管理的位置，不一定表现为普通源码旁文件。
`importlib.resources` 以包为定位边界，使读取逻辑与启动目录分离。
需要真实文件路径的外部 API 应使用资源上下文管理接口，避免假设资源永久落盘。
"""

print('典型写法:')
print('from importlib import resources')
print('text = resources.files("my_package").joinpath("data/default.toml").read_text(encoding="utf-8")')
print('\n原因: 安装后包位置可能变化，cwd 也不可靠。')

from pathlib import PurePosixPath
for candidate in ['data/default.toml', '../secret.toml', '/tmp/config.toml']:
    path = PurePosixPath(candidate)
    safe = not path.is_absolute() and '..' not in path.parts
    print(f'{candidate!r}: 合法包内相对路径={safe}')
print('外部 API 必须接收真实路径时，使用 resources.as_file(...) 管理临时提取生命周期。')
