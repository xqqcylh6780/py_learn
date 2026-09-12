# -*- coding: utf-8 -*-
"""
18 异常常见陷阱与实战清单
========================
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("坑 1：except Exception: pass")
print("错误消失了，但状态可能已经损坏；至少要有明确恢复策略或在边界记录。")


show("坑 2：try 包住太多代码")
print("你以为捕获的是 int() 的 ValueError，实际可能把后续业务代码的 ValueError 也吞掉。")


show("坑 3：捕获后重新造同类异常，却丢掉 cause")
print("需要翻译异常时用 `raise NewError(...) from exc`。")


show("坑 4：finally return")
print("它可能覆盖 try 的 return，甚至吞掉正在传播的异常。")


show("坑 5：把 assert 当业务校验")
print("-O 下断言可能被移除。")


show("坑 6：错误字符串当程序接口")
print("错误消息可以改文案；程序逻辑应依赖异常类型/字段。")


show("坑 7：重复记录同一异常")
print("底层 logger.exception 后 raise，上层再次 logger.exception，最终日志充满重复 traceback。")


show("坑 8：泄露敏感信息")
print("异常消息、日志、note、traceback 周边变量都可能包含隐私或密钥。")


show("坑 9：异步任务无人管理")
print("create_task() 后丢掉引用，会让失败、取消和生命周期变难管理。")


show("坑 10：把异常当 goto")
print("普通可预期分支优先 if/return；异常用于无法正常履行当前操作契约的情况。")


show("项目检查清单")
checks = [
    "捕获的异常是否足够具体？",
    "当前层真的能恢复吗？不能就继续传播。",
    "是否保留了原始 cause/traceback？",
    "资源在失败路径是否一定释放？",
    "日志是否只在合适边界记录一次？",
    "错误信息是否包含敏感数据？",
    "API 是否有稳定异常契约？",
    "异步取消是否被错误吞掉？",
]
for i, item in enumerate(checks, 1):
    print(f"{i}. {item}")

print("\n练习：99_exercises.py -> ex35 ~ ex40")
