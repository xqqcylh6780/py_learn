"""06 解释器成本与数据结构

字节码、函数调用、属性查找和对象分配都有成本，但只有出现在热点上才值得
关心。用 `dis` 理解一段代码做了什么，用 profile 验证它是否真的重要。

数据结构应按操作选择：成员查询常用 set，队头出队常用 deque，按键访问
常用 dict。局部变量通常比重复属性查找便宜，但可读性和算法复杂度优先。
"""
import dis
from collections import deque


def total_squares(values: list[int]) -> int:
    return sum(value * value for value in values)


queue = deque(["a", "b", "c"])
queue.popleft()
members = {"alice", "bob"}

print("contains alice:", "alice" in members)
print("queue:", list(queue))
dis.dis(total_squares)
print("结论：先以语义选择结构，再在热点中用测量验证成本。")
