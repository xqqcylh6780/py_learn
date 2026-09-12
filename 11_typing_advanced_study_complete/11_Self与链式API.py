# -*- coding: utf-8 -*-
"""11 Self：返回“当前具体子类”"""
from typing import Self

class Builder:
    def __init__(self) -> None:
        self.parts: list[str] = []
    def add(self, text: str) -> Self:
        self.parts.append(text)
        return self

class HtmlBuilder(Builder):
    def bold(self) -> Self:
        self.parts.append('<b>')
        return self

h = HtmlBuilder().add('x').bold()
print(type(h).__name__, h.parts)
print('Self 比把返回值固定写成 Builder 更能保留子类类型。')
