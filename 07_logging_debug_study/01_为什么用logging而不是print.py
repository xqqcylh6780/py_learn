# -*- coding: utf-8 -*-
"""
01 为什么用 logging 而不是 print
=================================

运行：python 01_为什么用logging而不是print.py

重点：
- print 适合临时观察；logging 适合长期运行的软件
- 日志可以分级、过滤、写多个目标、保留时间/模块/线程等上下文
- 库代码通常不要擅自替应用配置全局日志
"""
import logging

print("[print] 临时调试输出")

logger = logging.getLogger("demo")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)

logger.debug("DEBUG 默认看不到，因为当前级别是 INFO")
logger.info("服务启动")
logger.warning("这是警告")

print("\n核心区别：")
print("1. logging 有级别，可按环境控制输出量")
print("2. logging 可写终端、文件、网络等不同 Handler")
print("3. logging 自动携带时间、模块、线程、进程等上下文")
print("4. logging 可以集中配置，而不必到处改 print")
