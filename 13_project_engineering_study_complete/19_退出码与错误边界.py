# -*- coding: utf-8 -*-
"""
19 退出码与错误边界
===========

CLI/服务边界将内部异常转换为用户可理解的信息和稳定退出码；核心业务层不要到处 sys.exit。

退出码面向调用者，错误文本面向人；自动化脚本不应依赖解析自然语言判断成功与否。
预期业务错误与程序缺陷应分开处理，后者要保留足够诊断信息。
统一边界还能保证资源清理和日志记录发生后，再结束整个进程。
"""

def command(ok=True):
    return 0 if ok else 2
for ok in [True,False]:
    print('ok=',ok,'exit=',command(ok))
print('\n0 通常表示成功；非 0 表示失败，具体含义由 CLI 文档定义。')
print('入口层可 raise SystemExit(main())；业务层优先抛异常或返回业务结果。')
