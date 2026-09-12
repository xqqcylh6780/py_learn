# -*- coding: utf-8 -*-
"""27 urllib.parse：URL 拆解、拼接与查询参数"""
from urllib.parse import urlsplit, urlencode, parse_qs, quote, unquote, urljoin

url = "https://example.com:8443/api/items?q=hello%20world&page=2#top"
p = urlsplit(url)
print(p)
print("scheme:", p.scheme)
print("hostname:", p.hostname)
print("port:", p.port)
print("path:", p.path)
print("query:", parse_qs(p.query))

print("\n=== urlencode ===")
query = urlencode({"q": "中文 空格", "page": 2})
print(query)

print("\n=== quote/unquote ===")
encoded = quote("a/b 中文", safe="")
print(encoded, unquote(encoded))

print("\n=== urljoin 安全提醒 ===")
base = "https://example.com/users/"
print(urljoin(base, "123"))
print(urljoin(base, "https://evil.example/"))
print("不要把不可信的绝对 URL 直接交给 urljoin 后假设结果仍属于原域名。")
