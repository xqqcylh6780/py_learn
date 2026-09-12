"""08 I/O 与序列化成本

I/O 密集任务常被网络、磁盘和编码转换支配。提高性能通常依赖批处理、缓冲、
减少往返和选择合适的数据格式，而不是缩短几行 Python 循环。

序列化时要同时观察 CPU、体积、延迟和兼容性。`pickle` 不能反序列化不可信
数据；JSON 更适合互操作，但并不一定更快或更小。
"""
import json
from io import StringIO


rows = [{"id": number, "name": f"user-{number}"} for number in range(3)]
payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))

buffer = StringIO()
for row in rows:
    buffer.write(f"{row['id']},{row['name']}\n")

print("json bytes:", len(payload.encode("utf-8")))
print("batched text:\n" + buffer.getvalue(), end="")
print("结论：测量端到端时间，优先减少 I/O 次数和数据搬运。")
