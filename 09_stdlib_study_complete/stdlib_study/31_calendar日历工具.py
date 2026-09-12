# -*- coding: utf-8 -*-
"""31 calendar：日历计算，不要手写月份天数"""
import calendar

print("leap 2024:", calendar.isleap(2024))
print("leap 2100:", calendar.isleap(2100))
print("monthrange:", calendar.monthrange(2026, 9), "<- (首日星期, 天数)")

print("\n=== 月日历矩阵 ===")
weeks = calendar.monthcalendar(2026, 9)
for week in weeks:
    print(week)

print("\n=== Calendar.itermonthdates ===")
cal = calendar.Calendar(firstweekday=calendar.MONDAY)
for d in list(cal.itermonthdates(2026, 9))[:10]:
    print(d, "in month=", d.month == 9)

print("\n月份加减、月底等业务规则容易出错；不要假设每月 30 天。")
