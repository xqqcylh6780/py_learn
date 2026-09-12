# -*- coding: utf-8 -*-
"""12 Protocol：结构化子类型（静态鸭子类型）

Protocol 根据成员结构描述能力，调用方无需继承某个共同基类。它适合端口、
适配器、可替换客户端和测试替身，让接口依赖保持窄而清晰。

Protocol 应只包含调用方真正需要的成员。协议过大会提高实现成本，并把偶然
细节变成公共契约。默认情况下它只参与静态检查。
"""
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
