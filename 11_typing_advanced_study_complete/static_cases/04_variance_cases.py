"""用静态检查器观察协变接口与可变容器的不变性。"""

from collections.abc import Sequence


class Animal:
    pass


class Cat(Animal):
    pass


def inspect_animals(items: Sequence[Animal]) -> None:
    pass


def add_animal(items: list[Animal]) -> None:
    items.append(Animal())


cats: list[Cat] = [Cat()]
inspect_animals(cats)  # Sequence 是只读协变接口，可以通过检查
add_animal(cats)  # expected type-check error：list 可变且不变

