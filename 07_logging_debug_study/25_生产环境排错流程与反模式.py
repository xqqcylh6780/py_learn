# -*- coding: utf-8 -*-
"""25 生产环境排错流程与常见反模式。"""

print("推荐排错顺序：")
steps = [
    "1. 先明确症状：错误、变慢、卡死、内存涨、CPU 高，还是数据错",
    "2. 固定时间窗口、请求 ID、版本号和复现条件",
    "3. 查 ERROR/WARNING 及完整 traceback，不只看最后一行",
    "4. 对照变更：代码、配置、依赖、数据、基础设施",
    "5. 卡死看线程/协程栈；慢看 profiler；内存涨看 tracemalloc/进程指标",
    "6. 提出可证伪假设，一次改一个变量",
    "7. 修复后补自动测试、监控或日志，让同类问题下次更快定位",
]
for s in steps:
    print(s)

print("\n高频反模式：")
for s in [
    "到处 print 且上线后删不干净",
    "except Exception: pass",
    "同一异常每层都 logger.exception，造成重复日志",
    "日志里直接写密码、Token、身份证等敏感信息",
    "字符串先用 f-string 拼好再调用 logger.debug，失去惰性格式化优势",
    "没测量就凭感觉优化",
    "只记录 str(exc)，不保留 traceback",
    "生产问题只看日志，不关联版本/请求 ID/配置",
]:
    print("-", s)
