# -*- coding: utf-8 -*-
"""
08 异常边界与分层 —— 谁应该捕获异常
===================================

原则：
- 能恢复，才在当前层捕获
- 不能恢复，就继续传播
- 在系统边界统一记录与转换
"""


def show(title):
    print("\n" + "=" * 68)
    print(title)
    print("=" * 68)


class RepositoryError(Exception):
    pass


class ServiceError(Exception):
    pass


show("1. 底层：抛出具体错误")
def repository_get(user_id):
    if user_id == 0:
        raise RepositoryError("数据库连接失败")
    if user_id == 404:
        return None
    return {"id": user_id, "name": "Alice"}


show("2. 服务层：只翻译自己理解的错误")
def service_get_user(user_id):
    try:
        user = repository_get(user_id)
    except RepositoryError as exc:
        raise ServiceError("用户服务暂时不可用") from exc
    if user is None:
        return None
    return user


show("3. 边界层：统一变成对外响应")
def endpoint(user_id):
    try:
        user = service_get_user(user_id)
    except ServiceError as exc:
        print("这里应记录完整 traceback")
        return 500, {"error": str(exc)}
    if user is None:
        return 404, {"error": "not found"}
    return 200, user

for uid in (1, 404, 0):
    print(uid, "->", endpoint(uid))


show("4. 最糟糕的模式之一：层层捕获、层层打印、再继续抛")
print("这样会重复日志，而且经常丢失上下文。")
print("通常只在真正的日志边界记录一次完整异常。")


show("5. ‘能恢复’的例子")
print("缓存 miss -> 查数据库：可以恢复。")
print("主配置失败 -> 读取备用配置：可以恢复。")
print("数据损坏但当前层不知道怎么修：不要吞掉。")

print("\n练习：99_exercises.py -> ex15 ~ ex16")
