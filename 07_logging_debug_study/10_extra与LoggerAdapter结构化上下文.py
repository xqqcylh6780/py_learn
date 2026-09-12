# -*- coding: utf-8 -*-
"""10 extra 与 LoggerAdapter：给日志增加结构化上下文。"""
import logging

logger = logging.getLogger("context.demo")
logger.handlers.clear()
logger.propagate = False
logger.setLevel(logging.INFO)

h = logging.StreamHandler()
h.setFormatter(logging.Formatter("%(levelname)s request=%(request_id)s user=%(user)s %(message)s"))
logger.addHandler(h)

logger.info("直接 extra", extra={"request_id": "r-001", "user": "alice"})

adapter = logging.LoggerAdapter(logger, {"request_id": "r-002", "user": "bob"})
adapter.info("LoggerAdapter 自动附带上下文")

print("\n注意：extra 的键不能覆盖 LogRecord 已有保留字段，例如 'message'、'name'。")
print("真实服务中 request_id/trace_id 很适合做结构化字段。")
