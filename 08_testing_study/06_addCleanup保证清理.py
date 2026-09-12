# -*- coding: utf-8 -*-
"""
06 addCleanup 保证清理
==================

直接运行本文件即可观察示例。
"""
import tempfile
import unittest
from pathlib import Path

class TestCleanup(unittest.TestCase):
    def test_temp_dir(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)

        p = Path(tmp.name) / "data.txt"
        p.write_text("hello", encoding="utf-8")
        self.assertEqual(p.read_text(encoding="utf-8"), "hello")

if __name__ == "__main__":
    unittest.main(verbosity=2)

# addCleanup 的优势：
# 即使测试中途失败，注册过的清理动作仍会执行。
# 这比“测试函数最后手动删文件”可靠。
