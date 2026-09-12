# -*- coding: utf-8 -*-
"""
23 SQLite 集成测试
==============

直接运行本文件即可观察示例。
"""
import sqlite3

def init_db(conn):
    conn.execute("create table users(id integer primary key, name text not null)")

def add_user(conn, name):
    cur = conn.execute("insert into users(name) values (?)", (name,))
    conn.commit()
    return cur.lastrowid

conn = sqlite3.connect(":memory:")
try:
    init_db(conn)
    uid = add_user(conn, "Alice")
    row = conn.execute("select id, name from users where id=?", (uid,)).fetchone()
    print(row)
finally:
    conn.close()

# 内存 SQLite 是很实用的集成测试工具。
# 但如果生产环境用 PostgreSQL/MySQL，
# 仍需少量针对真实数据库行为差异的集成测试。
