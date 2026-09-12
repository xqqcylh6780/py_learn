# 04_exception_study — Python 异常处理完整学习包

这一目录不是只教 `try/except` 语法，而是从 **Python 异常模型 → 精准捕获 → 异常链 → 自定义异常 → 资源清理 → 诊断日志 → ExceptionGroup → asyncio → API 设计** 完整走一遍。

目标是学完之后，你不仅会“处理报错”，还知道一个真实项目应该怎样设计失败路径。

## 环境

- 推荐 Python 3.13
- 大部分内容兼容 Python 3.11+
- `ExceptionGroup`、`except*`、`BaseException.add_note()`、`sys.exception()` 需要 Python 3.11+
- 只使用 Python 标准库

## 目录

| 文件 | 内容 |
|---|---|
| `01_异常是什么.py` | 异常对象、传播、栈展开、异常 vs 返回值 |
| `02_异常层次与内置异常.py` | BaseException / Exception、常见内置异常、继承关系 |
| `03_try_except精准捕获.py` | 匹配顺序、多个异常、缩小 try、边界捕获 |
| `04_else与finally.py` | else 成功路径、finally 清理、finally return 陷阱 |
| `05_raise与重新抛出.py` | 主动 raise、bare raise、NotImplementedError |
| `06_异常链与raise_from.py` | `__context__`、`__cause__`、`raise ... from`、`from None` |
| `07_自定义异常设计.py` | 异常层次、结构化字段、异常命名 |
| `08_异常边界与分层.py` | repository/service/endpoint 分层、恢复与传播 |
| `09_资源清理与上下文管理器.py` | 异常安全、with、contextmanager、ExitStack |
| `10_assert与异常.py` | assert 正确用途、`-O`、业务校验 |
| `11_traceback与诊断.py` | traceback、`sys.exception()`、诊断信息 |
| `12_logging记录异常.py` | `logger.exception`、`exc_info`、日志边界、脱敏 |
| `13_add_note与异常元数据.py` | Python 3.11 `add_note()` |
| `14_ExceptionGroup与except_star.py` | 多异常、`ExceptionGroup`、`except*` |
| `15_asyncio中的异常.py` | await 传播、超时、取消、TaskGroup |
| `16_warnings与异常的边界.py` | warnings 分类、过滤、stacklevel、何时不用异常 |
| `17_API异常契约与库设计.py` | 稳定错误契约、内置异常、自定义异常、接口边界 |
| `18_异常常见陷阱与实战清单.py` | 高频错误模式与项目检查清单 |
| `19_EAFP与LBYL.py` | EAFP/LBYL、TOCTOU、外部状态竞争窗口 |
| `20_系统级异常与程序边界.py` | KeyboardInterrupt、SystemExit、CancelledError、SyntaxError、CLI 边界 |
| `99_exercises.py` | 44 道自动判分练习 |

## 推荐学习方式

按编号顺序：

```powershell
cd 04_exception_study
python 01_异常是什么.py
python 02_异常层次与内置异常.py
...
```

每学一节，做对应练习：

```powershell
python 99_exercises.py
```

练习册中的 TODO 是故意留下的。一开始大量 `[FAIL]` / `[ERR]` 是正常的。

## 学完必须真正掌握的东西

你应该能够解释并实际写出：

- 为什么通常 `except Exception` 而不是 `except BaseException`
- 为什么 try 范围应该尽量小
- `else` 和把代码直接写在 try 后面的区别
- 为什么 `finally` 里不应该 `return`
- `raise`、`raise exc`、`raise NewError from exc` 的用途差异
- `__context__`、`__cause__`、`from None` 分别是什么
- 如何设计一个稳定的应用异常层次
- 什么时候应该捕获，什么时候应该继续向上传播
- 如何做到资源清理但不吞异常
- 为什么 assert 不能做权限/参数/业务校验
- 如何保存 traceback 又不把内部堆栈直接暴露给用户
- 为什么日志应在边界统一记录，而不是每层都打一遍
- `add_note()` 适合解决什么问题
- 为什么并发失败需要 `ExceptionGroup`
- `except*` 和普通 `except` 的处理模型有什么不同
- asyncio 中异常、超时、取消的关系
- warning 和 exception 应如何选择
- 一个公开 API 应如何定义自己的异常契约

## 和其他学习包的关系

建议总体顺序：

```text
01_python_core_study
        ↓
02_collections_study
        ↓
04_exception_study
        ↓
03_oop_study
        ↓
10_concurrency_study
```

实际上异常贯穿后面所有 Python 工程内容，因此建议尽早学。

下一阶段最适合继续补：

```text
05_module_package_study/
06_file_io_study/
07_logging_debug_study/
08_testing_study/
```
