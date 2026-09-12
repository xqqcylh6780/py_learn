# -*- coding: utf-8 -*-
"""11 Filter：过滤记录，也可以注入字段。"""
import logging

class RequestFilter(logging.Filter):
    def __init__(self, request_id):
        super().__init__()
        self.request_id = request_id
    def filter(self, record):
        record.request_id = self.request_id
        return not record.getMessage().startswith("DROP")

logger = logging.getLogger("filter.demo")
logger.handlers.clear()
logger.propagate = False
logger.setLevel(logging.DEBUG)

h = logging.StreamHandler()
h.addFilter(RequestFilter("req-42"))
h.setFormatter(logging.Formatter("%(request_id)s %(levelname)s %(message)s"))
logger.addHandler(h)

logger.info("保留")
logger.info("DROP 这一条被过滤")

print("Filter 可以返回 False 丢弃记录；也常用于添加 request_id 等上下文。")
