# -*- coding: utf-8 -*-
"""12 pickle：Python 对象序列化方便，但绝不能反序列化不可信输入。"""
import pickle
from io import BytesIO

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. pickle 保留更多 Python 类型')
data={'coords':(1,2),'tags':{'a','b'}}
raw=pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(len(raw), pickle.loads(raw))

show('2. 安全边界')
print('pickle.load/loads 能触发对象构造甚至任意代码执行路径。')
print('规则：只加载自己完全信任来源产生的 pickle；外部交换优先 JSON/专门格式。')
print('限制类查找的自定义 Unpickler 也很难形成完整沙箱，不能把它当作通用安全边界。')

show('3. 版本兼容')
print('pickle 适合 Python 内部短期持久化，不应默认把它当跨语言、长期稳定数据格式。')
print('protocol 影响格式与性能，不提供加密、签名或向后兼容承诺。')
print('需要防篡改时先验证可信来源；即使有摘要，也不能加载未知发送者制作的 pickle。')
print('\n练习：ex23~ex24')
