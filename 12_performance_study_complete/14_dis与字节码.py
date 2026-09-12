"""14 dis：理解执行机制，但不要把某个版本字节码当语言规范。"""
import dis

def f(a,b):
    return a+b

dis.dis(f)
print('CPython 字节码会随版本变化；优化结论必须基于目标版本实测。')
