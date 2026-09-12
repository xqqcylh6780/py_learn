"""17 字符串构建：大量片段优先收集后 join。"""
parts=['ab']*10
print(''.join(parts))
print('少量字符串用 + 完全可以；不要机械地把所有 + 都改成 join。')
print('性能结论取决于循环、片段数量和 Python 版本。')
