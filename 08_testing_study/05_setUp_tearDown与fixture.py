# -*- coding: utf-8 -*-
"""
05 setUp/tearDown 与 fixture
===========================

直接运行本文件即可观察示例。
"""
import unittest

class Cart:
    def __init__(self):
        self.items = []
    def add(self, price):
        self.items.append(price)
    def total(self):
        return sum(self.items)

class TestCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass: 整个类一次")

    def setUp(self):
        print("setUp: 每个测试前")
        self.cart = Cart()

    def tearDown(self):
        print("tearDown: 每个测试后")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass: 整个类一次")

    def test_empty(self):
        self.assertEqual(self.cart.total(), 0)

    def test_add(self):
        self.cart.add(10)
        self.assertEqual(self.cart.total(), 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)

# 原则：fixture 尽量小。
# setUp 里塞几十个无关对象，会让测试难读、难维护。
