# -*- coding: utf-8 -*-
"""11 Self：返回“当前具体子类”

Self 适合返回 self 的链式方法、替代构造器和复制方法。继承后，检查器会把
Self 解析为调用该方法的具体子类，而不是固定的基类。

若方法总是返回某个固定基类，就不应声明 Self。Self 也不是“当前实例”的
运行时特殊对象，它只服务于静态关系表达。
"""
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
