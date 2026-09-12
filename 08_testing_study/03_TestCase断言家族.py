# -*- coding: utf-8 -*-
"""
03 TestCase 断言家族
================

直接运行本文件即可观察示例。
"""
import unittest

class DemoAssertions(unittest.TestCase):
    def runTest(self):
        self.assertEqual({"a": 1}, {"a": 1})
        self.assertNotEqual(1, 2)
        self.assertTrue([1])
        self.assertFalse([])
        self.assertIsNone(None)
        self.assertIsNotNone(0)
        self.assertIs( ... , ... )
        self.assertIn("py", "python")
        self.assertNotIn(9, [1, 2, 3])
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
        self.assertCountEqual([1, 2, 2], [2, 1, 2])
        self.assertSequenceEqual([1, 2], [1, 2])
        self.assertDictEqual({"x": 1}, {"x": 1})

if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(DemoAssertions())
    print("所有断言通过:", result.wasSuccessful())

# 选择专门断言的意义：失败时能得到更有信息量的 diff。
