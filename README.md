# py_learn

Python 学习笔记。每个主题一个独立目录，里面是**可以跑的教程 + 自动判分的练习**。
不依赖任何第三方库，只用标准库。

## 目录

| 目录 | 主题 | 讲解 | 练习 |
|---|---|---|---|
| [`collections_study/`](collections_study/) | collections 容器模块 | 5 节 | 13 题 |
| [`oop_study/`](oop_study/) | 面向对象（类、对象、元类） | 20 节 | 30 题 |
| [`concurrency_study/`](concurrency_study/) | 并发（线程、进程、协程） | 12 节 | 18 题 |

合计 **37 个讲解文件 + 61 道练习题**，全部实跑验证过。

## 怎么用

进到任意一个目录，按编号顺序读：

```powershell
cd collections_study
python 01_counter.py
```

每个文件都是同一套结构：**先说不用它有多麻烦 → 给能跑的例子 → 指出坑 → 实战**。
直接运行就能看到输出，改里面的数据做实验是最快的学习方式。

读完一节，去做对应那几道题：

```powershell
python 99_exercises.py
```

练习册是**自动判分**的，一开始通过数是 0，那是待办清单而不是错误：

```
[FAIL] ex5_property_validation   设置 -1 应该抛 ValueError
[ OK ] ex11_singleton
...
通过 1/30
```

把 `TODO` 填掉再跑一次，看通过数往上涨。卡住了，参考答案在每个练习册文件的最底下，
但建议先自己想 5 分钟。

## 各目录简介

### collections_study

`collections` 模块里真正用得上的那几个容器：

| 文件 | 内容 |
|---|---|
| `01_counter.py` | 计数、`most_common`、缺失键返回 0 的陷阱 |
| `02_defaultdict.py` | 分组、邻接表、默认工厂 |
| `03_deque.py` | 双端队列、`maxlen`、和 list 的性能对比 |
| `04_namedtuple.py` | 具名元组、`_replace`、和 dataclass 的取舍 |
| `05_ordereddict_chainmap.py` | LRU 缓存、多层配置合并 |

### oop_study

从「怎么定义一个类」一直到「元类和描述符」，分三个阶段：

- **基础**（01-06）：类与对象、三种方法、封装与 property、继承与 MRO、魔术方法、生命周期与拷贝
- **进阶**（07-12）：描述符、`__slots__`、dataclass、Enum、抽象基类与 Protocol、运算符重载
- **高级**（13-18）：反射与动态属性、元类、上下文管理器、迭代器协议、设计模式、类型注解
- **专题深入**（19-20）：装饰器拆解、生成器完整能力

顺序是有依赖的。描述符和元类建立在阶段一的属性查找规则上，别跳着看。

### concurrency_study

线程、进程、协程三套模型，外加选型和排错：

- **打地基**（01）：并发 vs 并行、IO 密集 vs CPU 密集、GIL
- **线程**（02-05）：Thread、锁与信号量、队列、线程池
- **进程**（06-07）：Process、`if __name__` 守卫、进程池、进程间通信
- **协程**（08-10）：async/await、限流超时取消、异步实战
- **选型**（11-12）：三模型对比、常见陷阱与排错速查

> **Windows 用户注意**：多进程用的是 spawn 模式，所有开进程的代码必须写在
> `if __name__ == "__main__":` 守卫里。这个包里涉及多进程的文件都遵守该约定，可以当模板抄。

## 环境

- Python 3.13（大部分代码兼容 3.11+，少数用到了 3.11 的 `TaskGroup`、`except*`）
- 无第三方依赖

如果终端显示中文乱码，运行时加 UTF-8 开关：

```powershell
python -X utf8 01_counter.py
```

## 建议的节奏

一天一节，每节大约 20 分钟读 + 20 分钟做题。

别贪快。`Counter` 和 `defaultdict` 的手感是靠改数字试出来的，不是看出来的；
描述符和元类更是要反复回来查。三个包全走完大概两个月，慢一点没关系。
