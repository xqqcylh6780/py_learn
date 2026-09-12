# -*- coding: utf-8 -*-
"""
16 临时文件、目录与文件系统测试
=================

直接运行本文件即可观察示例。
"""
import tempfile
import unittest
from pathlib import Path

def save_report(folder, text):
    path = Path(folder) / "report.txt"
    path.write_text(text, encoding="utf-8")
    return path

class TestFileSystem(unittest.TestCase):
    def test_save_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = save_report(tmp, "你好")
            self.assertTrue(path.exists())
            self.assertEqual(path.read_text(encoding="utf-8"), "你好")
            self.assertEqual(path.parent, Path(tmp))

if __name__ == "__main__":
    unittest.main(verbosity=2)

# tempfile 会真实走文件系统，但不会污染项目目录。
