# collections 模块学习包

一套可以直接跑的教程 + 练习。不用装任何第三方库。

## 怎么用

按编号顺序来，每个文件都是「先讲为什么，再给例子，最后指出坑」：

```powershell
cd E:\py_learn\collections_study
python 01_counter.py
python 02_defaultdict.py
python 03_deque.py
python 04_namedtuple.py
python 05_ordereddict_chainmap.py
```

读完一个文件，就去 `99_exercises.py` 做对应那一节：

```powershell
python 99_exercises.py
```

它会自动判分。一开始全是 `[FAIL]` 是正常的，那就是你的待办清单：

```
[FAIL] ex1_top_words                期望 ['a', 'b']，实际是 None
[ OK ] ex2_is_anagram
...
通过 1/13
```

把 TODO 填掉，再跑一次，看着通过数往上涨。卡住了就去 `99_exercises.py`
最底下的「参考答案」，但建议先自己想 5 分钟。

## 建议的节奏

| 天 | 内容 | 目标 |
|---|---|---|
| 1 | `01_counter.py` + 第 1 节练习 | 会用它统计任何东西 |
| 2 | `02_defaultdict.py` + 第 2 节练习 | 彻底告别 `if key not in d` |
| 3 | `03_deque.py` + 第 3 节练习 | 知道什么时候 list 不够用 |
| 4 | `04_namedtuple.py` + 第 4 节练习 | 写出可读的记录类型 |
| 5 | `05_ordereddict_chainmap.py` + 第 5 节练习 | 认识这两个「偏门但有用」的工具 |

别贪快。每天一个类型，比一天看完五个有用得多。

## 速查表

### 选哪个？

| 你的需求 | 用这个 |
|---|---|
| 数数、还要取前 N 名 | `Counter` |
| 数数，但后面还要做别的 | `defaultdict(int)` |
| 把一堆东西按某个键分组 | `defaultdict(list)` |
| 分组顺便去重 | `defaultdict(set)` |
| 队列（先进先出） | `deque` + `popleft()` |
| 栈（后进先出） | `deque` 或 `list` |
| 只保留最近 N 条 | `deque(maxlen=N)` |
| 一条不可变的记录 | `namedtuple` |
| 一个会改来改去的对象 | `dataclass`（不在本模块） |
| 把某个键挪到队首/队尾 | `OrderedDict.move_to_end()` |
| 多层配置叠加 | `ChainMap` |
| 只是要一个有序的字典 | 普通 `dict` 就够了 |

### 方法速查

```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap

# ---------- Counter ----------
c = Counter("aabbb")
c["z"]                    # 0，且不会写入（大坑）
c.most_common(2)          # [('b', 3), ('a', 2)]
c.total()                 # 总计数
c.update("aa")            # 累加
c.subtract("bb")          # 累减，可减成负数
Counter(a) + Counter(b)   # 加（丢掉非正数）
Counter(a) - Counter(b)   # 减（丢掉非正数）
Counter(a) & Counter(b)   # 取较小值
Counter(a) | Counter(b)   # 取较大值

# ---------- defaultdict ----------
d = defaultdict(list)
d["k"].append(1)          # 键不存在也不报错
d.get("k")                # 读但不创建
"k" in d                  # 判断但不创建

# ---------- deque ----------
dq = deque([1, 2, 3], maxlen=5)
dq.append(4); dq.appendleft(0)
dq.pop(); dq.popleft()
dq.rotate(1)              # 右移一位，负数左移
dq.extendleft([7, 8])     # 注意：会倒序插进去
dq[0]                     # O(1)
dq[3]                     # O(n)！这是 deque 的短板

# ---------- namedtuple ----------
Point = namedtuple("Point", ["x", "y"], defaults=[0])
p = Point(1, 2)
p.x; p[0]                 # 两种读法都行
p._asdict()               # 转字典
p._replace(x=9)           # 复制并改字段
Point._make([1, 2])       # 从序列构造
Point._fields             # ('x', 'y')

# ---------- OrderedDict ----------
od = OrderedDict([("a", 1), ("b", 2)])
od.move_to_end("a")             # 挪到末尾
od.move_to_end("a", last=False) # 挪到开头
od.popitem(last=False)          # 从开头弹

# ---------- ChainMap ----------
cfg = ChainMap(override, base)  # 左边优先
cfg["k"]                        # 从左往右找第一个命中
cfg["k"] = 1                    # 写入最左边那一层
cfg.new_child({"k": 2})         # 临时加一层
cfg.maps                        # 拿到底层字典列表
```

## 几个高频坑，先记住

1. `Counter` 的 `c[x]` 对缺失键返回 `0`，**但不会写入**；要写必须用 `c[x] += 1`。
2. `defaultdict` 用 `d[x]` **读**也会创建键。想只读不建，用 `.get()` 或 `in`。
3. `deque` 按下标访问是 O(n)，需要随机访问就用 `list`。
4. `deque.extendleft([1,2,3])` 插进去是 `3,2,1`，顺序是反的。
5. `namedtuple` 不可变，改字段要用 `_replace()` 得到新对象。
6. `OrderedDict` 之间比相等**看顺序**，但它和普通 `dict` 比时又不看顺序。
7. `ChainMap` 的写操作只作用于最前面那层，不会去改后面的。

## 小提示

如果你的终端显示中文乱码，运行时加上 UTF-8 开关：

```powershell
python -X utf8 01_counter.py
```
