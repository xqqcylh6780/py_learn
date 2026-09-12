# -*- coding: utf-8 -*-
"""
19 EAFP 与 LBYL —— 先做再处理，还是先检查
==========================================

EAFP: Easier to Ask Forgiveness than Permission
LBYL: Look Before You Leap

Python 经常偏好 EAFP，但不是“任何情况都用异常”。
"""

from pathlib import Path
import tempfile


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 字典读取：EAFP")
data = {"name": "Alice"}
try:
    age = data["age"]
except KeyError:
    age = 0
print("age =", age)


show("2. 字典读取：LBYL 也可能更直观")
if "name" in data:
    print(data["name"])
print("当检查本身就是业务逻辑时，LBYL 完全合理。")


show("3. 文件 exists() 后 open() 仍可能失败")
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "demo.txt"
    path.write_text("ok", encoding="utf-8")
    print("exists:", path.exists())
    # 在真实并发/外部环境中，exists() 与 open() 之间文件仍可能被删除或权限改变。
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print("真正的操作仍必须准备处理 OSError:", exc)
    else:
        print("read:", text)


show("4. TOCTOU：检查与使用之间存在时间窗口")
print("Time Of Check To Time Of Use。")
print("对文件、网络、进程等外部状态，‘先检查成功’不能保证下一步仍成功。")


show("5. EAFP 也不要拿来吞真正的 bug")
print("只捕获你预计的异常。`except Exception` 然后当成‘不存在’会掩盖程序错误。")


show("6. 选型")
print("纯内存状态、检查清晰且便宜 -> LBYL 常常很好。")
print("外部资源、存在竞争窗口、操作本身就是最终判定 -> EAFP 常更稳。")

print("\n练习：99_exercises.py -> ex41 ~ ex42")
