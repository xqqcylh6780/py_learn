"""24 数据搬运：序列化、复制、IPC 可能比计算本身更贵。"""
import json, pickle, timeit
obj={'items': list(range(1000)), 'name':'demo'}
print('json bytes:', len(json.dumps(obj).encode()))
print('pickle bytes:', len(pickle.dumps(obj)))
print('json:', timeit.timeit(lambda: json.dumps(obj), number=100))
print('pickle:', timeit.timeit(lambda: pickle.dumps(obj), number=100))
print('不要仅凭此例选格式：安全性、兼容性、可读性和跨语言能力同样重要。')
