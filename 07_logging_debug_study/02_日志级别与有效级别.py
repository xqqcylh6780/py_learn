# -*- coding: utf-8 -*-
"""02 日志级别与有效级别。"""
import logging

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("app.worker")

print("标准级别数值：")
for name in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    print(name, logging._nameToLevel[name])

print("\nlogger.level:", logger.level, "(0 表示 NOTSET)")
print("logger.getEffectiveLevel():", logger.getEffectiveLevel())
print("继承到 root 的 WARNING 后：")
logger.debug("不会显示")
logger.warning("会显示")

logger.setLevel(logging.DEBUG)
print("\n显式设置 logger 为 DEBUG 后，有效级别：", logger.getEffectiveLevel())
print("但 root handler 自己仍可能过滤低级别记录。")
logger.debug("是否显示取决于 handler 的 level；basicConfig 的 handler 默认 NOTSET")

print("\n建议：生产环境不要把 ERROR 当普通业务分支使用；级别表达严重程度。")
