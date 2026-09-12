# 05_module_package_study — Python 模块与包完整专题

这一包不是只教 `import xxx`，而是把 Python 的**模块系统、包结构、导入机制和真实项目排错**串起来。

## 课程目标

学完后应该能解释并处理：

- `import` 到底创建/复用了什么对象；
- 为什么模块第一次导入会执行顶层代码；
- `sys.path`、`sys.modules`、`sys.meta_path` 分别负责什么；
- `__name__ == "__main__"` 为什么成立；
- 为什么包内模块应该经常用 `python -m` 运行；
- `__init__.py` 能做什么、不该做什么；
- 绝对导入、相对导入如何解析；
- 为什么会出现 partially initialized module；
- `TYPE_CHECKING` 如何降低类型注解造成的运行时循环依赖；
- `ModuleSpec`、Finder、Loader 在现代导入系统里的位置；
- namespace package 与普通 package 的区别；
- `.pyc` 和 `__pycache__` 到底是什么；
- 怎样正确读取包资源；
- 怎样设计插件式动态加载；
- 包级 API 和 re-export 怎样保持稳定；
- 如何系统排查 `ImportError` / `ModuleNotFoundError`。

## 目录

| # | 文件 | 核心主题 |
|---:|---|---|
| 01 | `01_模块是什么与import执行过程.py` | module 对象、导入基本流程 |
| 02 | `02___name__与__main__.py` | 入口语义与 main guard |
| 03 | `03_sys_path与模块搜索路径.py` | 模块搜索路径 |
| 04 | `04_包与__init__.py` | package 与包初始化 |
| 05 | `05_绝对导入与相对导入.py` | absolute / relative import |
| 06 | `06_import各种写法与命名空间.py` | 各类 import 绑定语义 |
| 07 | `07___all__与星号导入.py` | `__all__`、公共导出 |
| 08 | `08_sys_modules模块缓存.py` | 模块缓存与对象复用 |
| 09 | `09_importlib动态导入与reload.py` | 动态导入、reload 边界 |
| 10 | `10_python_m与包内可执行模块.py` | `python -m`、包入口 |
| 11 | `11_循环导入为什么发生.py` | partially initialized module |
| 12 | `12_TYPE_CHECKING与类型导入.py` | 类型专用依赖 |
| 13 | `13_ModuleSpec与导入元数据.py` | `__spec__`、loader、package metadata |
| 14 | `14_MetaPathFinder与Loader概念.py` | import finder/loader 协议 |
| 15 | `15_命名空间包NamespacePackage.py` | PEP 420 namespace package |
| 16 | `16___pycache__与pyc字节码缓存.py` | pyc 缓存与失效 |
| 17 | `17_importlib_resources包资源文件.py` | 标准包资源访问 |
| 18 | `18_项目目录结构与导入边界.py` | flat/src layout、依赖边界 |
| 19 | `19_导入副作用与启动性能.py` | import-time side effects |
| 20 | `20_插件式动态加载设计.py` | 动态插件加载与校验 |
| 21 | `21_模块级__getattr__与__dir__.py` | PEP 562 模块动态属性 |
| 22 | `22_包级公共API设计.py` | re-export 与稳定 API |
| 23 | `23_ImportError与ModuleNotFoundError排错.py` | 导入错误系统诊断 |
| 24 | `24_模块与包常见陷阱.py` | 高频坑总结 |
| -- | `99_exercises.py` | 48 道自动判分练习 |

另外包含 `demo_pkg/`，它只是教程用的小型演示包，用来让导入例子能够真实运行。

## 推荐学习顺序

按 `01 -> 24` 顺序学习，每节完成后去练习册做对应两题。

```powershell
cd 05_module_package_study
python 01_模块是什么与import执行过程.py
python 99_exercises.py
```

## 重要学习原则

### 1. 不要背“当前目录就能 import”

真正要理解的是启动方式、`sys.path` 和包语境。不同入口的 `sys.path[0]` 可以不同。

### 2. 不要通过疯狂 `sys.path.append()` 修项目

那通常只是把项目结构问题变成环境依赖问题。

### 3. import 会执行代码

所以导入不可信 Python 模块不属于“安全读取配置”。模块顶层也应减少昂贵副作用。

### 4. 循环导入通常是架构信号

局部 import 有时合理，但长期应检查依赖方向和公共层设计。

### 5. 模块不等于 `.py` 文件

现代导入系统还能处理内建模块、扩展模块、namespace package、zip/自定义 loader 等来源。

## 环境

- 推荐 Python 3.11+
- 只使用标准库
- 所有教程按当前目录直接运行即可

## 下一阶段

完成本包后，推荐继续：

```text
06_file_io_study/
07_logging_debug_study/
08_testing_study/
stdlib_study/
typing_advanced_study/
performance_study/
project_engineering_study/
```
