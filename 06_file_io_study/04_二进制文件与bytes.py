# -*- coding: utf-8 -*-
"""04 二进制文件：图片、PDF、协议数据都应以 bytes 看待。"""
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
import struct

def show(t): print('\n'+'='*68+'\n'+t+'\n'+'='*68)

show('1. bytes 与 bytearray')
a=b'ABC'
b=bytearray(b'ABC')
b[0]=ord('Z')
print(a,b)
print('bytes 不可变；bytearray 可原地修改。')

show('2. rb/wb 不做编码转换')
with TemporaryDirectory() as d:
    p=Path(d)/'blob.bin'
    p.write_bytes(b'\x00\x01\xff')
    print(p.read_bytes())

show('3. struct 处理定长二进制结构')
data=struct.pack('<Ih', 1000, -7)
print(data, struct.unpack('<Ih', data))
print('< 表示小端；I/h 是字段类型。二进制协议必须明确字节序和字段宽度。')

show('4. BytesIO')
buf=BytesIO()
buf.write(b'abc')
print(buf.getvalue())
print('\n练习：ex7~ex8')
