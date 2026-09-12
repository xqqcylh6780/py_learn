# py_learn

Python 学习笔记。每个主题一个独立目录，里面是**可以跑的教程 + 自动判分的练习**。
不依赖任何第三方库，只用标准库。

## 目录

| 目录 | 主题 | 讲解 | 练习 |
|---|---|---:|---:|
| [`01_python_core_study/`](01_python_core_study/) | Python 核心语法与语言语义 | 23 节 | 52 题 |
| [`02_collections_study/`](02_collections_study/) | collections 容器模块 | 5 节 | 13 题 |
| [`03_oop_study/`](03_oop_study/) | 面向对象（类、对象、元类） | 20 节 | 30 题 |
| [`04_exception_study/`](04_exception_study/) | 异常处理与错误设计 | 20 节 | 44 题 |
| [`05_module_package_study/`](05_module_package_study/) | 模块、包与导入机制 | 24 节 | 48 题 |
| [`06_file_io_study/`](06_file_io_study/) | 文件、路径与 I/O | 26 节 | 56 题 |
| [`07_logging_debug_study/`](07_logging_debug_study/) | 日志、诊断与调试 | 28 节 | 58 题 |
| [`08_testing_study/`](08_testing_study/) | 测试与 Mock | 32 节 | 60 题 |
| [`09_stdlib_study_complete/`](09_stdlib_study_complete/) | 高频 Python 标准库 | 32 节 | 64 题 |
| [`10_concurrency_study/`](10_concurrency_study/) | 并发（线程、进程、协程） | 12 节 | 18 题 |
| [`11_typing_advanced_study_complete/`](11_typing_advanced_study_complete/) | Python 类型系统进阶 | 32 节 | 64 题 |
| [`12_performance_study_complete/`](12_performance_study_complete/) | 性能分析与优化 | 10 章 | 60 题 |
| [`13_project_engineering_study_complete/`](13_project_engineering_study_complete/) | Python 项目工程化与交付 | 32 节 | 64 题 |

合计 **296 个讲解文件 + 631 道练习题**。

## 建议学习顺序

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
07_logging_debug_study
        ↓
08_testing_study
        ↓
09_stdlib_study_complete
        ↓
10_concurrency_study
        ↓
11_typing_advanced_study_complete
        ↓
12_performance_study_complete
        ↓
13_project_engineering_study_complete
```

从核心语言语义开始，依次补齐对象模型、错误处理、标准库、并发、类型与性能，最后学习完整项目交付。

## 怎么用

进到任意一个目录，按编号顺序读：

```powershell
cd 01_python_core_study
python 01_对象引用与身份.py
```

每个文件尽量保持同一套结构：

**概念 → 能跑的例子 → 常见坑 → 对应练习**

读完一节，再运行：

```powershell
python 99_exercises.py
```

练习册会自动判分。把 `TODO` 填掉再跑，看通过数往上涨。
参考答案在各自 `99_exercises.py` 最底部。

## 主题概要

### 01_python_core_study

变量与对象引用、可变/不可变、`is`/`==`、函数参数、解包、推导式、
一等函数、LEGB、闭包、切片、真值、模式匹配、海象运算符、常用内置函数和常见陷阱。

### 02_collections_study

`Counter`、`defaultdict`、`deque`、`namedtuple`、`OrderedDict`、`ChainMap`。

### 03_oop_study

从类和对象一直到描述符、元类、上下文管理器、迭代器、装饰器、类型注解与设计模式。

### 04_exception_study

异常模型、精准捕获、资源清理、诊断与 API 异常设计。

### 05_module_package_study

模块、包、导入机制、包资源与导入错误排查。

### 06_file_io_study

路径、文件读写、编码、归档、临时文件与文件系统安全。

### 07_logging_debug_study

日志设计、异常诊断、调试器、性能和内存分析。

### 08_testing_study

单元测试、Mock、异步测试、集成测试与测试质量。

### 09_stdlib_study_complete

其余高频标准库：文本、时间、数值、网络、子进程和运行环境工具。

### 10_concurrency_study

线程、进程、协程三套模型，外加并发选型和排错。

### 11_typing_advanced_study_complete

现代类型注解、泛型、Protocol、TypedDict、类型缩窄与静态检查工程实践。

### 12_performance_study_complete

性能测量、热点定位、内存分析、缓存与优化回归测试。

### 13_project_engineering_study_complete

虚拟环境、依赖复现、项目元数据、CLI、构建产物、CI、发布安全与跨平台部署。

## 环境

- 推荐 Python 3.13
- 大多数内容兼容 Python 3.11+
- `match/case` 需要 Python 3.10+
- 无第三方依赖

如果终端中文乱码：

```powershell
python -X utf8 01_对象引用与身份.py
```
