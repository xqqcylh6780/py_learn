# -*- coding: utf-8 -*-
"""22 文件锁：标准库没有一个完全统一的跨平台 advisory lock API。"""
import os

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. 平台差异')
print('POSIX 常用 fcntl/flock；Windows 常用 msvcrt.locking。语义并不完全一致。')
try:
    import fcntl
    print('当前平台可导入 fcntl')
except ImportError:
    print('当前平台没有 fcntl（Windows 很常见）')
try:
    import msvcrt
    print('当前平台可导入 msvcrt')
except ImportError:
    print('当前平台没有 msvcrt（POSIX 很常见）')

show('2. 锁并不能自动解决所有问题')
print('要统一所有参与者都遵守同一种锁协议；还要考虑崩溃、超时、NFS/网络文件系统和锁粒度。')
print('简单的“锁文件存在即占用”方案也要解决原子创建、陈旧锁和 PID 复用。')
print('\n练习：ex43~ex44')
