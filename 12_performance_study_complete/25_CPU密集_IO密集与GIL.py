"""25 CPU/IO 与 GIL：先判断瓶颈类型，再选线程、进程或 asyncio。"""
print('传统 GIL 构建的 CPython：纯 Python CPU 密集线程通常不能获得线性多核加速。')
print('I/O 密集：线程/asyncio 常用于隐藏等待。')
print('CPU 密集：进程池常见；但 IPC、启动、序列化也有成本。')
print('Python 3.13 存在可选 free-threaded 构建；是否适用取决于解释器构建和扩展兼容性。')
