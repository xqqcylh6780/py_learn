# -*- coding: utf-8 -*-
"""21 Unpack + TypedDict：精确描述 **kwargs

Unpack[TypedDict] 能让检查器逐个验证关键字名称、值类型和必需性，适合已有
字典配置接口的渐进式改造。

它描述的是展开后的关键字参数，不会让函数运行时自动拒绝未知键。公共 API
参数较少时，显式命名参数通常仍更清楚。
"""
from typing import TypedDict, Unpack

class Options(TypedDict, total=False):
    timeout: float
    retries: int

def request(url: str, **kwargs: Unpack[Options]) -> dict[str, object]:
    return {'url': url, **kwargs}

print(request('https://example.test', timeout=1.5, retries=2))
print('类型检查器可以据此拒绝拼错的关键字或错误的值类型。')
