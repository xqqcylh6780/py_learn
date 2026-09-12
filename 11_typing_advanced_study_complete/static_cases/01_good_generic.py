from typing import reveal_type

def first[T](items: list[T]) -> T:
    return items[0]

x = first([1, 2, 3])
reveal_type(x)  # static checker should reveal int
