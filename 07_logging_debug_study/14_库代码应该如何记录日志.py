# -*- coding: utf-8 -*-
"""14 库代码的日志礼仪：不替应用做主。"""
import logging

# 库模块里最常见的模式：
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def do_work(value):
    logger.debug("do_work value=%r", value)
    if value < 0:
        logger.warning("negative value: %s", value)
    return value * 2

print(do_work(3))
print("\n库代码通常：")
print("- 使用 logging.getLogger(__name__)")
print("- 不调用 basicConfig() 强行配置 root")
print("- 不随便添加 FileHandler/StreamHandler")
print("- 让最终应用决定输出位置、格式和级别")
print("NullHandler 可避免旧环境中‘没有 handler’的警告，现代 Python 中主要是兼容/表达意图。")
