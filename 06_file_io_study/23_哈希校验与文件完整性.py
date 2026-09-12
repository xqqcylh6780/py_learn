# -*- coding: utf-8 -*-
"""23 hashlib：流式计算文件摘要。"""
from io import BytesIO
import hashlib

def digest_stream(f, algorithm='sha256', chunk_size=1024*1024):
    h=hashlib.new(algorithm)
    for chunk in iter(lambda: f.read(chunk_size), b''):
        h.update(chunk)
    return h.hexdigest()

raw=b'abc'*10000
print(digest_stream(BytesIO(raw)))
print(hashlib.sha256(raw).hexdigest())

print('摘要适合完整性校验、去重标识等；普通哈希不是消息认证。')
print('如果要防恶意篡改，应考虑 HMAC 或签名，而不是只公开一个 SHA-256。')
print('密码存储也不能直接 sha256(password)，应使用专门的密码哈希/KDF。')
print('核对可信摘要时使用 hmac.compare_digest，避免自己实现逐字符比较。')
print('分块大小影响吞吐和内存占用，不改变同一算法对同一字节序列的最终摘要。')
print('\n练习：ex45~ex46')
