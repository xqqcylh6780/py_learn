# -*- coding: utf-8 -*-
"""23 contextlib：上下文管理器工具箱"""
from contextlib import contextmanager, suppress, nullcontext, ExitStack, redirect_stdout
from io import StringIO

print("=== contextmanager ===")
@contextmanager
def transaction(name):
    print("BEGIN", name)
    try:
        yield {"name": name}
    except Exception:
        print("ROLLBACK", name)
        raise
    else:
        print("COMMIT", name)

with transaction("demo") as tx:
    print("inside", tx)

print("\n=== suppress：只用于明确可忽略的异常 ===")
with suppress(FileNotFoundError):
    open("__definitely_missing__")
print("continued")

print("\n=== nullcontext：可选上下文 ===")
with nullcontext("value") as x:
    print(x)

print("\n=== redirect_stdout ===")
buf = StringIO()
with redirect_stdout(buf):
    print("captured")
print("buffer:", buf.getvalue().strip())

print("\n=== ExitStack：动态管理多个资源 ===")
with ExitStack() as stack:
    stack.callback(lambda: print("cleanup B"))
    stack.callback(lambda: print("cleanup A"))
    print("work")
