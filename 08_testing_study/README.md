# 08_testing_study

Python 测试完整学习包。

目标不是只会写 `unittest.TestCase`，而是建立一套能真正用于项目的测试思维：

- 知道什么值得测，什么不该锁死
- 会写稳定、可重复、可独立运行的单元测试
- 会正确使用 `Mock / patch / autospec / AsyncMock`
- 会测试文件、环境变量、CLI、HTTP、SQLite、线程、asyncio
- 会定位 flaky test、顺序依赖和测试污染
- 理解覆盖率、变异测试、property-based testing 等现代测试思想
- 知道标准库 `unittest` 与 pytest/coverage/Hypothesis/tox 等生态如何衔接

这一目录的可运行主线只依赖 Python 标准库。

---

## 内容

### 第一阶段：测试地基

| 文件 | 内容 |
|---|---|
| `01_为什么要测试与测试边界.py` | 测试目标、行为、边界、测试层次 |
| `02_unittest最小结构.py` | TestCase、suite、runner |
| `03_TestCase断言家族.py` | 常用断言与专门断言 |
| `04_测试发现命名与组织.py` | discovery、命名、tests 目录 |
| `05_setUp_tearDown与fixture.py` | fixture 生命周期 |
| `06_addCleanup保证清理.py` | 失败时仍可靠清理资源 |
| `07_subTest与表驱动测试.py` | subTest、数据驱动 |
| `08_测试异常警告与日志.py` | assertRaises、assertWarns、assertLogs |

### 第二阶段：Mock 与依赖隔离

| 文件 | 内容 |
|---|---|
| `09_Mock基础.py` | Mock 基础、调用记录 |
| `10_patch必须补在使用处.py` | patch where looked up |
| `11_spec_spec_set与autospec.py` | 防止假接口与错误签名 |
| `12_return_value_side_effect与调用记录.py` | 返回值、异常、调用序列 |
| `13_MagicMock_PropertyMock与协议.py` | 魔术方法、property |
| `14_mock_open与文件依赖.py` | mock_open 与真实临时文件的取舍 |
| `15_依赖注入比过度patch更稳.py` | clock/rng/client 等依赖注入 |
| `31_测试替身stub_fake_spy_mock.py` | Dummy / Stub / Fake / Spy / Mock |

### 第三阶段：真实环境与确定性

| 文件 | 内容 |
|---|---|
| `16_临时文件目录与文件系统测试.py` | tempfile、Path |
| `17_环境变量与patch_dict.py` | 环境变量隔离 |
| `18_时间随机数UUID与确定性.py` | 非确定性来源与控制 |
| `21_CLI与subprocess测试.py` | CLI、退出码、stdout/stderr |
| `22_本地HTTP集成测试.py` | 本地 HTTP、随机空闲端口 |
| `23_SQLite集成测试.py` | 内存数据库集成测试 |

### 第四阶段：异步与并发测试

| 文件 | 内容 |
|---|---|
| `19_IsolatedAsyncioTestCase与AsyncMock.py` | async 测试 |
| `20_asyncio超时取消与后台任务测试.py` | timeout、cancel、任务清理 |
| `24_线程并发代码怎么测.py` | Event/Barrier/timeout，避免 sleep 猜时序 |

### 第五阶段：测试稳定性与维护

| 文件 | 内容 |
|---|---|
| `25_测试隔离与顺序依赖.py` | 测试污染、顺序依赖 |
| `26_flaky测试超时与重试.py` | flaky test 根因 |
| `27_skip_expectedFailure与条件测试.py` | skip、expectedFailure |
| `28_doctest及其边界.py` | 可执行文档示例 |
| `29_覆盖率变异测试与测试质量.py` | coverage、branch、mutation |
| `30_测试架构AAA与反模式.py` | Arrange/Act/Assert、测试反模式 |
| `32_pytest与现代测试工具生态.py` | pytest、coverage.py、Hypothesis、tox/nox、CI |

---

## 练习

`99_exercises.py` 共 **60 道自动判分题**。

运行：

```powershell
python 99_exercises.py
```

初始状态应为：

```text
通过 0/60 | FAIL=60 | ERR=0
```

完成全部题后：

```text
通过 60/60 | FAIL=0 | ERR=0
```

参考答案在文件底部，以注释形式保存，不影响练习运行。

---

## 推荐学习顺序

建议按编号主线：

```text
01 → 02 → ... → 30
```

然后再补：

```text
31 测试替身分类
32 pytest 与现代测试生态
```

每学 1~2 节就做对应练习，不建议先把所有教程看完再统一做题。

---

## 这一包学完后应该会什么

你应该能解释并实际处理：

- 为什么测试应该优先关注公开行为而不是内部实现
- 为什么 `patch()` 经常“明明 patch 了却没生效”
- `spec`、`spec_set`、`autospec` 的区别
- Stub、Fake、Spy、Mock 各适合什么场景
- 为什么依赖注入经常比大量 patch 更稳
- 如何测试异常、warning、日志
- 如何测试临时文件和环境变量又不污染机器
- 如何让时间、随机数、UUID 变得可测试
- 如何测试 `async def`、AsyncMock、超时和取消
- 为什么线程测试不能靠 `sleep`
- 如何给 HTTP 集成测试申请随机空闲端口
- 为什么每个测试都必须能够独立运行
- flaky test 最常见的根因是什么
- 为什么“代码覆盖率 100%”也可能测试质量很差
- 为什么 CI 中的重试不能代替修复竞态
- pytest 能改善哪些体验，但哪些测试设计原则与框架无关

---

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
07_logging_debug_study
        ↓
08_testing_study
```

后面可以继续：

```text
stdlib_study
typing_advanced_study
performance_study
project_engineering_study
```

其中 `project_engineering_study` 再把 pytest、coverage、CI、pyproject.toml、打包发布等真正接进完整项目。
