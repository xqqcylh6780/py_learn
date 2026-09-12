"""22 容器增长：Python 容器已有成熟增长策略，不要模仿 C 手工预分配一切。"""
items=[]
for i in range(10): items.append(i)
print(items)
print('已知结果时，推导式/list(range(...)) 往往比 Python 层循环 append 更简洁。')
print('但不要为了省几次扩容写复杂、难维护的预分配逻辑。')
