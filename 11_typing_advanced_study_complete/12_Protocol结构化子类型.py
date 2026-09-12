# -*- coding: utf-8 -*-
"""12 Protocol：结构化子类型（静态鸭子类型）"""
from typing import Protocol

class Closable(Protocol):
    def close(self) -> None: ...

class SocketLike:
    def close(self) -> None:
        print('closed')

def shutdown(x: Closable) -> None:
    x.close()

# SocketLike 没继承 Closable，但结构满足协议。
shutdown(SocketLike())
print('Protocol 让“鸭子类型”可以被静态检查器精确理解。')
