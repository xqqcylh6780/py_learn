# -*- coding: utf-8 -*-
"""18 hashlib：消息摘要、文件哈希与密码哈希边界"""
import hashlib
from io import BytesIO

payload = b"hello world"
print("sha256:", hashlib.sha256(payload).hexdigest())
print("sha3_256:", hashlib.sha3_256(payload).hexdigest())
print("blake2b:", hashlib.blake2b(payload, digest_size=16).hexdigest())

print("\n=== 流式 update ===")
h = hashlib.sha256()
for chunk in [b"hello ", b"world"]:
    h.update(chunk)
print(h.hexdigest())

print("\n=== file_digest（Python 3.11+）===")
f = BytesIO(payload)
print(hashlib.file_digest(f, "sha256").hexdigest())

print("\n=== 密码存储 ===")
salt = b"0123456789abcdef"
dk = hashlib.pbkdf2_hmac("sha256", b"password", salt, 200_000)
print("PBKDF2 len:", len(dk))
print("生产系统应使用经过审查的密码哈希方案和合理参数；普通 sha256(password) 不够。")
