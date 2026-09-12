# -*- coding: utf-8 -*-
"""
07 __all__ 与 from ... import *
===============================

__all__ 主要控制：
    from module_or_package import *
时哪些名字被导出。

它不是安全边界，也不会让其他公开属性“访问不了”。
常规业务代码一般不推荐星号导入，因为来源不清晰、静态分析困难、容易覆盖名字。
"""

import demo_pkg


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. demo_pkg 声明了 __all__")
print(demo_pkg.__all__)

show("2. __all__ 不是访问控制")
print("PACKAGE_NAME:", demo_pkg.PACKAGE_NAME)
print("greet:", demo_pkg.greet("Alice"))
print("Python 没有靠 __all__ 实现真正的 private。")

show("3. 下划线只是约定")
_hidden = "内部实现"
print("单下划线通常表示不建议外部使用，但语言层面仍可访问。")

show("4. 推荐")
print("公共 API 用明确 import；库作者可用 __all__ 表达导出意图。")
print("不要依赖 `import *` 构建大型项目的命名空间。")
