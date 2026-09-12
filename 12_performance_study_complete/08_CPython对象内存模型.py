"""08 CPython 对象内存：变量名引用对象，对象有类型与管理开销。"""
import sys

for x in [0, 1.0, '', 'hello', [], [1,2,3], {}, set()]:
    print(type(x).__name__, sys.getsizeof(x))
print('sys.getsizeof 只报告对象自身的浅层大小，不递归计算引用对象。')
print('不同 Python 实现、版本、平台的字节数都可能不同。')
