# -*- coding: utf-8 -*-
"""09 异常日志：exc_info、stack_info、stacklevel。"""
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(filename)s:%(lineno)d %(message)s", force=True)
logger = logging.getLogger("exc.demo")

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("计算失败")  # 等价于 error(..., exc_info=True) 的常见用法

logger.info("普通日志附带当前调用栈", stack_info=True)

def helper():
    logger.warning("把来源定位到调用者", stacklevel=2)

def caller():
    helper()

caller()

print("\nlogger.exception 应放在异常处理上下文中；否则没有当前异常可附加。")
