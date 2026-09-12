# -*- coding: utf-8 -*-
"""
14 __main__ 与 python -m
=======================

给包增加 __main__.py 后，可通过 `python -m package_name` 启动；入口应保持很薄。

薄入口只负责调用可测试的主函数并把返回值转换为进程退出状态。
若把业务代码直接写在模块顶层，导入测试、复用函数和错误处理都会变困难。
`python -m` 还保证包上下文正确，适合验证安装后的真实启动方式。
"""

print('src/demo_app/__main__.py:')
print('from .cli import main')
print('if __name__ == "__main__":')
print('    raise SystemExit(main())')
print('\n业务逻辑放 cli.py/service.py，不要堆进 __main__.py。')
