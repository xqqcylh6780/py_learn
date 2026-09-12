# -*- coding: utf-8 -*-
"""
collections.Counter —— 专门用来"数数"的字典
============================================

运行：  python 01_counter.py
练习：  python 99_exercises.py   （文件末尾有本节的题目）

建议用法：先跑一遍看输出，再随手改里面的字符串和数字做实验。
读懂一个知识点再往下翻，比一口气看完有效得多。
"""

from collections import Counter


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ---------------------------------------------------------------
# 1. 先说"为什么"：不用 Counter 你得手写什么
# ---------------------------------------------------------------
show("1. 手动计数 vs Counter")

words = "the quick brown fox jumps over the lazy dog the fox".split()

# 手写版：
manual = {}
for w in words:
    if w not in manual:
        manual[w] = 0
    manual[w] += 1
print("手写版 :", manual)

# Counter 版：
c = Counter(words)
print("Counter:", c)
print("结果一样吗:", dict(c) == manual)
print("注意 repr 已经按次数从多到少排好了")


# ---------------------------------------------------------------
# 2. 核心能力：most_common
# ---------------------------------------------------------------
show("2. most_common —— 找出前 N 名")

print("全部排序  :", c.most_common())
print("前 3 名   :", c.most_common(3))
print("倒数第 1 名:", c.most_common()[-1])

# 次数并列时怎么办？按"第一次出现的先后"排，因为底层是稳定的 sorted
tie = Counter(["b", "a", "c"])
print("三个都是 1 次时的顺序:", tie.most_common())


# ---------------------------------------------------------------
# 3. 最大的坑：读一个不存在的键
# ---------------------------------------------------------------
show("3. 坑：c[x] 对缺失的键返回 0，而且不会写进去")

t = Counter("aab")
print("t                =", t)
print("t['z']           =", t["z"], " <- 返回 0，不报 KeyError")
print("'z' in t         =", "z" in t, " <- 但也没有把它加进去")

t["z"] += 1
print("t['z'] += 1 之后  ->", t, " <- 这次是「写」，真的进去了")

print()
print("结论：读用 t[x] 很方便，但要判断「到底有没有」就用 in 或 .get()")
print("t.get('qq')      =", t.get("qq"), " <- 同样返回 None/0，也不写入")


# ---------------------------------------------------------------
# 4. 集合风格的运算符：+ - & |
# ---------------------------------------------------------------
show("4. 运算符 + - & |（Counter 独有）")

a = Counter("aabbb")   # a=2, b=3
b = Counter("abbcc")   # a=1, b=2, c=2

print("a     =", a)
print("b     =", b)
print()
print("a + b =", a + b, "  计数相加")
print("a - b =", a - b, "  相减，只保留正数（0 和负数直接消失）")
print("a & b =", a & b, "  每个键取较小值（交集）")
print("a | b =", a | b, "  每个键取较大值（并集）")


# ---------------------------------------------------------------
# 5. 其他常用方法
# ---------------------------------------------------------------
show("5. elements / total / update / subtract")

c2 = Counter("aabbbc")          # a=2, b=3, c=1
print("c2                =", c2)
print("sorted(elements())=", sorted(c2.elements()), " 按计数把元素展开回去")
print("total()           =", c2.total(), " 所有计数之和")

c2.update("aaaa")               # 注意：是"累加"，不是替换
print("update('aaaa')    =", c2)

c2.subtract("aa")               # 注意：是"累减"
print("subtract('aa')    =", c2)

c2.subtract("zzzz")
print("subtract('zzzz')  =", c2, " 负数和 0 会被保留下来")
print("负数项仍然会出现在 most_common 里:", c2.most_common()[-1])

print()
print("对比一下：A - B 会丢掉非正数项，subtract() 会保留，两者语义不同")


# ---------------------------------------------------------------
# 6. 实战
# ---------------------------------------------------------------
show("6. 实战")

import re

# 6.1 统计一段文本的词频
text = """
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
"""
freq = Counter(re.findall(r"[a-z]+", text.lower()))
print("出现最多的 5 个词:")
for word, n in freq.most_common(5):
    print(f"   {word:<8} {n}")

# 6.2 字母异位词（anagram）：Counter 相等只看计数，不看顺序
print()
print('Counter("silent") == Counter("listen"):', Counter("silent") == Counter("listen"))
print('Counter("apple")  == Counter("apply") :', Counter("apple") == Counter("apply"))

# 6.3 众数：出现次数最多的那个元素
votes = ["red", "blue", "red", "green", "red", "blue"]
print()
print("投票结果:", Counter(votes))
print("众数    :", Counter(votes).most_common(1)[0][0])

# 6.4 找出只出现一次的元素
print("只出现一次:", [k for k, n in Counter(votes).items() if n == 1])


show("做完了？去 99_exercises.py 做第 1 节练习")
