# -*- coding: utf-8 -*-
"""03 Logger 层级、传播 propagate 与重复日志。"""
import logging

root = logging.getLogger()
root.handlers.clear()
root.setLevel(logging.DEBUG)

root_h = logging.StreamHandler()
root_h.setFormatter(logging.Formatter("ROOT %(name)s: %(message)s"))
root.addHandler(root_h)

app = logging.getLogger("myapp")
child = logging.getLogger("myapp.db")

own_h = logging.StreamHandler()
own_h.setFormatter(logging.Formatter("OWN  %(name)s: %(message)s"))
app.addHandler(own_h)
app.setLevel(logging.DEBUG)

print("默认 propagate=True，所以记录会先到 myapp 的 handler，再继续向 root 传播：")
child.info("可能出现两次")

print("\n关闭 myapp.propagate：")
app.propagate = False
child.info("只经过 myapp 的 handler")

print("\n工程建议：")
print("- 应用通常在顶层统一配置 handler")
print("- 子模块只 getLogger(__name__) 并记录")
print("- 重复日志先检查是不是同一记录被多个祖先 handler 处理")
