# -*- coding: utf-8 -*-
"""
22 本地 HTTP 集成测试
===============

直接运行本文件即可观察示例。
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.request import urlopen

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"OK"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    host, port = server.server_address
    with urlopen(f"http://{host}:{port}/", timeout=2) as r:
        print("status:", r.status)
        print("body:", r.read().decode())
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=2)

# 使用端口 0 让操作系统分配空闲端口，避免测试写死端口。
