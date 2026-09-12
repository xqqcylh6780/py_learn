# -*- coding: utf-8 -*-
"""
23 wheel 与 dist-info
====================

wheel 基于 ZIP；*.dist-info 保存 METADATA、WHEEL、RECORD 等安装元数据。

RECORD 列出安装文件及摘要，METADATA 描述名称、版本和依赖，WHEEL 记录格式与标签。
检查产物结构能发现源码树正常但包文件、许可证或资源没有被构建后端收集的问题。
理解格式用于诊断和审计，生成 wheel 仍应交给符合规范的构建后端。
"""

import zipfile, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    p=Path(d)/'demo.whl'
    with zipfile.ZipFile(p,'w') as z:
        z.writestr('demo_pkg/__init__.py','')
        z.writestr('demo_pkg-1.0.dist-info/METADATA','Name: demo-pkg\nVersion: 1.0\n')
    with zipfile.ZipFile(p) as z:
        print('\n'.join(z.namelist()))
print('\n真实 wheel 有严格规范，不应手工拼一个 ZIP 就拿去发布。')
