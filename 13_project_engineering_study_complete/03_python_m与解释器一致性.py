# -*- coding: utf-8 -*-
"""
03 python -m 与解释器一致性
====================

`python -m pip` 明确使用当前 Python 解释器运行 pip，可减少多 Python 环境装错包。

同样的原则适用于 unittest、包入口和许多标准库工具：先选解释器，再选模块。
直接调用 PATH 中的 pip 或脚本包装器时，它们可能属于另一个虚拟环境。
排错时应记录 `sys.executable` 与工具报告的位置，而不是只看激活提示符。
"""

import sys
print('当前解释器:', sys.executable)
print('推荐命令:')
for cmd in [
    'python -m pip --version',
    'python -m pip install <package>',
    'python -m unittest',
    'python -m my_package',
]:
    print(' ', cmd)
print('\n诊断时同时确认 python 路径和 pip 路径。')
