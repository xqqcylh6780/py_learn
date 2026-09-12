# -*- coding: utf-8 -*-
"""05 Formatter 与 LogRecord 常用字段。"""
import logging
import threading

logger = logging.getLogger("format.demo")
logger.handlers.clear()
logger.propagate = False
logger.setLevel(logging.INFO)

h = logging.StreamHandler()
h.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | pid=%(process)d | thread=%(threadName)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
))
logger.addHandler(h)

logger.info("一条包含常用上下文的日志")

print("\n常用 LogRecord 字段：")
for field in ["name", "levelname", "message", "pathname", "filename", "lineno", "funcName", "process", "threadName"]:
    print("-", field)

print("\n不要在 format 中引用不存在的自定义字段，否则格式化会报错。")
