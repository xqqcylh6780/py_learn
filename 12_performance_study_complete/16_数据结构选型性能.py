"""16 数据结构选型：最常见、收益最大的 Python 性能优化之一。"""
from collections import deque
lst=list(range(1000)); dq=deque(range(1000)); st=set(lst)
print('list 尾部 append/pop 很快；头部 pop(0) 需要搬移元素。')
print('deque 两端插入删除适合队列；set/dict 适合成员测试/索引。')
print(999 in st, dq[0], lst[-1])
