# -*- coding: utf-8 -*-
"""
03 try/except 与精准捕获
======================

核心规则：
1. except 从上到下匹配，第一个匹配项生效
2. 子类应写在父类前面
3. try 块要尽可能小，避免误捕获无关错误
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


show("1. 精准捕获")
text = "abc"
try:
    value = int(text)
except ValueError as exc:
    print("不是合法整数:", exc)


show("2. 一次捕获多个同类处理方式的异常")
for item in ("x", None):
    try:
        print(int(item))
    except (ValueError, TypeError) as exc:
        print(type(exc).__name__, "-> 输入不能转整数")


show("3. 子类必须放在父类前")
try:
    open("__definitely_missing__.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("具体处理：文件不存在")
except OSError:
    print("更宽泛的操作系统错误")


show("4. try 范围越大，越容易误捕获")

def load_number(text):
    # 好：只保护真正可能抛 ValueError 的那一行。
    try:
        number = int(text)
    except ValueError:
        return None
    return number * 2

print(load_number("12"))
print(load_number("x"))


show("5. except Exception 不是永远错误，但要放在系统边界")
print("例如 Web 请求入口、后台 worker 顶层：记录完整日志后转成统一错误响应。")
print("业务函数内部则优先捕获你真正能处理的具体异常。")


show("6. 裸 except: 的风险更高")
print("`except:` 等价于捕获 BaseException，通常连 Ctrl+C / SystemExit 也会抓住。")

print("\n练习：99_exercises.py -> ex05 ~ ex06")
