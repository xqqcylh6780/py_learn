# -*- coding: utf-8 -*-
"""
12 logging 记录异常
==================

本节只讲异常相关日志；完整 logging 会放在 07_logging_debug_study。
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("exception_demo")


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. logger.exception 自动附带当前 traceback")
try:
    int("oops")
except ValueError:
    logger.exception("解析配置失败")


show("2. logger.error 默认不会自动带 traceback")
try:
    1 / 0
except ZeroDivisionError as exc:
    logger.error("只有消息: %s", exc)
    logger.error("显式 exc_info=True 也能带 traceback", exc_info=True)


show("3. 日志边界")
print("同一个异常如果每一层都 logger.exception + raise，会产生重复堆栈。")
print("一般在请求入口、worker 顶层、命令行入口等边界记录一次。")


show("4. 日志里不要泄露敏感数据")
print("异常 message 可能含路径、token、SQL 参数、病人信息等。")
print("生产日志需要脱敏；不要为了调试把整个请求对象直接打印。")


show("5. 日志参数优先延迟格式化")
user_id = 42
logger.info("处理用户 user_id=%s", user_id)
print("比 logger.info(f'...') 更符合 logging 的延迟格式化设计。")

print("\n练习：99_exercises.py -> ex23 ~ ex24")
