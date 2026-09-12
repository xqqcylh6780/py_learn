# -*- coding: utf-8 -*-
"""
23 运算符优先级与位运算
======================

重点不是死背整张优先级表，而是知道哪些表达式容易误读，以及位运算的真实用途。
"""


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


section("1. 常见算术运算")
print("2 ** 3 =", 2 ** 3)
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)

section("2. 优先级：不确定就加括号")
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2, "<- 幂运算右结合")
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)

section("3. 位运算")
a = 0b1010
b = 0b1100
print("a      =", bin(a))
print("b      =", bin(b))
print("a & b  =", bin(a & b))
print("a | b  =", bin(a | b))
print("a ^ b  =", bin(a ^ b))
print("a << 1 =", bin(a << 1))
print("a >> 1 =", bin(a >> 1))

section("4. 位掩码示例")
READ = 0b001
WRITE = 0b010
EXECUTE = 0b100
permissions = READ | WRITE
print("permissions:", bin(permissions))
print("can read:", bool(permissions & READ))
print("can execute:", bool(permissions & EXECUTE))

section("5. 比较和逻辑表达式")
x = 5
print(1 < x < 10 and x != 7)
print("复杂条件建议用括号或拆成有名字的中间变量，减少误读。")

section("6. 条件表达式")
status = "adult" if 20 >= 18 else "minor"
print(status)
print("条件表达式适合短小二选一；复杂分支仍应使用 if/elif。")
