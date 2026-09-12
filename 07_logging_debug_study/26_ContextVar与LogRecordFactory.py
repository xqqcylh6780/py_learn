# -*- coding: utf-8 -*-
"""
26 ContextVar 与 LogRecordFactory
=================================

在 asyncio / Web 服务中，线程局部变量不一定足够表达“当前请求”。
contextvars.ContextVar 可以随异步上下文传播；LogRecordFactory 可以在所有记录创建时统一注入字段。
"""
import contextvars
import logging

request_id_var = contextvars.ContextVar("request_id", default="-")
old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.request_id = request_id_var.get()
    return record

logging.setLogRecordFactory(record_factory)
try:
    logger = logging.getLogger("ctx.demo")
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(logging.INFO)
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("request=%(request_id)s %(message)s"))
    logger.addHandler(h)

    logger.info("没有请求上下文")
    token = request_id_var.set("req-100")
    try:
        logger.info("当前请求")
    finally:
        request_id_var.reset(token)
finally:
    # LogRecordFactory 是进程级全局设置，教程结束恢复，避免污染其他代码。
    logging.setLogRecordFactory(old_factory)

print("\n工程里要明确谁负责安装全局 LogRecordFactory，避免多个库互相覆盖。")
