# -*- coding: utf-8 -*-
"""16 secrets：安全随机数与 Token"""
import secrets

print("randbelow:", secrets.randbelow(100))
print("randbits:", secrets.randbits(16))
print("choice:", secrets.choice("ABCDEFGHJKLMNPQRSTUVWXYZ23456789"))
print("token_bytes:", secrets.token_bytes(8))
print("token_hex:", secrets.token_hex(8))
print("token_urlsafe:", secrets.token_urlsafe(8))

print("\n=== compare_digest ===")
a = "expected-token"
b = "expected-token"
print(secrets.compare_digest(a, b))

print("\n安全随机 ≠ 自动安全系统。Token 长度、过期、存储、重放保护仍需整体设计。")
print("token_urlsafe(n) 的 n 表示随机字节数，编码后的字符串长度通常更长。")
print("生成 token 后仍要限制用途和有效期，服务端保存时可考虑只保存不可逆摘要。")
