"""13 weakref：缓存不一定要延长对象生命周期。"""
import weakref, gc
class Item: pass
obj=Item(); cache=weakref.WeakValueDictionary(); cache['x']=obj
print('before:', list(cache))
del obj; gc.collect()
print('after :', list(cache))
print('弱引用常用于缓存、观察者、元数据；它不是通用“性能加速器”。')
