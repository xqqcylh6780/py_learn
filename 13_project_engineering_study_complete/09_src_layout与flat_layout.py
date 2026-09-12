# -*- coding: utf-8 -*-
"""
09 src layout 与 flat layout
===========================

src layout 能更早暴露“源码目录恰好可 import”造成的假成功。

src layout 强迫测试按安装后的路径解析包，有助于发现漏打包文件和错误导入。
flat layout 更简单，适合小项目，但运行测试时要防止仓库根目录遮蔽已安装版本。
布局选择应与构建配置、测试入口和团队命令保持一致，不能只移动目录。
"""

print('src layout:')
print('project/')
print('├─ pyproject.toml')
print('├─ src/demo_app/__init__.py')
print('└─ tests/')
print('\n本地开发常配合: python -m pip install -e .')
print('flat layout 并非错误；关键是团队一致、安装行为和测试行为清晰。')
