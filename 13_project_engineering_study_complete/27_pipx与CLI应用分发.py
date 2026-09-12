# -*- coding: utf-8 -*-
"""
27 pipx 与 CLI 应用
================

库依赖装进项目 venv；独立 CLI 工具更适合隔离安装。pipx 是常见 Python CLI 安装方式。

pipx 为每个应用维护独立环境，再把命令包装器暴露到用户 PATH，减少工具间依赖冲突。
它适合最终用户安装命令行应用，不负责项目开发依赖或服务部署。
应用仍需正确声明 Python 版本、运行依赖和 console script，隔离工具不能弥补错误元数据。
"""

print('CLI 项目用 [project.scripts] 暴露命令。')
print('pipx install .  可把 CLI 安装到独立环境。')
print('pipx run ...    可按工具规则临时运行。')
print('\n不要为了一个 CLI 工具，把它和所有项目业务依赖塞进同一个 venv。')
