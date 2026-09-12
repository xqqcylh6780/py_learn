# -*- coding: utf-8 -*-
"""06 basicConfig 的真实行为与 force=True。"""
import logging

root = logging.getLogger()
root.handlers.clear()

logging.basicConfig(level=logging.INFO, format="FIRST %(message)s")
logging.info("第一次配置")

# root 已有 handler 时，默认再次 basicConfig 通常不重新配置。
logging.basicConfig(level=logging.DEBUG, format="SECOND %(message)s")
logging.debug("这条通常仍看不到")
logging.info("格式仍是 FIRST")

print("\n使用 force=True 会先移除并关闭现有 root handlers，再重配：")
logging.basicConfig(level=logging.DEBUG, format="FORCED %(levelname)s %(message)s", force=True)
logging.debug("现在 DEBUG 可见")

print("\n注意：force=True 适合应用入口/测试，不适合库代码擅自调用。")
