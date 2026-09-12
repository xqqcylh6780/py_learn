# -*- coding: utf-8 -*-
"""
19 IsolatedAsyncioTestCase 与 AsyncMock
======================================

直接运行本文件即可观察示例。
"""
import asyncio
import unittest
from unittest.mock import AsyncMock

async def fetch_name(client, uid):
    data = await client.fetch(uid)
    return data["name"]

class TestAsync(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = AsyncMock()

    async def test_fetch_name(self):
        self.client.fetch.return_value = {"name": "Alice"}
        result = await fetch_name(self.client, 1)
        self.assertEqual(result, "Alice")
        self.client.fetch.assert_awaited_once_with(1)

    async def test_async_exception(self):
        self.client.fetch.side_effect = TimeoutError("slow")
        with self.assertRaises(TimeoutError):
            await fetch_name(self.client, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
