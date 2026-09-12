# -*- coding: utf-8 -*-
"""09 zoneinfo：时区、UTC、夏令时与 aware datetime"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

print("=== aware datetime ===")
sg = ZoneInfo("Asia/Singapore")
ny = ZoneInfo("America/New_York")
dt_sg = datetime(2026, 9, 12, 18, 0, tzinfo=sg)
print("SG:", dt_sg)
print("UTC:", dt_sg.astimezone(timezone.utc))
print("NY :", dt_sg.astimezone(ny))

print("\n=== naive vs aware ===")
naive = datetime(2026, 9, 12, 18, 0)
print("naive.tzinfo =", naive.tzinfo)
print("aware.tzinfo =", dt_sg.tzinfo)

print("\n=== DST 歧义与 fold ===")
a = datetime(2026, 11, 1, 1, 30, tzinfo=ny, fold=0)
b = datetime(2026, 11, 1, 1, 30, tzinfo=ny, fold=1)
print(a, a.utcoffset())
print(b, b.utcoffset())

print("\n工程建议：内部传输/存储优先使用 UTC + 明确时区；展示时再转换到当地时区。")
