"""21 __slots__：大量简单实例时可减少每实例属性存储开销。"""
import sys
class Normal:
    def __init__(self,x): self.x=x
class Slotted:
    __slots__=('x',)
    def __init__(self,x): self.x=x
n=Normal(1); s=Slotted(1)
print('normal object:', sys.getsizeof(n), 'dict:', sys.getsizeof(n.__dict__))
print('slotted object:', sys.getsizeof(s))
print('__slots__ 的首要理由应是数据模型/大量实例；不要承诺固定百分比加速。')
