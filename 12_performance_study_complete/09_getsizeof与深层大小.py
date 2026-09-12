"""09 getsizeof 陷阱：容器大小 != 容器及其所有元素总大小。"""
import sys

a=[list(range(100)) for _ in range(10)]
print('outer only:', sys.getsizeof(a))
print('outer + rows(shallow sum):', sys.getsizeof(a)+sum(sys.getsizeof(r) for r in a))
print('精确深层内存统计很难：共享引用不能重复计算，递归结构要防循环。')
