# -*- coding: utf-8 -*-
"""20 base64 / binascii：二进制文本编码，不是加密"""
import base64
import binascii

raw = b"hello\x00world"
encoded = base64.b64encode(raw)
print(encoded)
print(base64.b64decode(encoded))

print("\n=== URL-safe base64 ===")
url_token = base64.urlsafe_b64encode(b"\xfb\xff?data")
print(url_token, base64.urlsafe_b64decode(url_token))

print("\n=== 严格校验 ===")
try:
    base64.b64decode(b"@@@not-base64@@@", validate=True)
except binascii.Error as e:
    print(type(e).__name__, e)

print("\n=== hex ===")
hexed = binascii.hexlify(raw)
print(hexed, binascii.unhexlify(hexed))

print("\nBase64 只是编码，任何人都能解码。不要用它“加密”密码或敏感数据。")
