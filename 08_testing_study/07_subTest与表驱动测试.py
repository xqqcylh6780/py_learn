# -*- coding: utf-8 -*-
"""
07 subTest 与表驱动测试
=================

直接运行本文件即可观察示例。
"""
import unittest

def is_even(n):
    return n % 2 == 0

class TestEven(unittest.TestCase):
    def test_cases(self):
        cases = [
            (0, True),
            (1, False),
            (2, True),
            (-3, False),
            (-4, True),
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(is_even(value), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)

# subTest 不是 pytest.parametrize 的完全替代，
# 但在标准库 unittest 中非常适合小型表驱动测试。
