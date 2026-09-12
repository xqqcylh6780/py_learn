"""23 I/O：减少系统调用和小块往返，通常比 Python 微优化重要。"""
import io
buf=io.StringIO()
for i in range(5): buf.write(f'{i}\n')
print(buf.getvalue())
print('真实文件/网络场景要考虑 buffering、批量读写、协议批次和 fsync 成本。')
