# 13_project_engineering_study_complete

这一目录讲的是：**如何把“能跑的 Python 代码”变成一个可长期维护、可安装、可测试、可构建、可发布、可部署的 Python 工程。**

目标 Python：**3.13 主线**，大多数思想适用于 3.11+。

## 课程目录

| 节 | 主题 |
|---:|---|
| 01 | 从脚本到工程 |
| 02 | 虚拟环境 venv |
| 03 | `python -m` 与解释器一致性 |
| 04 | requirements 与 constraints |
| 05 | 依赖可复现与锁定策略 |
| 06 | `pyproject.toml` 总览 |
| 07 | build-system 与构建后端 |
| 08 | `[project]` 元数据与依赖 |
| 09 | src layout 与 flat layout |
| 10 | 分发名、包名与 import 名 |
| 11 | 包资源与 `importlib.resources` |
| 12 | 版本号与版本来源 |
| 13 | argparse CLI 设计 |
| 14 | `__main__.py` 与 `python -m` |
| 15 | console scripts / entry points |
| 16 | 配置分层与环境变量 |
| 17 | secrets 与凭据管理 |
| 18 | 应用数据目录与路径策略 |
| 19 | 退出码与错误边界 |
| 20 | subprocess 工程写法 |
| 21 | `importlib.metadata` |
| 22 | sdist 与 wheel |
| 23 | wheel / dist-info 结构 |
| 24 | editable install |
| 25 | 本地开发工作流 |
| 26 | 发布与供应链安全 |
| 27 | pipx 与 CLI 应用分发 |
| 28 | Git / 版本 / CHANGELOG |
| 29 | CI 持续集成 |
| 30 | 质量门禁 |
| 31 | Docker 与容器边界 |
| 32 | Windows 打包部署与最终工程清单 |

另有：

- `99_exercises.py`：64 道自动判分题
- `examples/sample_app/`：最小可安装 `src` layout CLI 示例
- `PROJECT_TEMPLATE.md`：新项目结构模板
- `RELEASE_CHECKLIST.md`：发布检查表
- `VALIDATION.txt`：本学习包验证结果

## 推荐学习方式

每学完一节，做对应两道题：

```powershell
python 01_从脚本到工程.py
python 99_exercises.py
```

32 节按交付链路拆分，练习函数名直接说明所考查的主题。多数中段章节对应连续两题，例如第 13 节对应 `ex23`、`ex24`；第 01、02、24、32 节因综合题和交叉主题不严格保持两题一节。每组练习至少有一道要求实现函数并通过多个输入，学习时按函数名定位相关章节，不要只依赖题号换算。

工程化不能只看代码。建议把 `examples/sample_app/` 单独复制出来，实际创建虚拟环境并做 editable install：

```powershell
cd examples/sample_app
python -m venv .venv
# 激活 .venv
python -m pip install -e .
demo-engineering Alice
python -m demo_app Alice
```

如需真正构建 wheel/sdist，在自己的开发环境安装构建前端后执行：

```powershell
python -m build
```

## 必须建立的工程观念

1. **venv 是可丢弃环境，不是项目资产。**
2. **库的依赖兼容范围和应用的可复现锁定不是一回事。**
3. **`pyproject.toml` 是现代 Python 项目元数据和构建配置入口。**
4. **构建成功不等于发布成功；发布成功也不等于部署成功。**
5. **CI 应从干净环境验证项目。**
6. **secret 不进入 Git、镜像、日志、异常信息和测试快照。**
7. **最终交付物要做安装/启动 smoke test。**
8. **生产发布必须可以追溯并考虑回滚。**

## 与其他学习包的关系

```text
01_python_core_study
02_collections_study
03_oop_study
04_exception_study
05_module_package_study
06_file_io_study
07_logging_debug_study
08_testing_study
09_stdlib_study_complete
10_concurrency_study
11_typing_advanced_study_complete
12_performance_study_complete
13_project_engineering_study_complete
```

学完这一包，你的目标不再只是“会写 Python”，而是能把 Python 项目完整交付出去。
