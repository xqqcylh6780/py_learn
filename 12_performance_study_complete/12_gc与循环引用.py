"""12 gc：引用计数处理大多数对象；循环引用需要循环垃圾回收器。"""
import gc
class Node:
    pass

a=Node(); b=Node(); a.other=b; b.other=a
print('gc enabled:', gc.isenabled())
print('threshold:', gc.get_threshold())
del a,b
print('collected:', gc.collect())
print('不要为了“更快”随意长期关闭 GC；先测量并理解对象生命周期。')
