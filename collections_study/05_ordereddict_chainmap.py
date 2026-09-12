# -*- coding: utf-8 -*-
"""
collections.OrderedDict 和 collections.ChainMap
================================================

运行：  python 05_ordereddict_chainmap.py
练习：  python 99_exercises.py   （第 5 节）

这两个用得比前三个少，但各有不可替代的场景：
  OrderedDict -> 需要「把某个键挪到最前/最后」的时候（LRU 缓存、FIFO 淘汰）
  ChainMap    -> 需要「多层配置叠加查找」的时候
"""

from collections import OrderedDict, ChainMap


def show(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# =================================================================
# 第一部分：OrderedDict
# =================================================================
show("1. OrderedDict 现在还需要吗？")

# 从 Python 3.7 起，普通 dict 也保证按插入顺序遍历了
d = {"b": 1, "a": 2, "c": 3}
od = OrderedDict([("b", 1), ("a", 2), ("c", 3)])

print("普通 dict    :", d, " (3.7+ 也保序)")
print("OrderedDict  :", od)
print("遍历结果一样 :", list(d) == list(od))

print()
print("所以「只想保序」已经不需要 OrderedDict 了。它只剩两个独家能力：")
print("  move_to_end(key, last=True)  把一个键挪到末尾或开头")
print("  popitem(last=False)          从开头弹出（普通 dict 只能从末尾弹）")


show("2. 独家能力：move_to_end 和 popitem(last=False)")

od2 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print("原始            :", dict(od2))

od2.move_to_end("a")
print("move_to_end(a)  :", dict(od2), " a 跑到最后")

od2.move_to_end("c", last=False)
print("move_to_end(c, last=False):", dict(od2), " c 跑到最前")

print("popitem(last=True) :", od2.popitem(last=True), " 从末尾弹")
print("popitem(last=False):", od2.popitem(last=False), " 从开头弹")


show("3. 一个反直觉的点：相等比较时它「顺序敏感」")

o1 = OrderedDict([("x", 1), ("y", 2)])
o2 = OrderedDict([("y", 2), ("x", 1)])
print("两个 OrderedDict 内容相同但顺序不同:", o1 == o2, " <- False！")
print("普通 dict 的同样对比              :", {"x": 1, "y": 2} == {"y": 2, "x": 1}, " <- True")
print("OrderedDict 和普通 dict 比        :", o1 == {"y": 2, "x": 1}, " <- True，跟普通 dict 比就不看顺序")


show("4. 实战：用 OrderedDict 写一个 LRU 缓存")


class LRUCache:
    """容量满了就淘汰「最久没被访问过」的那一项。"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return None
        self.data.move_to_end(key)      # 刚被用过 -> 标成最新
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)   # 淘汰队首 = 最久未用

    def __repr__(self):
        return f"LRU({dict(self.data)})"


cache = LRUCache(3)
for k in ["a", "b", "c"]:
    cache.put(k, k.upper())
print("放入 a,b,c   :", cache)

cache.get("a")                  # 访问 a，a 变新鲜
print("访问 a 之后  :", cache)

cache.put("d", "D")             # 挤掉一个
print("放入 d 之后  :", cache, " <- b 被淘汰了，因为它是最近最少使用的")


# =================================================================
# 第二部分：ChainMap
# =================================================================
show("5. ChainMap：多层字典叠起来查找")

defaults = {"color": "red", "size": "M", "debug": False}
env_vars = {"debug": True}
cmd_args = {"color": "blue"}

config = ChainMap(cmd_args, env_vars, defaults)

print("查找顺序：cmd_args -> env_vars -> defaults（从左往右，先命中先用）")
print()
print("  config['color'] =", config["color"], " <- 来自 cmd_args")
print("  config['debug'] =", config["debug"], " <- 来自 env_vars")
print("  config['size']  =", config["size"], "  <- 来自 defaults")

print()
print("底层就是这几个字典：")
for i, m in enumerate(config.maps):
    print(f"  maps[{i}] = {m}")

print()
print("对 ChainMap 来说它们是一体的：")
print("  'size' in config  =", "size" in config)
print("  len(config)       =", len(config), " 三个字典的键并起来")
print("  dict(config)      =", dict(config), " 合并后的完整视图")


show("6. 关键：写入只会落到最前面那层")

config["size"] = "L"            # 写进 cmd_args，不动 defaults
print("写入 config['size'] = 'L' 之后：")
print("  cmd_args =", cmd_args, " <- 改了这里")
print("  defaults =", defaults, " <- 原封不动")

print()
print("这个特性正好用来实现「局部覆盖，不污染全局」")


show("7. new_child()：临时盖一层上去")

base = ChainMap({"a": 1, "b": 2})
print("base          :", dict(base))

temp = base.new_child({"b": 99})
print("new_child 之后:", dict(temp), " b 被临时覆盖")
print("base 没变     :", dict(base))
print()
print("临时改完就丢掉 temp，base 干干净净 —— 这就是「作用域」的雏形")


show("8. 实战：命令行参数 > 环境变量 > 默认配置")


def get_setting(name, cli=None, env=None, default_cfg=None):
    layers = []
    if cli:
        layers.append(cli)
    if env:
        layers.append(env)
    if default_cfg:
        layers.append(default_cfg)
    return ChainMap(*layers).get(name)


print("只给默认值        :", get_setting("port", default_cfg={"port": 8000}))
print("环境变量覆盖      :", get_setting("port", env={"port": 9000},
                                          default_cfg={"port": 8000}))
print("命令行参数优先级最高:", get_setting("port", cli={"port": 3000},
                                            env={"port": 9000},
                                            default_cfg={"port": 8000}))


show("做完了？去 99_exercises.py 做第 5 节练习")
