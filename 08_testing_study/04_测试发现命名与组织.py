# -*- coding: utf-8 -*-
"""
04 测试发现、命名与组织
=============

直接运行本文件即可观察示例。
"""
import unittest

print("unittest 默认发现约定：")
print("- 文件通常命名 test*.py")
print("- TestCase 方法以 test 开头")
print("- python -m unittest discover")
print("- 可用 -s 指定起始目录、-p 指定文件模式")

print("\n推荐结构：")
print(r"""
project/
├─ src_or_package/
└─ tests/
   ├─ test_users.py
   ├─ test_orders.py
   └─ integration/
      └─ test_storage.py
""")

print("测试名应描述行为，而不是 test1/test2。")
print("例如：test_expired_token_is_rejected")

class TestNaming(unittest.TestCase):
    def test_name_can_explain_expected_behavior(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
