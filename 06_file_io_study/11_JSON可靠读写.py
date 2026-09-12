# -*- coding: utf-8 -*-
"""11 JSON：数据交换常用，但类型能力有限。"""
import json
from decimal import Decimal

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. dumps/loads')
data={'name':'中文','items':[1,2],'ok':True,'none':None}
s=json.dumps(data, ensure_ascii=False, indent=2)
print(s)
print(json.loads(s))

show('2. JSON 对象键最终是字符串')
s=json.dumps({1:'one'})
print(s, json.loads(s))

show('3. 浮点精度要求高时 parse_float')
obj=json.loads('{"price": 0.1}', parse_float=Decimal)
print(obj, type(obj['price']).__name__)

show('4. 自定义对象不能直接序列化')
try:
    json.dumps({1,2,3})
except TypeError as e:
    print(type(e).__name__, e)
print('可通过 default= 或预先转换为 JSON 可表达结构。')
print('\n练习：ex21~ex22')
