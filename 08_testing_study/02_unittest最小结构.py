# -*- coding: utf-8 -*-
"""
02 unittest 最小结构
================

直接运行本文件即可观察示例。
"""
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_two_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_number(self):
        self.assertEqual(add(-1, 1), 0)

def demo():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print("成功:", result.wasSuccessful())

if __name__ == "__main__":
    demo()

# 命令行常用：
# python -m unittest
# python -m unittest -v
# python -m unittest path.to.test_module.TestClass.test_method
