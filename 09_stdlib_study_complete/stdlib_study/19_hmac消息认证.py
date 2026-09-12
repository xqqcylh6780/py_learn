# -*- coding: utf-8 -*-
"""19 hmac：带密钥的消息认证"""
import hashlib
import hmac

key = b"super-secret-key"
message = b"amount=100&user=42"
mac = hmac.new(key, message, hashlib.sha256)
signature = mac.hexdigest()
print("signature:", signature)

received = hmac.new(key, message, hashlib.sha256).hexdigest()
print("verified:", hmac.compare_digest(signature, received))

print("\n=== 消息被修改 ===")
tampered = hmac.new(key, b"amount=999&user=42", hashlib.sha256).hexdigest()
print(hmac.compare_digest(signature, tampered))

print("\nHMAC 提供完整性与认证，不提供加密；消息内容仍然是明文。")
print("比较 MAC/Token 时使用 compare_digest，避免普通逐字符比较带来的时序信息。")
