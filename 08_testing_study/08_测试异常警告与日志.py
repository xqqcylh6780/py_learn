# -*- coding: utf-8 -*-
"""
08 测试异常、警告与日志
=============

直接运行本文件即可观察示例。
"""
import logging
import unittest
import warnings

def parse_age(text):
    n = int(text)
    if n < 0:
        raise ValueError("age must be >= 0")
    return n

def old_api():
    warnings.warn("old_api is deprecated", DeprecationWarning)
    return 1

logger = logging.getLogger("demo.testing")

def work():
    logger.info("work started")

class TestFailures(unittest.TestCase):
    def test_exception(self):
        with self.assertRaisesRegex(ValueError, ">= 0"):
            parse_age("-1")

    def test_warning(self):
        with self.assertWarns(DeprecationWarning):
            old_api()

    def test_logs(self):
        with self.assertLogs("demo.testing", level="INFO") as cm:
            work()
        self.assertTrue(any("work started" in line for line in cm.output))

if __name__ == "__main__":
    unittest.main(verbosity=2)
