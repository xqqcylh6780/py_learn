# -*- coding: utf-8 -*-
"""08 datetime：date、time、datetime、timedelta"""
from datetime import date, datetime, timedelta

print("=== date ===")
d = date(2026, 9, 12)
print(d, d.year, d.weekday(), d.isoweekday())

print("\n=== timedelta 运算 ===")
print(d + timedelta(days=30))
print((date(2026, 10, 1) - d).days)

print("\n=== datetime 构造与替换 ===")
dt = datetime(2026, 9, 12, 18, 30, 15)
print(dt)
print(dt.replace(hour=9, minute=0))

print("\n=== ISO 8601 ===")
s = dt.isoformat(timespec="seconds")
print(s)
print(datetime.fromisoformat(s))

print("\n=== strptime / strftime ===")
parsed = datetime.strptime("2026/09/12 18:30", "%Y/%m/%d %H:%M")
print(parsed.strftime("%Y-%m-%d %H:%M:%S"))

print("\n注意：datetime 本身不会自动理解“新加坡时间/纽约时间”；时区用 zoneinfo。")
