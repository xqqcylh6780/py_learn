"""19 名字/属性查找：知道成本存在，但不要用牺牲可读性的方式提前微优化。"""
import math, timeit

def global_lookup(xs): return [math.sqrt(x) for x in xs]
def local_lookup(xs):
    sqrt=math.sqrt
    return [sqrt(x) for x in xs]
xs=list(range(100))
print(timeit.timeit(lambda: global_lookup(xs), number=1000))
print(timeit.timeit(lambda: local_lookup(xs), number=1000))
print('现代 CPython 会持续优化解释器；是否值得缓存局部变量必须实测。')
