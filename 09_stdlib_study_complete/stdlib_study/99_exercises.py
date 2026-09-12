# -*- coding: utf-8 -*-
"""
标准库专题练习册 —— 64 题，自动判分
=================================

运行：
    python 99_exercises.py

规则：
- 每题都有 TODO 区域。
- 初始版本应为 0/64，而不是“有些题天然通过”。
- 参考答案在文件底部，仅建议卡住后查看。
"""

_checks = []

def check(fn):
    _checks.append(fn)
    return fn

@check
def ex01_cache_wrapper():
    """给函数加缓存，让相同参数只真正执行一次。"""
    from functools import lru_cache
    calls = {"n": 0}
    def raw(x):
        calls["n"] += 1
        return x * x
    # TODO_START
    cached = raw
    # TODO_END
    assert cached(3) == 9
    assert cached(3) == 9
    assert calls["n"] == 1

@check
def ex02_partial_request():
    """用 partial 固定 timeout=2。"""
    from functools import partial
    def request(url, *, timeout=5):
        return url, timeout
    # TODO_START
    fast = request
    # TODO_END
    assert fast("x") == ("x", 2)

@check
def ex03_wraps_metadata():
    """让装饰器保留原函数的 __name__。"""
    from functools import wraps
    def deco(fn):
        # TODO_START
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        # TODO_END
        return wrapper
    @deco
    def hello():
        return "hi"
    assert hello() == "hi"
    assert hello.__name__ == "hello"

@check
def ex04_singledispatch_int():
    """为 int 注册 singledispatch 实现。"""
    from functools import singledispatch
    @singledispatch
    def render(x):
        return "default"
    # TODO_START
    pass
    # TODO_END
    assert render(3) == "int:3"
    assert render("x") == "default"

@check
def ex05_itertools_islice():
    """从 count(10, 2) 取前 4 个。"""
    from itertools import count, islice
    # TODO_START
    result = []
    # TODO_END
    assert result == [10, 12, 14, 16]

@check
def ex06_chain_flatten_once():
    """使用 chain.from_iterable 展平一层。"""
    from itertools import chain
    data = [[1, 2], [3], [4, 5]]
    # TODO_START
    result = []
    # TODO_END
    assert result == [1, 2, 3, 4, 5]

@check
def ex07_combinations():
    """生成 ABC 两两组合。"""
    from itertools import combinations
    # TODO_START
    result = []
    # TODO_END
    assert result == [("A","B"), ("A","C"), ("B","C")]

@check
def ex08_groupby_all_keys():
    """先排序再 groupby，让同 key 聚到一起。"""
    from itertools import groupby
    data = [("A",1), ("B",2), ("A",3)]
    # TODO_START
    result = {}
    # TODO_END
    assert result == {"A":[1,3], "B":[2]}

@check
def ex09_itemgetter_sort():
    """按元组第 2 项升序。"""
    from operator import itemgetter
    data = [("a",3), ("b",1), ("c",2)]
    # TODO_START
    result = data
    # TODO_END
    assert result == [("b",1), ("c",2), ("a",3)]

@check
def ex10_methodcaller_strip():
    """用 methodcaller 调用 strip。"""
    from operator import methodcaller
    data = [" a ", " b "]
    # TODO_START
    result = data
    # TODO_END
    assert result == ["a", "b"]

@check
def ex11_regex_fullmatch():
    """验证订单号必须完整匹配 A-123 形式。"""
    import re
    # TODO_START
    valid = False
    invalid = True
    # TODO_END
    assert valid is True
    assert invalid is False

@check
def ex12_regex_named_group():
    """提取邮箱 user/domain 命名组。"""
    import re
    text = "mail: alice@example.com"
    # TODO_START
    result = {}
    # TODO_END
    assert result == {"user":"alice", "domain":"example.com"}

@check
def ex13_regex_sub_mask():
    """手机号中间四位替换成 ****。"""
    import re
    text = "13812345678"
    # TODO_START
    result = text
    # TODO_END
    assert result == "138****5678"

@check
def ex14_regex_multiline():
    """从多行日志里取 ERROR 行。"""
    import re
    text = "INFO a\nERROR boom\nINFO b"
    # TODO_START
    result = []
    # TODO_END
    assert result == ["ERROR boom"]

@check
def ex15_datetime_add_days():
    """日期加 30 天。"""
    from datetime import date, timedelta
    d = date(2026, 9, 12)
    # TODO_START
    result = d
    # TODO_END
    assert result == date(2026, 10, 12)

@check
def ex16_datetime_iso_roundtrip():
    """ISO 字符串解析回 datetime。"""
    from datetime import datetime
    text = "2026-09-12T18:30:00"
    # TODO_START
    result = None
    # TODO_END
    assert result == datetime(2026,9,12,18,30)

@check
def ex17_zoneinfo_to_utc():
    """把新加坡 aware datetime 转 UTC。"""
    from datetime import datetime, timezone
    from zoneinfo import ZoneInfo
    dt = datetime(2026,9,12,18,0,tzinfo=ZoneInfo("Asia/Singapore"))
    # TODO_START
    result = dt
    # TODO_END
    assert result.tzinfo == timezone.utc
    assert result.hour == 10

@check
def ex18_zoneinfo_fold():
    """构造纽约 DST 回拨时的第二个 01:30。"""
    from datetime import datetime
    from zoneinfo import ZoneInfo
    ny = ZoneInfo("America/New_York")
    # TODO_START
    result = datetime(2026,11,1,1,30,tzinfo=ny, fold=0)
    # TODO_END
    assert result.fold == 1
    assert result.utcoffset().total_seconds() == -5 * 3600

@check
def ex19_time_monotonic_clock():
    """选择适合计算超时的时钟函数。"""
    import time
    # TODO_START
    clock = time.time
    # TODO_END
    assert clock is time.monotonic

@check
def ex20_time_perf_counter():
    """选择适合短代码性能计时的高分辨率时钟。"""
    import time
    # TODO_START
    clock = time.time
    # TODO_END
    assert clock is time.perf_counter

@check
def ex21_decimal_exact():
    """用 Decimal 得到精确 0.3。"""
    from decimal import Decimal
    # TODO_START
    result = Decimal("0")
    # TODO_END
    assert result == Decimal("0.3")

@check
def ex22_decimal_quantize():
    """12.345 按 ROUND_HALF_UP 保留两位。"""
    from decimal import Decimal, ROUND_HALF_UP
    x = Decimal("12.345")
    # TODO_START
    result = x
    # TODO_END
    assert result == Decimal("12.35")

@check
def ex23_fraction_sum():
    """精确计算 1/3 + 1/6。"""
    from fractions import Fraction
    # TODO_START
    result = Fraction(0)
    # TODO_END
    assert result == Fraction(1,2)

@check
def ex24_fraction_limit():
    """把 float 0.1 近似成分母 <= 10 的分数。"""
    from fractions import Fraction
    # TODO_START
    result = Fraction(0.1)
    # TODO_END
    assert result == Fraction(1,10)

@check
def ex25_math_gcd_lcm():
    """求 12 和 18 的 gcd/lcm。"""
    import math
    # TODO_START
    result = (0, 0)
    # TODO_END
    assert result == (6, 36)

@check
def ex26_math_isclose():
    """正确判断 0.1+0.2 与 0.3 近似相等。"""
    import math
    # TODO_START
    result = False
    # TODO_END
    assert result is True

@check
def ex27_statistics_median():
    """计算中位数。"""
    from statistics import median
    data = [9,1,5,3,7]
    # TODO_START
    result = None
    # TODO_END
    assert result == 5

@check
def ex28_normaldist_cdf():
    """标准正态分布 CDF(0) 应为 0.5。"""
    from statistics import NormalDist
    # TODO_START
    result = 0.0
    # TODO_END
    assert abs(result - 0.5) < 1e-12

@check
def ex29_random_reproducible():
    """使用独立 Random(42) 生成可复现序列。"""
    import random
    # TODO_START
    result = []
    # TODO_END
    expected_rng = random.Random(42)
    expected = [expected_rng.randint(1,10) for _ in range(4)]
    assert result == expected

@check
def ex30_random_sample():
    """不放回抽 3 个元素。"""
    import random
    rng = random.Random(1)
    # TODO_START
    result = [1,1,1]
    # TODO_END
    assert len(result) == 3
    assert len(set(result)) == 3
    assert set(result) <= set(range(10))

@check
def ex31_secrets_hex_length():
    """生成 8 字节对应的 16 个十六进制字符。"""
    import secrets
    # TODO_START
    token = ""
    # TODO_END
    assert len(token) == 16
    int(token, 16)

@check
def ex32_compare_digest():
    """用安全比较函数比较两个 token。"""
    import secrets
    a = "abc123"
    b = "abc123"
    # TODO_START
    result = False
    # TODO_END
    assert result is True

@check
def ex33_uuid4_version():
    """生成 UUID4。"""
    import uuid
    # TODO_START
    u = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
    # TODO_END
    assert isinstance(u, uuid.UUID)
    assert u.version == 4

@check
def ex34_uuid5_deterministic():
    """相同 namespace/name 得到相同 UUID5。"""
    import uuid
    # TODO_START
    a = uuid.uuid4()
    b = uuid.uuid4()
    # TODO_END
    assert a == b
    assert a.version == 5

@check
def ex35_sha256():
    """计算 b'abc' 的 SHA-256 十六进制摘要。"""
    import hashlib
    # TODO_START
    result = ""
    # TODO_END
    assert result == hashlib.sha256(b"abc").hexdigest()
    assert len(result) == 64

@check
def ex36_hash_stream_update():
    """分块 update 得到与一次性 sha256 相同的摘要。"""
    import hashlib
    # TODO_START
    result = ""
    # TODO_END
    assert result == hashlib.sha256(b"hello world").hexdigest()

@check
def ex37_hmac_sha256():
    """计算 HMAC-SHA256。"""
    import hashlib, hmac
    key = b"k"
    msg = b"message"
    # TODO_START
    result = ""
    # TODO_END
    expected = hmac.new(key, msg, hashlib.sha256).hexdigest()
    assert result == expected

@check
def ex38_hmac_compare_digest():
    """用 compare_digest 比较签名。"""
    import hmac
    a = "a" * 64
    b = "a" * 64
    # TODO_START
    result = False
    # TODO_END
    assert result is True

@check
def ex39_base64_roundtrip():
    """Base64 编解码往返。"""
    import base64
    raw = b"hello\x00world"
    # TODO_START
    result = b""
    # TODO_END
    assert result == raw

@check
def ex40_base64_validate():
    """严格模式下非法 Base64 应抛 binascii.Error。"""
    import base64, binascii
    # TODO_START
    caught = False
    # TODO_END
    assert caught is True

@check
def ex41_heapq_topk():
    """取最大的 3 个数。"""
    import heapq
    data = [9,1,8,2,7,3]
    # TODO_START
    result = []
    # TODO_END
    assert result == [9,8,7]

@check
def ex42_heapq_priority():
    """按优先级从小到大弹出任务。"""
    import heapq
    heap = []
    for item in [(2,0,"B"), (1,1,"A"), (2,2,"C")]:
        heapq.heappush(heap, item)
    # TODO_START
    result = []
    # TODO_END
    assert result == ["A","B","C"]

@check
def ex43_bisect_bounds():
    """求 70 的左右插入位置。"""
    from bisect import bisect_left, bisect_right
    data = [60,70,70,80]
    # TODO_START
    result = (0,0)
    # TODO_END
    assert result == (1,3)

@check
def ex44_bisect_insort():
    """把 75 插入并保持有序。"""
    from bisect import insort
    data = [60,70,80]
    # TODO_START
    pass
    # TODO_END
    assert data == [60,70,75,80]

@check
def ex45_contextmanager_cleanup():
    """用 contextmanager 保证 finally 清理。"""
    from contextlib import contextmanager
    events = []
    # TODO_START
    @contextmanager
    def cm():
        yield
    # TODO_END
    with cm():
        events.append("work")
    assert events == ["work", "cleanup"]

@check
def ex46_contextlib_suppress():
    """只忽略 FileNotFoundError。"""
    from contextlib import suppress
    # TODO_START
    continued = False
    # TODO_END
    assert continued is True

@check
def ex47_inspect_keyword_only():
    """用 inspect 判断 timeout 是 KEYWORD_ONLY。"""
    import inspect
    def f(host, *, timeout=5):
        return host, timeout
    # TODO_START
    result = False
    # TODO_END
    assert result is True

@check
def ex48_inspect_bind():
    """用 Signature.bind 绑定调用参数。"""
    import inspect
    def f(a, b=2, *, c=3):
        pass
    sig = inspect.signature(f)
    # TODO_START
    result = {}
    # TODO_END
    assert result == {"a":1, "b":9, "c":4}

@check
def ex49_deepcopy():
    """深拷贝后修改内部列表不影响原对象。"""
    import copy
    original = [[1],[2]]
    # TODO_START
    copied = original.copy()
    # TODO_END
    copied[0].append(9)
    assert original == [[1],[2]]
    assert copied == [[1,9],[2]]

@check
def ex50_weakref_lifetime():
    """建立弱引用，并在对象释放后得到 None。"""
    import weakref, gc
    class Box: pass
    obj = Box()
    # TODO_START
    ref = lambda: "still-alive"
    # TODO_END
    del obj
    gc.collect()
    assert ref() is None

@check
def ex51_configparser_types():
    """从 INI 读取 int 和 bool。"""
    import configparser
    cfg = configparser.ConfigParser()
    cfg.read_string("[s]\nport=8080\ndebug=yes\n")
    # TODO_START
    result = ("8080", "yes")
    # TODO_END
    assert result == (8080, True)

@check
def ex52_tomllib_parse():
    """解析 TOML。"""
    import tomllib
    text = 'name="demo"\n[server]\nport=8000\n'
    # TODO_START
    result = {}
    # TODO_END
    assert result == {"name":"demo","server":{"port":8000}}

@check
def ex53_urlsplit():
    """解析 URL 的 hostname 和 port。"""
    from urllib.parse import urlsplit
    url = "https://example.com:8443/a?q=1"
    # TODO_START
    result = (None,None)
    # TODO_END
    assert result == ("example.com", 8443)

@check
def ex54_urlencode():
    """编码查询参数。"""
    from urllib.parse import urlencode, parse_qs
    params = {"q":"中文 空格","page":2}
    # TODO_START
    query = ""
    # TODO_END
    assert parse_qs(query) == {"q":["中文 空格"], "page":["2"]}

@check
def ex55_pformat():
    """把对象格式化成字符串。"""
    from pprint import pformat
    obj = {"b":2,"a":1}
    # TODO_START
    result = ""
    # TODO_END
    assert isinstance(result, str)
    assert "'a': 1" in result and "'b': 2" in result

@check
def ex56_textwrap_shorten():
    """把长文本缩到 width=20。"""
    import textwrap
    text = "Python standard library is useful for everyday programming"
    # TODO_START
    result = text
    # TODO_END
    assert len(result) <= 20
    assert result.endswith("...")

@check
def ex57_subprocess_capture():
    """启动当前 Python 子进程并捕获 stdout。"""
    import subprocess, sys
    # TODO_START
    result = ""
    # TODO_END
    assert result == "child-ok"

@check
def ex58_shlex_split():
    """按 shell 风格拆分带引号字符串。"""
    import shlex
    cmd = 'tool --name "hello world" --count 3'
    # TODO_START
    result = []
    # TODO_END
    assert result == ["tool","--name","hello world","--count","3"]

@check
def ex59_mappingproxy():
    """创建只读映射视图。"""
    from types import MappingProxyType
    source = {"x":1}
    # TODO_START
    proxy = source
    # TODO_END
    blocked = False
    try:
        proxy["y"] = 2
    except TypeError:
        blocked = True
    assert blocked is True
    source["x"] = 9
    assert proxy["x"] == 9

@check
def ex60_simple_namespace():
    """创建可用属性访问的简单命名空间。"""
    from types import SimpleNamespace
    # TODO_START
    obj = SimpleNamespace(host=None, port=None)
    # TODO_END
    assert obj.host == "127.0.0.1"
    assert obj.port == 8000

@check
def ex61_calendar_leap():
    """判断闰年规则。"""
    import calendar
    # TODO_START
    result = (False, True)
    # TODO_END
    assert result == (True, False)

@check
def ex62_calendar_month_days():
    """获取 2026-09 的天数。"""
    import calendar
    # TODO_START
    days = 0
    # TODO_END
    assert days == 30

@check
def ex63_sys_version_info():
    """得到当前 Python 主版本与次版本。"""
    import sys
    # TODO_START
    result = (0,0)
    # TODO_END
    assert result == (sys.version_info.major, sys.version_info.minor)
    assert result[0] == 3

@check
def ex64_platform_implementation():
    """获取 Python 实现名称。"""
    import platform
    # TODO_START
    result = ""
    # TODO_END
    assert result in {"CPython","PyPy","GraalVM","Jython"}
    assert result == platform.python_implementation()

def run_all():
    print("=" * 72)
    print("标准库专题练习册")
    print("=" * 72)
    passed = 0
    failed = 0
    errors = 0
    for fn in _checks:
        try:
            fn()
        except AssertionError as e:
            failed += 1
            print(f"[FAIL] {fn.__name__:<34} {e or '断言未通过'}")
        except Exception as e:
            errors += 1
            print(f"[ERR ] {fn.__name__:<34} {type(e).__name__}: {e}")
        else:
            passed += 1
            print(f"[ OK ] {fn.__name__:<34}")
    print("-" * 72)
    print(f"通过 {passed}/{len(_checks)}  FAIL={failed}  ERR={errors}")
    return passed, failed, errors

if __name__ == "__main__":
    run_all()

# ======================================================================
# 参考答案（注释形式，不会参与程序执行）
# ======================================================================

# ex01_cache_wrapper
# cached = lru_cache(maxsize=None)(raw)

# ex02_partial_request
# fast = partial(request, timeout=2)

# ex03_wraps_metadata
# @wraps(fn)
# def wrapper(*args, **kwargs):
#     return fn(*args, **kwargs)

# ex04_singledispatch_int
# @render.register
# def _(x: int):
#     return f"int:{x}"

# ex05_itertools_islice
# result = list(islice(count(10, 2), 4))

# ex06_chain_flatten_once
# result = list(chain.from_iterable(data))

# ex07_combinations
# result = list(combinations("ABC", 2))

# ex08_groupby_all_keys
# data.sort(key=lambda x: x[0])
# result = {k: [v for _, v in g] for k, g in groupby(data, key=lambda x: x[0])}

# ex09_itemgetter_sort
# result = sorted(data, key=itemgetter(1))

# ex10_methodcaller_strip
# result = list(map(methodcaller("strip"), data))

# ex11_regex_fullmatch
# pat = re.compile(r"[A-Z]-\d+")
# valid = pat.fullmatch("A-123") is not None
# invalid = pat.fullmatch("xxA-123") is not None

# ex12_regex_named_group
# m = re.search(r"(?P<user>[\w.]+)@(?P<domain>[\w.]+)", text)
# result = m.groupdict()

# ex13_regex_sub_mask
# result = re.sub(r"(?<=\d{3})\d{4}(?=\d{4})", "****", text)

# ex14_regex_multiline
# result = re.findall(r"^ERROR.*$", text, flags=re.MULTILINE)

# ex15_datetime_add_days
# result = d + timedelta(days=30)

# ex16_datetime_iso_roundtrip
# result = datetime.fromisoformat(text)

# ex17_zoneinfo_to_utc
# result = dt.astimezone(timezone.utc)

# ex18_zoneinfo_fold
# result = datetime(2026,11,1,1,30,tzinfo=ny, fold=1)

# ex19_time_monotonic_clock
# clock = time.monotonic

# ex20_time_perf_counter
# clock = time.perf_counter

# ex21_decimal_exact
# result = Decimal("0.1") + Decimal("0.2")

# ex22_decimal_quantize
# result = x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# ex23_fraction_sum
# result = Fraction(1,3) + Fraction(1,6)

# ex24_fraction_limit
# result = Fraction(0.1).limit_denominator(10)

# ex25_math_gcd_lcm
# result = (math.gcd(12,18), math.lcm(12,18))

# ex26_math_isclose
# result = math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)

# ex27_statistics_median
# result = median(data)

# ex28_normaldist_cdf
# result = NormalDist().cdf(0)

# ex29_random_reproducible
# rng = random.Random(42)
# result = [rng.randint(1,10) for _ in range(4)]

# ex30_random_sample
# result = rng.sample(range(10), k=3)

# ex31_secrets_hex_length
# token = secrets.token_hex(8)

# ex32_compare_digest
# result = secrets.compare_digest(a, b)

# ex33_uuid4_version
# u = uuid.uuid4()

# ex34_uuid5_deterministic
# a = uuid.uuid5(uuid.NAMESPACE_URL, "https://example.com/x")
# b = uuid.uuid5(uuid.NAMESPACE_URL, "https://example.com/x")

# ex35_sha256
# result = hashlib.sha256(b"abc").hexdigest()

# ex36_hash_stream_update
# h = hashlib.sha256()
# h.update(b"hello ")
# h.update(b"world")
# result = h.hexdigest()

# ex37_hmac_sha256
# result = hmac.new(key, msg, hashlib.sha256).hexdigest()

# ex38_hmac_compare_digest
# result = hmac.compare_digest(a, b)

# ex39_base64_roundtrip
# encoded = base64.b64encode(raw)
# result = base64.b64decode(encoded)

# ex40_base64_validate
# try:
#     base64.b64decode(b"@@@", validate=True)
# except binascii.Error:
#     caught = True

# ex41_heapq_topk
# result = heapq.nlargest(3, data)

# ex42_heapq_priority
# result = [heapq.heappop(heap)[2] for _ in range(len(heap))]

# ex43_bisect_bounds
# result = (bisect_left(data,70), bisect_right(data,70))

# ex44_bisect_insort
# insort(data, 75)

# ex45_contextmanager_cleanup
# @contextmanager
# def cm():
#     try:
#         yield
#     finally:
#         events.append("cleanup")

# ex46_contextlib_suppress
# with suppress(FileNotFoundError):
#     open("__missing_stdlib_study__")
# continued = True

# ex47_inspect_keyword_only
# p = inspect.signature(f).parameters["timeout"]
# result = (p.kind is inspect.Parameter.KEYWORD_ONLY)

# ex48_inspect_bind
# bound = sig.bind(1, 9, c=4)
# result = dict(bound.arguments)

# ex49_deepcopy
# copied = copy.deepcopy(original)

# ex50_weakref_lifetime
# ref = weakref.ref(obj)

# ex51_configparser_types
# result = (cfg["s"].getint("port"), cfg["s"].getboolean("debug"))

# ex52_tomllib_parse
# result = tomllib.loads(text)

# ex53_urlsplit
# p = urlsplit(url)
# result = (p.hostname, p.port)

# ex54_urlencode
# query = urlencode(params)

# ex55_pformat
# result = pformat(obj)

# ex56_textwrap_shorten
# result = textwrap.shorten(text, width=20, placeholder="...")

# ex57_subprocess_capture
# cp = subprocess.run(
#     [sys.executable, "-c", 'print("child-ok")'],
#     capture_output=True, text=True, check=True,
# )
# result = cp.stdout.strip()

# ex58_shlex_split
# result = shlex.split(cmd)

# ex59_mappingproxy
# proxy = MappingProxyType(source)

# ex60_simple_namespace
# obj = SimpleNamespace(host="127.0.0.1", port=8000)

# ex61_calendar_leap
# result = (calendar.isleap(2024), calendar.isleap(2100))

# ex62_calendar_month_days
# _, days = calendar.monthrange(2026, 9)

# ex63_sys_version_info
# result = (sys.version_info.major, sys.version_info.minor)

# ex64_platform_implementation
# result = platform.python_implementation()
