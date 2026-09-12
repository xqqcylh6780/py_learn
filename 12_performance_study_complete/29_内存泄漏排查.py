"""29 Python“内存泄漏”：先区分仍被引用、缓存增长、allocator 保留和真正外部资源泄漏。"""
import gc
class Holder: pass
root=[]
for _ in range(100): root.append(Holder())
print('still referenced:', len(root))
print('gc objects:', len(gc.get_objects()))
print('排查顺序：tracemalloc snapshot -> 引用关系 -> 全局缓存/容器 -> C 扩展/外部资源。')
