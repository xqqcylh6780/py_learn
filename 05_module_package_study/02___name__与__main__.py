# -*- coding: utf-8 -*-
"""
02 __name__ 与 __main__
======================

同一份 Python 文件：
- 被 import 时，__name__ 通常是模块全名；
- 直接作为入口执行时，__name__ == "__main__"。

这就是 if __name__ == "__main__": 的本质。
"""

import demo_pkg.greeter as greeter


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 当前文件")
print("当前 __name__ =", __name__)

show("2. 被导入模块")
print("greeter.__name__ =", greeter.__name__)
print("greeter 被 import，所以不是 __main__。")


def main():
    print("main() 里做真正的程序入口工作")
    print(greeter.greet("Python"))


show("3. 入口守卫")
print("入口守卫让模块既能被 import，又能直接运行。")

if __name__ == "__main__":
    main()

# 典型结构：
# def main():
#     ...
#
# if __name__ == "__main__":
#     main()
#
# 不要把大量业务逻辑直接塞进入口守卫；把它们拆成可测试函数。
