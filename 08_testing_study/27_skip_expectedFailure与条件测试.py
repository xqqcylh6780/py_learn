# -*- coding: utf-8 -*-
"""
27 skip、expectedFailure 与条件测试
=============================

直接运行本文件即可观察示例。
"""
import sys
import unittest

class Demo(unittest.TestCase):
    @unittest.skip("演示：功能暂未实现")
    def test_future(self):
        self.fail()

    @unittest.skipUnless(sys.version_info >= (3, 11), "需要 Python 3.11+")
    def test_version_feature(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_known_bug(self):
        self.assertEqual(1, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)

# skip 要有清楚原因。
# expectedFailure 只适合已知且被追踪的问题；
# 如果它突然通过，unittest 会报告 unexpected success。
