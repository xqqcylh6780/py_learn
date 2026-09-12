# -*- coding: utf-8 -*-
"""08 日志轮转：RotatingFileHandler / TimedRotatingFileHandler。"""
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from pathlib import Path
import tempfile

with tempfile.TemporaryDirectory() as d:
    path = Path(d) / "app.log"
    logger = logging.getLogger("rotate.demo")
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(logging.INFO)

    h = RotatingFileHandler(path, maxBytes=120, backupCount=2, encoding="utf-8")
    h.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(h)
    for i in range(20):
        logger.info("line %02d abcdefghijklmnopqrstuvwxyz", i)
    h.close()
    print("按大小轮转后的文件:", sorted(p.name for p in Path(d).iterdir()))

print("\n按时间轮转使用 TimedRotatingFileHandler，例如 when='midnight'。")
print("注意：多进程同时直接写同一轮转文件可能产生竞争，生产中应集中写入。")
