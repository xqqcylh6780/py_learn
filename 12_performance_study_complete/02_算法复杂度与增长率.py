"""02 算法复杂度：先消灭数量级问题，再谈微优化。"""

def contains_list(xs, targets):
    return [x for x in targets if x in xs]

def contains_set(xs, targets):
    lookup = set(xs)
    return [x for x in targets if x in lookup]

xs = list(range(10_000)); targets = [1, 9999, 20_000]
print(contains_list(xs, targets))
print(contains_set(xs, targets))
print('list 成员测试通常 O(n)，set/dict 平均通常 O(1)。')
print('但 Big-O 只描述增长趋势，不等于真实常数时间。')
