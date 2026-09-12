# 07_logging_debug_study

Python 标准库日志与调试完整学习包。

这部分不是只教 `logging.basicConfig()`，目标是让你能够在真实项目里完成：

- 正确设计应用日志结构
- 解决重复日志、日志丢失、级别失效、编码和轮转问题
- 给日志增加 request_id / trace_id 等上下文
- 在线程、进程、asyncio 场景下安全收集日志
- 保存完整异常 traceback
- 使用 warnings、traceback、pdb、faulthandler、inspect 等诊断工具
- 用 cProfile / tracemalloc 区分 CPU 热点和内存问题
- 建立一套生产环境排错流程

全部内容只使用 Python 标准库。

## 课程目录

| # | 文件 | 核心内容 |
|---:|---|---|
| 01 | `01_为什么用logging而不是print.py` | logging 与 print 的职责边界 |
| 02 | `02_日志级别与有效级别.py` | DEBUG~CRITICAL、NOTSET、effective level |
| 03 | `03_Logger层级传播与重复日志.py` | logger 层级、parent、propagate、重复日志 |
| 04 | `04_Handler输出到不同目标.py` | StreamHandler、多目标输出、Handler 级别 |
| 05 | `05_Formatter与LogRecord.py` | Formatter、LogRecord、常用上下文字段 |
| 06 | `06_basicConfig的真实行为.py` | basicConfig 只配置一次、force=True |
| 07 | `07_文件日志编码与关闭.py` | FileHandler、UTF-8、关闭生命周期 |
| 08 | `08_日志轮转Rotating与TimedRotating.py` | 大小/时间轮转、backupCount、多进程风险 |
| 09 | `09_异常日志exc_info_stack_info_stacklevel.py` | logger.exception、exc_info、stack_info、stacklevel |
| 10 | `10_extra与LoggerAdapter结构化上下文.py` | extra、LoggerAdapter、请求上下文 |
| 11 | `11_Filter与上下文注入.py` | Filter 过滤与字段注入 |
| 12 | `12_QueueHandler与QueueListener.py` | 异步化日志 I/O、队列日志架构 |
| 13 | `13_dictConfig集中配置.py` | `logging.config.dictConfig` 工程配置 |
| 14 | `14_库代码应该如何记录日志.py` | `getLogger(__name__)`、NullHandler、库日志礼仪 |
| 15 | `15_warnings警告系统.py` | warnings、过滤、测试、转 logging |
| 16 | `16_traceback模块.py` | format_exc、TracebackException |
| 17 | `17_未捕获异常钩子.py` | sys/threading/unraisable hooks |
| 18 | `18_pdb_breakpoint与事后调试.py` | pdb、breakpoint、post_mortem |
| 19 | `19_inspect与调用栈.py` | signature、frame、调用者定位 |
| 20 | `20_faulthandler低级故障诊断.py` | 崩溃、卡死、线程栈 dump |
| 21 | `21_time_perf_counter与timeit.py` | 正确测时、微基准 |
| 22 | `22_cProfile与pstats.py` | CPU profile、cumtime/tottime |
| 23 | `23_tracemalloc内存追踪.py` | Python 内存分配追踪 |
| 24 | `24_线程协程调试与任务异常.py` | Thread/Task 异常、asyncio debug |
| 25 | `25_生产环境排错流程与反模式.py` | 排错流程、日志反模式、安全意识 |
| 26 | `26_ContextVar与LogRecordFactory.py` | asyncio 请求上下文、全局记录工厂 |
| 27 | `27_sys_settrace与调试器原理.py` | trace 事件、调试器底层思路 |
| 28 | `28_多进程网络日志与安全边界.py` | 多进程集中日志、SocketHandler/pickle 风险、shutdown |
| 99 | `99_exercises.py` | 58 道自动判分练习 |

## 推荐学习顺序

按编号从 01 学到 28。

前 14 节先把 **logging 系统本身**学扎实；15~20 是 **异常和调试工具**；21~23 是 **性能/内存诊断**；24~28 是 **并发和生产环境高级专题**。

```powershell
cd 07_logging_debug_study
python 01_为什么用logging而不是print.py
python 99_exercises.py
```

练习册初始应为：

```text
通过 0/58
```

## 学完以后应该能回答

1. 为什么 `logger.setLevel(DEBUG)` 后 DEBUG 仍可能不显示？
2. 为什么一条日志会出现两遍？`propagate` 到底做什么？
3. Logger 和 Handler 的 level 分别在什么时候过滤？
4. `basicConfig()` 为什么第二次调用常常没效果？
5. 为什么库代码不应该自己 `basicConfig()`？
6. `logger.exception()`、`exc_info=True`、`stack_info=True` 有什么区别？
7. 如何让日志显示真正调用者，而不是包装函数的位置？
8. 如何给每条日志自动添加 request_id？
9. 多线程/慢磁盘场景为什么适合 QueueHandler？
10. 多进程为什么不建议所有进程直接轮转同一个普通日志文件？
11. warnings 和 exception 的定位有什么不同？
12. 只有 `str(exc)` 为什么不足以排错？
13. 程序“卡死”但没有异常时应该看什么？
14. CPU 高、内存持续涨分别优先用什么工具？
15. asyncio Task 的异常为什么可能很晚才看到？
16. 为什么 `logger.debug(f"{expensive()}")` 在关闭 DEBUG 后仍可能浪费性能？
17. 为什么日志里不能直接输出 Token、密码、身份证号等敏感信息？
18. 为什么远端 SocketHandler/pickle 必须考虑信任边界？

## 工程建议

应用入口负责配置，业务模块只负责记录：

```python
# app.py
logging.config.dictConfig(...)

# service.py
logger = logging.getLogger(__name__)
```

不要让每个模块分别创建自己的日志文件和全局配置。

典型的生产日志应该至少考虑：

```text
time
level
logger/module
request_id / trace_id
process/thread/task（按需要）
message
exception traceback（异常时）
```

同时要做敏感字段脱敏，并配置合理的轮转与保留周期。

## 与其他学习包的关系

建议整体顺序：

```text
01_python_core_study
        ↓
02_collections_study
        ↓
03_oop_study
        ↓
04_exception_study
        ↓
05_module_package_study
        ↓
06_file_io_study
        ↓
07_logging_debug_study   ← 当前
        ↓
08_testing_study
```

下一阶段最适合学习 `08_testing_study`，因为日志、异常、文件和模块基础补齐后，就可以系统进入单元测试、mock、patch、临时文件、异步测试和测试设计。
