"""03 timeit：微基准的标准库工具。"""
import timeit

stmt1 = "'-'.join(parts)"
setup = "parts = ['a', 'b', 'c', 'd']"
print('join:', timeit.timeit(stmt1, setup=setup, number=10000))
print('repeat:', timeit.repeat(stmt1, setup=setup, repeat=3, number=10000))
print('timeit 会尽量减少基准框架本身的干扰；仍需避免测量无关工作。')
