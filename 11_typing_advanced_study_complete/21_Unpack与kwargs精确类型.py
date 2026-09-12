# -*- coding: utf-8 -*-
"""21 Unpack + TypedDict：精确描述 **kwargs"""
from typing import TypedDict, Unpack

class Options(TypedDict, total=False):
    timeout: float
    retries: int

def request(url: str, **kwargs: Unpack[Options]) -> dict[str, object]:
    return {'url': url, **kwargs}

print(request('https://example.test', timeout=1.5, retries=2))
print('类型检查器可以据此拒绝拼错的关键字或错误的值类型。')
