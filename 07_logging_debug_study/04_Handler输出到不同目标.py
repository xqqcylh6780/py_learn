# -*- coding: utf-8 -*-
"""04 Handler：同一条日志输出到不同目标。"""
import logging
import io

logger = logging.getLogger("handler_demo")
logger.handlers.clear()
logger.propagate = False
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(logging.Formatter("CONSOLE %(levelname)s: %(message)s"))

buffer = io.StringIO()
memory_stream = logging.StreamHandler(buffer)
memory_stream.setLevel(logging.DEBUG)
memory_stream.setFormatter(logging.Formatter("BUFFER %(levelname)s: %(message)s"))

logger.addHandler(console)
logger.addHandler(memory_stream)

logger.debug("调试细节")
logger.info("普通信息")
logger.warning("需要关注")

print("\n缓冲区收到了所有 DEBUG+ 记录：")
print(buffer.getvalue(), end="")
print("Handler 也有自己的 level；Logger 和 Handler 两层都会参与过滤。")
