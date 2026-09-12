# -*- coding: utf-8 -*-
"""
11 spec、spec_set 与 autospec
===========================

直接运行本文件即可观察示例。
"""
from unittest.mock import Mock, create_autospec

class PaymentClient:
    def charge(self, user_id, amount, *, currency="CNY"):
        return {"ok": True}

loose = Mock()
loose.this_method_does_not_exist()
print("普通 Mock 会允许凭空访问不存在的属性。")

strict = Mock(spec_set=PaymentClient)
try:
    strict.no_such_method()
except AttributeError as e:
    print("spec_set 能更早暴露拼写错误:", e)

client = create_autospec(PaymentClient, instance=True)
client.charge("u1", 10, currency="CNY")
try:
    client.charge("u1")
except TypeError as e:
    print("autospec 还能检查调用签名:", e)
