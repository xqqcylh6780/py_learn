# Python 并发编程学习包

线程、进程、协程三套模型，12 个可运行文件 + 18 道自动判分的练习。
只用标准库，不需要装任何东西。

## 怎么用

```powershell
cd E:\py_learn\concurrency_study
python 01_并发基础与GIL.py
```

每个文件都是同一套结构：**先说现象 → 给能跑的例子 → 指出坑 → 讲选型**。
读完一个文件就去做对应那几道题：

```powershell
python 99_exercises.py
```

一开始 `通过 0/18` 是正常的，那就是待办清单。答案在文件最底下，
但建议先自己想 5 分钟。

## 完整路线图

### 第一部分 · 打地基

| 文件 | 讲什么 |
|---|---|
| `01_并发基础与GIL.py` | 并发 vs 并行、IO 密集 vs CPU 密集、GIL 限制了什么、串行/线程/进程三方实测 |

### 第二部分 · 线程（IO 密集的主力）

| 文件 | 讲什么 |
|---|---|
| `02_线程基础.py` | Thread、start/join、daemon、为什么线程杀不掉 |
| `03_线程同步.py` | 竞态实测、Lock、RLock、Semaphore、Event、死锁 |
| `04_队列与生产者消费者.py` | queue.Queue、毒丸、task_done、为什么队列能替代大部分锁 |
| `05_线程池.py` | ThreadPoolExecutor、Future、异常处理、map vs as_completed、超时 |

### 第三部分 · 进程（CPU 密集的唯一出路）

| 文件 | 讲什么 |
|---|---|
| `06_进程基础.py` | Process、**必须写 `if __name__ == '__main__'` 的原因**、进程不共享内存、进程池、启动开销实测 |
| `07_进程间通信.py` | Queue、Pipe、Manager、Value/Array 共享内存、pickle 限制 |

### 第四部分 · 协程（高并发 IO）

| 文件 | 讲什么 |
|---|---|
| `08_协程与asyncio基础.py` | async/await 的本质、串行 await vs gather、create_task、事件循环、忘了 await |
| `09_asyncio并发控制.py` | as_completed、超时、Semaphore 限流、TaskGroup、取消任务、asyncio.Queue |
| `10_异步IO实战.py` | **协程最大的坑：卡死事件循环**、to_thread、run_in_executor、重试+限流实战 |

### 第五部分 · 选型与排错

| 文件 | 讲什么 |
|---|---|
| `11_并发模型对比与选型.py` | 三模型总览、IO/CPU 两种场景的完整实测、决策流程、混合策略 |
| `12_常见陷阱.py` | 10 个高频坑的现象/原因/解法，加一张排错速查表 |

## 建议的节奏

| 天 | 内容 | 学完能做什么 |
|---|---|---|
| 1 | 01 | 拿到需求能判断该用哪种模型 |
| 2-3 | 02-05 | 能写线程池处理批量 IO，不会写出竞态和死锁 |
| 4-5 | 06-07 | 能写多进程处理 CPU 密集任务，知道怎么传数据 |
| 6-7 | 08-10 | 能写 asyncio 服务，不会踩阻塞事件循环的坑 |
| 8 | 11-12 | 能做技术选型，能快速定位并发 bug |

时间紧的话：**只读 01、03、05、10 这四节**，覆盖了日常 80% 的场景。

## 核心速查表

### 选哪个模型

```
任务是「算」为主还是「等」为主？
│
├─ 算为主（CPU 密集）──> 进程池
│                        asyncio 和线程都救不了你
│
└─ 等为主（IO 密集）
   │
   ├─ 并发量小（几十个）──> 线程池（最简单）
   └─ 并发量大（几百以上）─> asyncio
                             （库只有同步版就退回线程池）
```

### 三种模型对照

| | 线程 | 进程 | 协程 |
|---|---|---|---|
| 类型 | 并发 | 并行 | 并发 |
| 共享内存 | 是 | 否 | 是（但不需要锁） |
| 需要加锁 | 是 | 否 | 否 |
| 开销 | 中 | 高（约 60ms/个） | 极低 |
| 擅长 | IO 密集 | CPU 密集 | 高并发 IO |
| 数量级 | 几百 | CPU 核数 | 几万 |

### 常用 API 速查

```python
# ---------- 线程 ----------
import threading, queue
from concurrent.futures import ThreadPoolExecutor, as_completed

t = threading.Thread(target=fn, args=(1,), daemon=False)
t.start()
t.join()

lock = threading.Lock()
with lock:
    counter += 1                     # 读-改-写必须整块包住

sem = threading.Semaphore(3)         # 限制并发数
ev = threading.Event()               # ev.wait() / ev.set()

q = queue.Queue(maxsize=100)
q.put(item)
item = q.get(timeout=1)
q.task_done()                        # 配 task_done，join 才能返回

with ThreadPoolExecutor(max_workers=10) as pool:
    f = pool.submit(fn, 1)
    f.result(timeout=1)              # 必须取，否则异常被吞
    results = list(pool.map(fn, items))        # 保序
    for f in as_completed(futures):            # 谁先完成先处理
        print(f.result())

# ---------- 进程 ----------
import multiprocessing

if __name__ == "__main__":           # Windows 上必须写！
    p = multiprocessing.Process(target=fn, args=(1,))
    p.start()
    p.join()

    with multiprocessing.Pool(4) as pool:
        results = pool.map(fn, items)          # fn 必须在模块顶层

    q = multiprocessing.Queue()                # 跨进程传数据
    d = multiprocessing.Manager().dict()       # 共享字典（慢但省事）
    v = multiprocessing.Value("i", 0)          # 共享内存（快）
    with v.get_lock():
        v.value += 1

# ---------- 协程 ----------
import asyncio

async def main():
    one = await fetch()                        # 单个
    many = await asyncio.gather(f(), g())      # 并发（保序）
    task = asyncio.create_task(f())

    async for x in asyncio.as_completed([f(), g()]):   # 谁先完成先处理
        pass

    await asyncio.wait_for(slow(), timeout=1)  # 单任务超时

    sem = asyncio.Semaphore(3)                 # 限流
    async with sem:
        pass

    await asyncio.to_thread(blocking_fn)       # 包住同步阻塞函数

    async with asyncio.TaskGroup() as tg:      # 一个失败全部取消（3.11+）
        tg.create_task(f())

asyncio.run(main())
```

## 12 个最容易踩的坑

1. **有 GIL ≠ 线程安全**。`counter += 1` 是三步，中间会被切走（03 节）。
2. **用普通列表当队列**：判断、取值、删除之间会被切走，还会 O(n)（04 节）。
3. **毒丸数量不对**：两个消费者只放一颗 `None`，另一个永远等下去（12 节坑 4）。
4. **死锁**：多把锁的获取顺序不一致，互相等（03 节）。
5. **submit 之后不取 result**：异常被静默吞掉，日志里什么都没有（05、12 节）。
6. **daemon 线程写文件**：主线程一退就被掐断，数据烂掉（02、12 节）。
7. **多进程缺 `if __name__ == '__main__'`**：Windows 上疯狂开进程直到机器卡死（06、12 节）。
8. **把 lambda 传给进程**：pickle 失败，「单进程好好的，一上多进程就报错」（07 节）。
9. **协程里忘了 await**：任务从没执行，还不报错（08、12 节）。
10. **协程里调阻塞函数**：整个事件循环被卡死，全站变慢（10 节）。
11. **线程池开太大**：CPU 密集只会互相抢 GIL；IO 密集可能被封 IP（05 节）。
12. **忘了 join**：主线程先跑完，收集到的数据少一半（02 节）。

## Windows 用户特别注意

多进程在 Windows 上用的是 **spawn** 模式，子进程会重新导入你的模块。
所以下面这条是硬性要求，少一次都不行：

```python
def main():
    ...                     # 所有开进程的代码放这里

if __name__ == "__main__":
    main()
```

本学习包里所有涉及多进程的文件都遵守这个约定，可以当模板抄。

## 小提示

终端中文乱码的话，运行时加 UTF-8 开关：

```powershell
python -X utf8 01_并发基础与GIL.py
```
