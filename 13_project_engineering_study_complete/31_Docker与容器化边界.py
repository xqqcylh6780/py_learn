# -*- coding: utf-8 -*-
"""
31 Docker 与容器化边界
================

容器能封装运行环境，但不能替代依赖管理、测试、配置设计和可观察性。

镜像应来自可审计构建，运行时配置和秘密通过部署平台注入，而不是烘焙进层中。
非 root 用户、只读文件系统和信号处理会直接影响 Python 应用的路径与退出设计。
固定基础镜像摘要提高可复现性，但也需要持续重建以获得安全更新。
"""

print('Dockerfile 示意:')
for line in ['FROM python:3.13-slim','WORKDIR /app','COPY . .','RUN python -m pip install --no-cache-dir .','CMD ["python", "-m", "demo_app"]']:
    print(line)
print('\n重点: 基础镜像策略、非 root、secret 不进镜像、缓存、健康检查、日志、退出信号。')
