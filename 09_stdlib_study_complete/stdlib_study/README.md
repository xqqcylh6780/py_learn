# Python 标准库专题学习包

这个目录不是“把标准库目录抄一遍”，而是按**真实项目使用频率、容易踩坑程度、可迁移性**筛出的标准库核心课程。

目标不是记住每个 API，而是建立这几个能力：

- 看到问题时知道标准库里是否已经有成熟工具；
- 知道模块的正确边界，而不是“能跑就行”；
- 分清编码、哈希、认证、随机数、UUID、加密这些容易混淆的概念；
- 正确处理时间、时区、十进制、浮点误差、排序、优先队列、URL、子进程等工程问题；
- 能读官方文档，并知道什么时候该选第三方库而不是继续硬用标准库。

## 课程目录

| 节 | 文件 | 核心内容 |
|---:|---|---|
| 01 | `01_functools_cache_partial.py` | `cache`、`lru_cache`、`cached_property`、`partial`、缓存失效边界 |
| 02 | `02_functools_wraps_singledispatch.py` | `wraps`、`singledispatch`、`reduce` |
| 03 | `03_itertools核心迭代器.py` | `count/cycle/repeat/chain/islice/takewhile/dropwhile` |
| 04 | `04_itertools组合分组与batched.py` | 排列组合、`groupby`、`pairwise`、`batched` |
| 05 | `05_operator函数化运算.py` | `itemgetter/attrgetter/methodcaller` |
| 06 | `06_re正则基础.py` | 匹配、搜索、完整匹配、捕获组、命名组、`finditer` |
| 07 | `07_re进阶替换边界与灾难性回溯.py` | 替换、flags、边界、贪婪、ReDoS 风险 |
| 08 | `08_datetime日期时间基础.py` | `date/datetime/timedelta`、ISO 8601、解析格式化 |
| 09 | `09_zoneinfo时区与DST.py` | aware/naive datetime、UTC、IANA 时区、DST、`fold` |
| 10 | `10_time时钟与计时.py` | `time/monotonic/perf_counter/process_time` 的区别 |
| 11 | `11_decimal精确十进制.py` | `Decimal`、上下文、精度、`quantize`、舍入 |
| 12 | `12_fractions有理数.py` | `Fraction`、精确有理运算 |
| 13 | `13_math数学函数.py` | `gcd/lcm/comb/perm/fsum/isclose/isfinite` |
| 14 | `14_statistics统计函数.py` | 均值、中位数、众数、方差、分位数、`NormalDist` |
| 15 | `15_random伪随机.py` | 随机抽样、洗牌、权重、可复现、非安全随机 |
| 16 | `16_secrets安全随机.py` | 安全 Token、`randbelow`、`compare_digest` |
| 17 | `17_uuid唯一标识.py` | UUID4、UUID5、解析、唯一性与保密性的区别 |
| 18 | `18_hashlib摘要与文件哈希.py` | SHA-2/SHA-3/BLAKE2、流式哈希、`file_digest`、PBKDF2 边界 |
| 19 | `19_hmac消息认证.py` | HMAC、消息完整性、`compare_digest` |
| 20 | `20_base64与binascii.py` | Base64、URL-safe Base64、hex、严格校验、编码≠加密 |
| 21 | `21_heapq优先队列.py` | 最小堆、Top K、优先队列、tie-breaker |
| 22 | `22_bisect有序序列.py` | 二分边界、有序插入、复杂度、`key` |
| 23 | `23_contextlib上下文工具.py` | `contextmanager/suppress/nullcontext/ExitStack/redirect_stdout` |
| 24 | `24_inspect运行时反射.py` | `signature/bind/getmembers`、运行时反射边界 |
| 25 | `25_copy与weakref.py` | 浅拷贝、深拷贝、弱引用、弱缓存 |
| 26 | `26_configparser与tomllib.py` | INI/TOML 读取、类型转换、配置与秘密的边界 |
| 27 | `27_urllib_parse_URL处理.py` | URL 拆解、查询参数、quote、`urljoin` 安全风险 |
| 28 | `28_pprint_textwrap_string.py` | 结构化展示、文本换行缩进、简单模板 |
| 29 | `29_subprocess与shlex.py` | 子进程、退出码、超时、参数拆分、shell 注入边界 |
| 30 | `30_collections_abc与types.py` | ABC 协议、`MappingProxyType`、`SimpleNamespace` |
| 31 | `31_calendar日历工具.py` | 闰年、月份天数、日历迭代 |
| 32 | `32_sys与platform运行环境.py` | Python/OS/venv/解释器运行环境信息 |
| 99 | `99_exercises.py` | 64 道自动判分练习 |

## 学习顺序

建议按编号学习，但可以分成 6 个阶段：

```text
阶段 1：函数与迭代
01 -> 05

阶段 2：文本与时间
06 -> 10

阶段 3：数字与统计
11 -> 14

阶段 4：随机、安全标识与摘要
15 -> 20

阶段 5：数据结构与运行时工具
21 -> 25

阶段 6：配置、URL、系统交互
26 -> 32
```

每学完一节，可以去 `99_exercises.py` 做对应的两题。

```powershell
python 01_functools_cache_partial.py
python 99_exercises.py
```

## 为什么有些标准库没有在这里重复

你的整个 `py_learn` 是按专题拆分的，所以这里**刻意不重复**已经有独立课程的内容：

- `collections` → `02_collections_study/`
- `pathlib / tempfile / shutil / glob / mmap / 文件哈希实践` → `06_file_io_study/`
- `logging / traceback / pdb / cProfile / tracemalloc` → `07_logging_debug_study/`
- `unittest / mock` → `08_testing_study/`
- `threading / multiprocessing / asyncio / queue` → `10_concurrency_study/`
- `Enum / dataclass / Protocol / 迭代器 / 上下文管理协议` 的语言与 OOP 部分 → `03_oop_study/`
- import 系统、`importlib`、包资源 → `05_module_package_study/`

这里会在需要时引用这些概念，但不把同一课程复制一遍。

## 几个必须真正理解的边界

### `random` vs `secrets`

游戏随机、模拟、测试复现可以使用 `random`。密码重置 Token、验证码、会话秘密等安全场景使用 `secrets`。

### `hashlib` vs `hmac` vs Base64

```text
Base64   = 编码，可逆，不保密
Hash     = 无密钥摘要，常用于完整性/指纹
HMAC     = 带密钥认证，验证“消息没改 + 对方知道密钥”
Encryption = 加密，不属于 Base64/普通 Hash/HMAC
```

### `datetime` vs `zoneinfo`

不要只会创建一个 `datetime` 就认为自己处理了时区。跨地区系统要明确区分 naive 和 aware datetime，并理解 DST。

### `Decimal` vs float

不是“float 永远不能用”。科学计算、图形、概率等大量场景本来就使用浮点数；但金额、税率、法定舍入规则等十进制业务应明确考虑 `Decimal`。

### `heapq` / `bisect` 的复杂度

`heapq` 适合不断取最小/最高优先级；`bisect` 的**查找位置**是 O(log n)，但向 Python list 中间插入仍是 O(n)。

### `subprocess`

默认优先：

```python
subprocess.run([program, arg1, arg2], shell=False)
```

不要把不可信用户输入拼成一整条 shell 字符串再 `shell=True`。

## Python 版本

本课程以 **Python 3.13** 为主要运行目标。

部分 API 的最低版本：

- `tomllib`：Python 3.11+
- `hashlib.file_digest`：Python 3.11+
- `itertools.pairwise`：Python 3.10+
- `itertools.batched`：Python 3.12+

整个仓库如果以 Python 3.13 学习，可以直接运行本包全部内容。

## 练习规则

`99_exercises.py` 初始状态应为：

```text
通过 0/64  FAIL=64  ERR=0
```

完成所有 TODO 后应达到：

```text
通过 64/64  FAIL=0  ERR=0
```

参考答案在练习册底部。建议先自己做，再对答案。

## 学完以后应该具备的能力

你不需要背完所有函数名，但应该能回答：

- 为什么超时计算用 `monotonic()` 而不是 `time()`？
- 为什么金额不能随手 `Decimal(0.1)`？
- 为什么 `groupby()` 前经常需要排序？
- `uuid4` 的“随机唯一”为什么不等于“秘密”？
- HMAC 和 SHA-256 的用途有什么本质区别？
- Base64 为什么不是加密？
- `heapq` 为什么需要 tie-breaker？
- `bisect` 查找是 O(log n)，为什么插入仍可能慢？
- 为什么 `urljoin()` 处理不可信绝对 URL 时可能改变域名？
- 为什么子进程调用通常应该传参数列表而不是拼 shell 字符串？

能解释这些，标准库这一阶段才算真正学会。
