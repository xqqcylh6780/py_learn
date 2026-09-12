"""11 CPython 引用计数：实现细节，不要写依赖具体计数值的业务逻辑。"""
import sys
x=[]
print('refcount:', sys.getrefcount(x))
y=x
print('after alias:', sys.getrefcount(x))
del y
print('after del:', sys.getrefcount(x))
print('getrefcount 自己也会临时持有引用，因此数字包含测量开销。')
