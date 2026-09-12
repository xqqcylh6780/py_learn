# -*- coding: utf-8 -*-
"""07 FileHandler：编码、错误处理与关闭。"""
import logging
from pathlib import Path
import tempfile

with tempfile.TemporaryDirectory() as d:
    path = Path(d) / "app.log"
    logger = logging.getLogger("file.demo")
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(logging.INFO)

    h = logging.FileHandler(path, mode="w", encoding="utf-8", errors="backslashreplace")
    h.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(h)
    logger.info("中文日志：你好")
    logger.warning("第二行")

    # removeHandler 不会自动替你 close；长期程序应明确关闭自己创建的 handler。
    logger.removeHandler(h)
    h.close()

    print(path.read_text(encoding="utf-8"))

print("建议显式写 encoding='utf-8'，不要依赖操作系统默认编码。")
