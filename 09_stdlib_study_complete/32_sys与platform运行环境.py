# -*- coding: utf-8 -*-
"""32 sys / platform：解释器与运行环境信息"""
import sys
import platform

print("Python:", sys.version)
print("version_info:", sys.version_info)
print("executable:", sys.executable)
print("platform:", sys.platform)
print("byteorder:", sys.byteorder)
print("maxsize:", sys.maxsize)
print("prefix:", sys.prefix)
print("base_prefix:", sys.base_prefix)
print("是否 venv:", sys.prefix != sys.base_prefix)

print("\n=== argv 示例 ===")
print("argv:", sys.argv)

print("\n=== platform ===")
print("system:", platform.system())
print("release:", platform.release())
print("machine:", platform.machine())
print("python_implementation:", platform.python_implementation())

print("\n不要用 platform 字符串做过度脆弱的版本判断；优先特性检测（try/import/hasattr）和明确支持矩阵。")
