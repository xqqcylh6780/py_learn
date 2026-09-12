# -*- coding: utf-8 -*-
"""
28 多进程、网络日志与安全边界
=============================
"""
import logging
from logging.handlers import SocketHandler, DEFAULT_TCP_LOGGING_PORT

print("多进程日志建议：")
print("- 工作进程 -> multiprocessing.Queue -> 单独 listener/writer")
print("- 避免多个进程同时直接轮转同一个普通日志文件")
print("- 进程启动方式不同（spawn/fork/forkserver）时，不要假设 handler 状态会安全继承")

print("\n网络日志：")
print("SocketHandler 可以把 LogRecord 发到远端，但默认协议涉及 pickle。")
print("pickle 数据不应从不可信网络端点直接反序列化；需要认证、隔离或自定义安全协议。")

h = SocketHandler("localhost", DEFAULT_TCP_LOGGING_PORT)
print("SocketHandler 类型:", type(h).__name__)
h.close()  # 没有 emit，因此不会连接网络

print("\n生命周期：")
print("应用退出时 logging.shutdown() 会 flush/close 已注册的 handlers；解释器正常退出也会调用它。")
print("但崩溃、os._exit、强制 kill 等情况下不要假设缓冲日志一定落盘。")
