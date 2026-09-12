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
