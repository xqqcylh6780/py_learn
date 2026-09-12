from typing import Protocol

class Reader(Protocol):
    def read(self, size: int = -1) -> bytes: ...

class Good:
    def read(self, size: int = -1) -> bytes:
        return b'x' * max(size, 0)

class Bad:
    def read(self, size: str) -> str:
        return size

def consume(r: Reader) -> None: ...
consume(Good())
consume(Bad())  # expected type-check error
