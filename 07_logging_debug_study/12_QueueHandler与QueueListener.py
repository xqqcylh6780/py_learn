# -*- coding: utf-8 -*-
"""12 QueueHandler / QueueListener：把产生日志和写日志解耦。"""
import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue
from threading import Thread

q = Queue()
logger = logging.getLogger("queue.demo")
logger.handlers.clear()
logger.propagate = False
logger.setLevel(logging.INFO)
logger.addHandler(QueueHandler(q))

sink = logging.StreamHandler()
sink.setFormatter(logging.Formatter("%(threadName)s %(message)s"))
listener = QueueListener(q, sink, respect_handler_level=True)
listener.start()

def worker(n):
    for i in range(3):
        logger.info("worker=%s item=%s", n, i)

threads = [Thread(target=worker, args=(n,), name=f"T{n}") for n in range(2)]
for t in threads: t.start()
for t in threads: t.join()
listener.stop()

print("\n高并发或慢磁盘场景，QueueHandler 可降低业务线程直接做 I/O 的压力。")
print("多进程可用 multiprocessing.Queue，但配置和生命周期要更谨慎。")
