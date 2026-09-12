# -*- coding: utf-8 -*-
"""
08_testing_study 自动判分练习册 —— 60 题
====================================

运行：
    python 99_exercises.py

目标：
- 未填写 TODO 时：0/60
- 完成全部题后：60/60

参考答案位于文件最底部。建议先独立完成。
"""

_CHECKS = []

def check(fn):
    _CHECKS.append(fn)
    return fn

@check
def ex01_boundary_cases():
    """为 normalize_age 设计最小但有意义的边界用例集合。"""
    def normalize_age(n):
        if not isinstance(n, int):
            raise TypeError
        if not 0 <= n <= 150:
            raise ValueError
        return n
    cases = None  # TODO: 至少覆盖 0、150、越界两侧
    assert cases == [(0, 0), (150, 150), (-1, ValueError), (151, ValueError)]

@check
def ex02_behavior_not_implementation():
    """测试应关注公开行为：计算折后价格。"""
    def final_price(price, discount):
        return round(price * (1 - discount), 2)
    result = None  # TODO
    assert result == 80.0

@check
def ex03_build_testcase():
    """写一个 TestCase 并运行，验证 add(2,3)==5。"""
    import unittest
    def add(a, b):
        return a + b
    class TestAdd(unittest.TestCase):
        def test_add(self):
            pass  # TODO
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
    result = unittest.TestResult()
    suite.run(result)
    assert result.testsRun == 1
    assert len(result.failures) == 0
    assert len(result.errors) == 0
    assert getattr(TestAdd.test_add, "__doc__", None) == "implemented"

@check
def ex04_loader_discovers_test():
    """让 unittest loader 能发现一个以 test_ 开头的方法。"""
    import unittest
    class Demo(unittest.TestCase):
        def check_value(self):  # TODO: 改名
            self.assertTrue(True)
    names = unittest.defaultTestLoader.getTestCaseNames(Demo)
    assert names == ["test_value"]

@check
def ex05_almost_equal():
    """使用 TestCase 的近似相等语义验证浮点结果。"""
    import unittest
    case = unittest.TestCase()
    ok = False
    # TODO: 对 0.1 + 0.2 与 0.3 做 7 位小数近似断言，然后 ok=True
    assert ok is True

@check
def ex06_count_equal():
    """忽略顺序但保留重复次数比较两个序列。"""
    import unittest
    case = unittest.TestCase()
    ok = False
    # TODO: [1,2,2] 与 [2,1,2]
    assert ok is True

@check
def ex07_fixture_fresh_each_time():
    """证明 setUp 为每个测试创建新的列表。"""
    import unittest
    shared_seed = []
    seen = []
    class Demo(unittest.TestCase):
        def setUp(self):
            self.items = shared_seed  # TODO：每个测试应创建新的列表
        def test_a(self):
            self.items.append(1)
            seen.append(self.items)
        def test_b(self):
            self.items.append(2)
            seen.append(self.items)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
    r = unittest.TestResult(); suite.run(r)
    assert not r.failures and not r.errors
    assert len(seen) == 2 and seen[0] is not seen[1]

@check
def ex08_add_cleanup():
    """用 addCleanup 注册清理动作。"""
    import unittest
    events = []
    class Demo(unittest.TestCase):
        def test_cleanup(self):
            # TODO
            events.append("body")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
    r = unittest.TestResult(); suite.run(r)
    assert events == ["body", "cleanup"]

@check
def ex09_subtest_cases():
    """用 subTest 验证多个平方结果。"""
    import unittest
    class Demo(unittest.TestCase):
        def test_square(self):
            cases = [(2, 4), (3, 9), (4, 16)]
            checked = 0
            for x, expected in cases:
                # TODO: with self.subTest(x=x): ...
                pass
            self.assertEqual(checked, 3)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
    r = unittest.TestResult(); suite.run(r)
    assert not r.failures and not r.errors

@check
def ex10_meaningful_test_name():
    """把测试方法命名成能表达行为的名字。"""
    import unittest
    class Demo(unittest.TestCase):
        def test1(self):
            pass
    names = unittest.defaultTestLoader.getTestCaseNames(Demo)
    assert names == ["test_expired_token_is_rejected"]

@check
def ex11_assert_raises_regex():
    """验证非法年龄抛 ValueError 且消息包含 >= 0。"""
    import unittest
    def parse_age(s):
        n = int(s)
        if n < 0:
            raise ValueError("age must be >= 0")
        return n
    case = unittest.TestCase()
    ok = False
    # TODO
    assert ok is True

@check
def ex12_assert_logs():
    """用 assertLogs 捕获指定 logger。"""
    import logging, unittest
    logger = logging.getLogger("course.test")
    case = unittest.TestCase()
    captured = None
    # TODO
    assert captured is not None
    assert any("started" in line for line in captured.output)

@check
def ex13_mock_return_value():
    """配置 Mock 的返回值并检查调用参数。"""
    from unittest.mock import Mock
    client = Mock()
    # TODO
    result = client.fetch("u1")
    assert result == {"name": "Alice"}
    client.fetch.assert_called_once_with("u1")

@check
def ex14_mock_call_count():
    """让 mock 被准确调用两次。"""
    from unittest.mock import Mock
    m = Mock()
    # TODO
    assert m.call_count == 2
    assert m.call_args_list[0].args == (1,)
    assert m.call_args_list[1].args == (2,)

@check
def ex15_patch_where_used():
    """patch 消费方模块中的名字，而不是原定义模块。"""
    import types, sys, textwrap
    from unittest.mock import patch
    src = types.ModuleType("_ex15_src"); src.rate=lambda:0.1; sys.modules["_ex15_src"]=src
    consumer = types.ModuleType("_ex15_consumer")
    exec(textwrap.dedent("""
    from _ex15_src import rate

    def price(x):
        return x*(1+rate())
    """), consumer.__dict__)
    sys.modules["_ex15_consumer"]=consumer
    result = None
    # TODO: patch _ex15_consumer.rate 为 0.2
    assert result == 120

@check
def ex16_patch_restores():
    """确认 patch 离开上下文后原值恢复。"""
    from unittest.mock import patch
    import os
    before = os.getcwd
    inside_changed = after_restored = False
    # TODO
    assert inside_changed and after_restored

@check
def ex17_spec_set_blocks_unknown():
    """使用 spec_set 阻止不存在属性。"""
    from unittest.mock import Mock
    class API:
        def send(self): pass
    m = Mock()  # TODO
    blocked = False
    try:
        m.no_such_attr
    except AttributeError:
        blocked = True
    assert blocked

@check
def ex18_autospec_signature():
    """用 autospec 检查方法签名。"""
    from unittest.mock import create_autospec
    class API:
        def send(self, user, amount, *, currency="CNY"): pass
    m = None  # TODO
    blocked = False
    if m is not None:
        try:
            m.send("u1")
        except TypeError:
            blocked = True
    assert blocked

@check
def ex19_side_effect_sequence():
    """side_effect 依次产生异常和成功结果。"""
    from unittest.mock import Mock
    m = Mock()
    # TODO
    first_timeout = False
    try:
        m()
    except TimeoutError:
        first_timeout = True
    second = m()
    assert first_timeout and second == "ok"

@check
def ex20_assert_has_calls():
    """验证调用顺序。"""
    from unittest.mock import Mock, call
    m = Mock()
    m("a"); m("b")
    ok = False
    # TODO
    assert ok

@check
def ex21_magicmock_context_manager():
    """配置 MagicMock 作为上下文管理器。"""
    from unittest.mock import MagicMock
    m = MagicMock()
    # TODO
    with m as value:
        result = value
    assert result == "resource"
    m.__enter__.assert_called_once()
    m.__exit__.assert_called_once()

@check
def ex22_propertymock():
    """临时替换 property。"""
    from unittest.mock import PropertyMock, patch
    class User:
        @property
        def name(self):
            return "real"
    result = None
    # TODO
    assert result == "mocked"

@check
def ex23_mock_open():
    """用 mock_open 测读取第一行。"""
    from unittest.mock import mock_open, patch
    def load_first(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.readline().strip()
    result = None
    # TODO
    assert result == "hello"

@check
def ex24_temp_directory():
    """用 TemporaryDirectory 做真实文件系统测试。"""
    import tempfile
    from pathlib import Path
    ok = False
    # TODO
    assert ok

@check
def ex25_fake_clock():
    """通过依赖注入测试过期判断。"""
    def expired(deadline, clock):
        return clock.now() >= deadline
    class FakeClock:
        def __init__(self, now): self.value = now
        def now(self):
            return -1  # TODO：返回 self.value
    clock = FakeClock(100)
    assert expired(90, clock) is True
    assert expired(110, clock) is False

@check
def ex26_fake_sender():
    """用 fake 而不是 patch 隐藏依赖。"""
    class FakeSender:
        def __init__(self):
            self.messages = []
        def send(self, user, message):
            pass  # TODO：记录消息
    def welcome(sender, user):
        sender.send(user, "welcome")
    sender = FakeSender()
    welcome(sender, "alice")
    assert sender.messages == [("alice", "welcome")]

@check
def ex27_patch_dict_env():
    """临时设置环境变量并自动恢复。"""
    import os
    from unittest.mock import patch
    before = os.environ.get("_COURSE_MODE")
    inside = None
    # TODO
    after = os.environ.get("_COURSE_MODE")
    assert inside == "test"
    assert after == before

@check
def ex28_seeded_random():
    """用独立 Random 实例得到确定结果。"""
    import random
    a = b = None  # TODO
    assert a == b
    assert a == [1, 5, 2, 7, 5]

@check
def ex29_asyncmock():
    """AsyncMock 要用 assert_awaited_once_with。"""
    import asyncio
    from unittest.mock import AsyncMock
    async def run():
        client = AsyncMock()
        # TODO
        result = await client.fetch(1)
        client.fetch.assert_awaited_once_with(1)
        return result
    result = asyncio.run(run())
    assert result == {"id": 1}

@check
def ex30_async_timeout():
    """用 asyncio.timeout 验证超时。"""
    import asyncio
    async def slow():
        await asyncio.sleep(0.05)
    async def run():
        timed_out = False
        # TODO
        return timed_out
    assert asyncio.run(run()) is True

@check
def ex31_async_cancel_cleanup():
    """取消 task 后仍要 await 它并观察 CancelledError。"""
    import asyncio
    async def run():
        cleaned = asyncio.Event()
        async def worker():
            try:
                await asyncio.sleep(10)
            finally:
                cleaned.set()
        task = asyncio.create_task(worker())
        await asyncio.sleep(0)
        # TODO
        return cleaned.is_set(), task.cancelled()
    assert asyncio.run(run()) == (True, True)

@check
def ex32_isolated_asyncio_testcase():
    """创建一个 IsolatedAsyncioTestCase。"""
    import unittest, asyncio
    class Demo(unittest.IsolatedAsyncioTestCase):
        async def test_value(self):
            await asyncio.sleep(0)
            # TODO
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
    r = unittest.TestResult(); suite.run(r)
    assert not r.failures and not r.errors
    assert getattr(Demo.test_value, "__doc__", None) == "implemented"

@check
def ex33_subprocess_capture():
    """运行子进程并捕获 stdout。"""
    import subprocess, sys
    proc = None  # TODO
    assert proc is not None
    assert proc.returncode == 0
    assert proc.stdout.strip() == "HELLO"

@check
def ex34_exit_code():
    """验证 CLI 非零退出码而不让 subprocess.run 直接抛异常。"""
    import subprocess, sys
    proc = None  # TODO
    assert proc is not None and proc.returncode == 3

@check
def ex35_ephemeral_port():
    """创建绑定 127.0.0.1:0 的本地服务器，让 OS 分配端口。"""
    from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
    class H(BaseHTTPRequestHandler):
        def log_message(self, *args): pass
    server = None  # TODO
    assert server is not None
    port = server.server_address[1]
    try:
        assert port > 0
    finally:
        server.server_close()

@check
def ex36_local_http_roundtrip():
    """启动本地 HTTP 服务并真实请求一次。"""
    from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
    from threading import Thread
    from urllib.request import urlopen
    body = None
    # TODO
    assert body == "OK"

@check
def ex37_sqlite_memory():
    """使用 :memory: SQLite，不污染磁盘。"""
    import sqlite3
    conn = None  # TODO
    assert conn is not None
    try:
        conn.execute("create table t(x integer)")
        conn.execute("insert into t values (1)")
        assert conn.execute("select x from t").fetchone()[0] == 1
    finally:
        conn.close()

@check
def ex38_sqlite_parameterized():
    """SQL 参数必须通过占位符传递。"""
    import sqlite3
    conn=sqlite3.connect(":memory:")
    try:
        conn.execute("create table users(name text)")
        name="O'Reilly"
        # TODO
        row=conn.execute("select name from users").fetchone()
        assert row == (name,)
    finally:
        conn.close()

@check
def ex39_thread_join_timeout():
    """线程 join 要带 timeout，并确认线程确实结束。"""
    import threading
    done=[]
    def worker(): done.append(1)
    t=threading.Thread(target=worker)
    # TODO
    assert done == [1] and not t.is_alive()

@check
def ex40_event_instead_of_sleep():
    """用 Event 建立同步点，不靠 sleep 猜时序。"""
    import threading
    ready=threading.Event()
    def worker():
        # TODO
        pass
    t=threading.Thread(target=worker); t.start()
    observed = ready.wait(timeout=1)
    t.join(timeout=1)
    assert observed and not t.is_alive()

@check
def ex41_restore_global_state():
    """测试修改全局状态后必须恢复。"""
    state={"mode":"prod"}
    before=state.copy()
    # TODO：临时改成 test，再恢复
    inside=None
    assert inside=="test"
    assert state==before

@check
def ex42_independent_tests():
    """每个测试自己建立数据，不能依赖前一个测试。"""
    import unittest
    class Demo(unittest.TestCase):
        shared=[]
        def test_a(self):
            self.shared.append(1)
        def test_b(self):
            # TODO：不要依赖 test_a 留下的共享状态
            self.assertEqual(self.shared, [])
    suite=unittest.TestSuite([Demo("test_a"), Demo("test_b")])
    r=unittest.TestResult(); suite.run(r)
    assert not r.failures and not r.errors

@check
def ex43_deterministic_uuid():
    """把 ID 生成器作为依赖传入。"""
    def create_user(name, id_factory):
        return {"id": id_factory(), "name": name}
    # TODO
    result = None
    assert result == {"id": "fixed-id", "name": "Alice"}

@check
def ex44_bounded_wait():
    """等待条件时必须有超时，而不是无限等待。"""
    import threading
    evt=threading.Event()
    result = None  # TODO: wait 一个很短的 timeout
    assert result is False

@check
def ex45_skip_decorator():
    """给测试加 skip，使其报告 skipped 而不是失败。"""
    import unittest
    class Demo(unittest.TestCase):
        def test_future(self):  # TODO
            self.fail("not ready")
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
    r=unittest.TestResult(); suite.run(r)
    assert len(r.skipped)==1 and not r.failures

@check
def ex46_expected_failure():
    """把已知 bug 标为 expectedFailure。"""
    import unittest
    class Demo(unittest.TestCase):
        def test_bug(self):  # TODO
            self.assertEqual(1,2)
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
    r=unittest.TestResult(); suite.run(r)
    assert len(r.expectedFailures)==1

@check
def ex47_doctest_example():
    """让 docstring 示例和函数真实行为一致。"""
    import doctest, types, textwrap
    m=types.ModuleType("_ex47")
    m.__dict__["__name__"]="_ex47"
    exec(textwrap.dedent("""
    def double(x):
        'Example: double(3) should be 999'
        return x*2
    """), m.__dict__)
    # TODO：把 docstring 改成真正的 doctest，期望 double(3) == 6
    m.double.__doc__ = """
    >>> double(3)
    999
    """
    failures, tests = doctest.testmod(m, verbose=False)
    assert failures==0 and tests==1

@check
def ex48_doctest_ellipsis():
    """使用 doctest ELLIPSIS 处理不稳定的中间文本。"""
    import doctest
    flags = 0  # TODO
    checker=doctest.OutputChecker()
    ok=checker.check_output("value=<...>", "value=<object at 0x1234>", flags)
    assert ok

@check
def ex49_assert_not_just_execute():
    """只执行函数不算有效测试，必须验证结果。"""
    def classify(x):
        return "positive" if x > 0 else "non-positive"
    checked = False
    classify(1)  # TODO
    assert checked

@check
def ex50_branch_cases():
    """覆盖 classify 的两个业务分支。"""
    def classify(x):
        return "positive" if x > 0 else "non-positive"
    cases = None  # TODO
    assert cases == [(1, "positive"), (0, "non-positive")]

@check
def ex51_aaa_structure():
    """按 Arrange/Act/Assert 完成一个清晰测试。"""
    def discount(price, rate):
        return price*(1-rate)
    price=100; rate=0.2  # Arrange
    result=None           # TODO Act
    # TODO Assert
    done=False
    assert done

@check
def ex52_one_behavior_per_test():
    """拆出对空输入的独立行为验证。"""
    def first(items):
        if not items: return None
        return items[0]
    result = "TODO"
    # TODO
    assert result is None

@check
def ex53_stub_vs_mock():
    """stub 提供结果；mock 还可验证交互。"""
    from unittest.mock import Mock
    gateway=Mock()
    # TODO
    paid=gateway.charge(100)
    assert paid is True
    gateway.charge.assert_called_once_with(100)

@check
def ex54_spy_wraps():
    """使用 wraps 做 spy：调用真实函数同时记录调用。"""
    from unittest.mock import Mock
    def real(x): return x*2
    spy = None  # TODO
    result = None
    assert result == 6
    spy.assert_called_once_with(3)

@check
def ex55_assert_warns():
    """验证 DeprecationWarning。"""
    import warnings, unittest
    def old():
        warnings.warn("deprecated", DeprecationWarning)
    case=unittest.TestCase()
    ok=False
    # TODO
    assert ok

@check
def ex56_assert_no_logs():
    """验证某段逻辑没有 WARNING 以上日志。"""
    import logging, unittest
    logger=logging.getLogger("_ex56")
    case=unittest.TestCase()
    ok=False
    # TODO
    assert ok

@check
def ex57_patch_object():
    """patch.object 临时替换类方法。"""
    from unittest.mock import patch
    class API:
        def ping(self): return "real"
    result=None
    # TODO
    assert result=="fake"
    assert API().ping()=="real"

@check
def ex58_reset_mock():
    """reset_mock 清除调用历史但默认保留 return_value。"""
    from unittest.mock import Mock
    m=Mock(return_value=3)
    m(1)
    # TODO
    assert m.call_count==0
    assert m()==3
    assert m.call_count==1

@check
def ex59_factory_fixture():
    """用小型工厂函数创建测试数据，减少重复同时保持清晰。"""
    def make_user(name="Alice", active=True):
        # TODO
        return None
    u1=make_user()
    u2=make_user(name="Bob", active=False)
    assert u1=={"name":"Alice","active":True}
    assert u2=={"name":"Bob","active":False}

@check
def ex60_contract_test_shape():
    """对两个实现运行同一组契约测试。"""
    class MemoryStore:
        def __init__(self): self.d={}
        def put(self,k,v): self.d[k]=v
        def get(self,k): return self.d[k]
    class OtherStore:
        def __init__(self): self.d={}
        def put(self,k,v): pass  # TODO
        def get(self,k): return None  # TODO
    def contract(store):
        store.put("x",1)
        assert store.get("x")==1
    for cls in (MemoryStore, OtherStore):
        contract(cls())

def run_all():
    print("=" * 72)
    print("08_testing_study 自动判分练习册")
    print("=" * 72)
    passed = 0
    failed = 0
    errors = 0
    for fn in _CHECKS:
        try:
            fn()
        except AssertionError as e:
            failed += 1
            print(f"[FAIL] {fn.__name__:<34} {e or 'TODO/断言未通过'}")
        except Exception as e:
            errors += 1
            print(f"[ERR ] {fn.__name__:<34} {type(e).__name__}: {e}")
        else:
            passed += 1
            print(f"[ OK ] {fn.__name__}")
    print("-" * 72)
    print(f"通过 {passed}/{len(_CHECKS)} | FAIL={failed} | ERR={errors}")
    return passed, failed, errors

if __name__ == "__main__":
    run_all()

# ======================================================================
# 参考答案（全部以注释形式保存，不影响运行）
# ======================================================================
# 测试通常不只有一种正确写法；下面给出一种可运行参考实现。

# [01] ex01_boundary_cases
# def normalize_age(n):
#     if not isinstance(n, int):
#         raise TypeError
#     if not 0 <= n <= 150:
#         raise ValueError
#     return n
# cases = [(0, 0), (150, 150), (-1, ValueError), (151, ValueError)]
# assert cases == [(0, 0), (150, 150), (-1, ValueError), (151, ValueError)]

# [02] ex02_behavior_not_implementation
# def final_price(price, discount):
#     return round(price * (1 - discount), 2)
# result = final_price(100, 0.2)
# assert result == 80.0

# [03] ex03_build_testcase
# import unittest
# def add(a, b):
#     return a + b
# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         "implemented"
#         self.assertEqual(add(2, 3), 5)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
# result = unittest.TestResult()
# suite.run(result)
# assert result.testsRun == 1
# assert len(result.failures) == 0
# assert len(result.errors) == 0
# assert getattr(TestAdd.test_add, "__doc__", None) == "implemented"

# [04] ex04_loader_discovers_test
# import unittest
# class Demo(unittest.TestCase):
#     def test_value(self):
#         self.assertTrue(True)
# names = unittest.defaultTestLoader.getTestCaseNames(Demo)
# assert names == ["test_value"]

# [05] ex05_almost_equal
# import unittest
# case = unittest.TestCase()
# case.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
# ok = True
# assert ok is True

# [06] ex06_count_equal
# import unittest
# case = unittest.TestCase()
# case.assertCountEqual([1, 2, 2], [2, 1, 2])
# ok = True
# assert ok is True

# [07] ex07_fixture_fresh_each_time
# import unittest
# shared_seed = []
# seen = []
# class Demo(unittest.TestCase):
#     def setUp(self):
#         self.items = []
#     def test_a(self):
#         self.items.append(1)
#         seen.append(self.items)
#     def test_b(self):
#         self.items.append(2)
#         seen.append(self.items)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
# r = unittest.TestResult(); suite.run(r)
# assert not r.failures and not r.errors
# assert len(seen) == 2 and seen[0] is not seen[1]

# [08] ex08_add_cleanup
# import unittest
# events = []
# class Demo(unittest.TestCase):
#     def test_cleanup(self):
#         self.addCleanup(events.append, "cleanup")
#         events.append("body")
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
# r = unittest.TestResult(); suite.run(r)
# assert events == ["body", "cleanup"]

# [09] ex09_subtest_cases
# import unittest
# class Demo(unittest.TestCase):
#     def test_square(self):
#         cases = [(2, 4), (3, 9), (4, 16)]
#         checked = 0
#         for x, expected in cases:
#             with self.subTest(x=x):
#                 self.assertEqual(x*x, expected)
#                 checked += 1
#         self.assertEqual(checked, 3)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
# r = unittest.TestResult(); suite.run(r)
# assert not r.failures and not r.errors

# [10] ex10_meaningful_test_name
# import unittest
# class Demo(unittest.TestCase):
#     def test_expired_token_is_rejected(self):
#         pass
# names = unittest.defaultTestLoader.getTestCaseNames(Demo)
# assert names == ["test_expired_token_is_rejected"]

# [11] ex11_assert_raises_regex
# import unittest
# def parse_age(s):
#     n = int(s)
#     if n < 0:
#         raise ValueError("age must be >= 0")
#     return n
# case = unittest.TestCase()
# with case.assertRaisesRegex(ValueError, ">= 0"):
#     parse_age("-1")
# ok = True
# assert ok is True

# [12] ex12_assert_logs
# import logging, unittest
# logger = logging.getLogger("course.test")
# case = unittest.TestCase()
# with case.assertLogs("course.test", level="INFO") as captured:
#     logger.info("started")
# assert captured is not None
# assert any("started" in line for line in captured.output)

# [13] ex13_mock_return_value
# from unittest.mock import Mock
# client = Mock()
# client.fetch.return_value = {"name": "Alice"}
# result = client.fetch("u1")
# assert result == {"name": "Alice"}
# client.fetch.assert_called_once_with("u1")

# [14] ex14_mock_call_count
# from unittest.mock import Mock
# m = Mock()
# m(1)
# m(2)
# assert m.call_count == 2
# assert m.call_args_list[0].args == (1,)
# assert m.call_args_list[1].args == (2,)

# [15] ex15_patch_where_used
# import types, sys, textwrap
# from unittest.mock import patch
# src = types.ModuleType("_ex15_src"); src.rate=lambda:0.1; sys.modules["_ex15_src"]=src
# consumer = types.ModuleType("_ex15_consumer")
# exec(textwrap.dedent("""
# from _ex15_src import rate
# 
# def price(x):
#     return x*(1+rate())
# """), consumer.__dict__)
# sys.modules["_ex15_consumer"]=consumer
# with patch("_ex15_consumer.rate", return_value=0.2):
#     result = consumer.price(100)
# assert result == 120

# [16] ex16_patch_restores
# from unittest.mock import patch
# import os
# before = os.getcwd
# with patch("os.getcwd", return_value="/fake"):
#     inside_changed = (os.getcwd() == "/fake")
# after_restored = (os.getcwd is before)
# assert inside_changed and after_restored

# [17] ex17_spec_set_blocks_unknown
# from unittest.mock import Mock
# class API:
#     def send(self): pass
# m = Mock(spec_set=API)
# blocked = False
# try:
#     m.no_such_attr
# except AttributeError:
#     blocked = True
# assert blocked

# [18] ex18_autospec_signature
# from unittest.mock import create_autospec
# class API:
#     def send(self, user, amount, *, currency="CNY"): pass
# m = create_autospec(API, instance=True)
# blocked = False
# try:
#     m.send("u1")
# except TypeError:
#     blocked = True
# assert blocked

# [19] ex19_side_effect_sequence
# from unittest.mock import Mock
# m = Mock(side_effect=[TimeoutError("slow"), "ok"])
# first_timeout = False
# try:
#     m()
# except TimeoutError:
#     first_timeout = True
# second = m()
# assert first_timeout and second == "ok"

# [20] ex20_assert_has_calls
# from unittest.mock import Mock, call
# m = Mock()
# m("a"); m("b")
# m.assert_has_calls([call("a"), call("b")])
# ok = True
# assert ok

# [21] ex21_magicmock_context_manager
# from unittest.mock import MagicMock
# m = MagicMock()
# m.__enter__.return_value = "resource"
# with m as value:
#     result = value
# assert result == "resource"
# m.__enter__.assert_called_once()
# m.__exit__.assert_called_once()

# [22] ex22_propertymock
# from unittest.mock import PropertyMock, patch
# class User:
#     @property
#     def name(self):
#         return "real"
# with patch.object(User, "name", new_callable=PropertyMock) as p:
#     p.return_value = "mocked"
#     result = User().name
# assert result == "mocked"

# [23] ex23_mock_open
# from unittest.mock import mock_open, patch
# def load_first(path):
#     with open(path, "r", encoding="utf-8") as f:
#         return f.readline().strip()
# m = mock_open(read_data="hello\nworld\n")
# with patch("builtins.open", m):
#     result = load_first("fake.txt")
# m.assert_called_once_with("fake.txt", "r", encoding="utf-8")
# assert result == "hello"

# [24] ex24_temp_directory
# import tempfile
# from pathlib import Path
# with tempfile.TemporaryDirectory() as tmp:
#     p = Path(tmp) / "x.txt"
#     p.write_text("你好", encoding="utf-8")
#     ok = p.read_text(encoding="utf-8") == "你好"
# assert ok

# [25] ex25_fake_clock
# def expired(deadline, clock):
#     return clock.now() >= deadline
# class FakeClock:
#     def __init__(self, now): self.value = now
#     def now(self): return self.value
# clock = FakeClock(100)
# assert expired(90, clock) is True
# assert expired(110, clock) is False

# [26] ex26_fake_sender
# class FakeSender:
#     def __init__(self):
#         self.messages = []
#     def send(self, user, message):
#         self.messages.append((user, message))
# def welcome(sender, user):
#     sender.send(user, "welcome")
# sender = FakeSender()
# welcome(sender, "alice")
# assert sender.messages == [("alice", "welcome")]

# [27] ex27_patch_dict_env
# import os
# from unittest.mock import patch
# before = os.environ.get("_COURSE_MODE")
# with patch.dict(os.environ, {"_COURSE_MODE": "test"}):
#     inside = os.environ["_COURSE_MODE"]
# after = os.environ.get("_COURSE_MODE")
# assert inside == "test"
# assert after == before

# [28] ex28_seeded_random
# import random
# r1 = random.Random(123)
# r2 = random.Random(123)
# a = [r1.randint(1, 9) for _ in range(5)]
# b = [r2.randint(1, 9) for _ in range(5)]
# assert a == b
# assert a == [1, 5, 2, 7, 5]

# [29] ex29_asyncmock
# import asyncio
# from unittest.mock import AsyncMock
# async def run():
#     client = AsyncMock()
#     client.fetch.return_value = {"id": 1}
#     result = await client.fetch(1)
#     client.fetch.assert_awaited_once_with(1)
#     return result
# result = asyncio.run(run())
# assert result == {"id": 1}

# [30] ex30_async_timeout
# import asyncio
# async def slow():
#     await asyncio.sleep(0.05)
# async def run():
#     timed_out = False
#     try:
#         async with asyncio.timeout(0.001):
#             await slow()
#     except TimeoutError:
#         timed_out = True
#     return timed_out
# assert asyncio.run(run()) is True

# [31] ex31_async_cancel_cleanup
# import asyncio
# async def run():
#     cleaned = asyncio.Event()
#     async def worker():
#         try:
#             await asyncio.sleep(10)
#         finally:
#             cleaned.set()
#     task = asyncio.create_task(worker())
#     await asyncio.sleep(0)
#     task.cancel()
#     try:
#         await task
#     except asyncio.CancelledError:
#         pass
#     return cleaned.is_set(), task.cancelled()
# assert asyncio.run(run()) == (True, True)

# [32] ex32_isolated_asyncio_testcase
# import unittest, asyncio
# class Demo(unittest.IsolatedAsyncioTestCase):
#     async def test_value(self):
#         "implemented"
#         await asyncio.sleep(0)
#         self.assertEqual(2 + 3, 5)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
# r = unittest.TestResult(); suite.run(r)
# assert not r.failures and not r.errors
# assert getattr(Demo.test_value, "__doc__", None) == "implemented"

# [33] ex33_subprocess_capture
# import subprocess, sys
# proc = subprocess.run(
#     [sys.executable, "-c", "print('hello'.upper())"],
#     capture_output=True, text=True, encoding="utf-8"
# )
# assert proc is not None
# assert proc.returncode == 0
# assert proc.stdout.strip() == "HELLO"

# [34] ex34_exit_code
# import subprocess, sys
# proc = subprocess.run(
#     [sys.executable, "-c", "import sys; sys.exit(3)"],
#     capture_output=True
# )
# assert proc is not None and proc.returncode == 3

# [35] ex35_ephemeral_port
# from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
# class H(BaseHTTPRequestHandler):
#     def log_message(self, *args): pass
# server = ThreadingHTTPServer(("127.0.0.1", 0), H)
# assert server is not None
# port = server.server_address[1]
# try:
#     assert port > 0
# finally:
#     server.server_close()

# [36] ex36_local_http_roundtrip
# from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
# from threading import Thread
# from urllib.request import urlopen
# class H(BaseHTTPRequestHandler):
#     def do_GET(self):
#         data=b"OK"; self.send_response(200); self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
#     def log_message(self, *args): pass
# server=ThreadingHTTPServer(("127.0.0.1",0),H)
# thread=Thread(target=server.serve_forever,daemon=True); thread.start()
# try:
#     host,port=server.server_address
#     with urlopen(f"http://{host}:{port}/", timeout=2) as r:
#         body=r.read().decode()
# finally:
#     server.shutdown(); server.server_close(); thread.join(timeout=2)
# assert body == "OK"

# [37] ex37_sqlite_memory
# import sqlite3
# conn = sqlite3.connect(":memory:")
# assert conn is not None
# try:
#     conn.execute("create table t(x integer)")
#     conn.execute("insert into t values (1)")
#     assert conn.execute("select x from t").fetchone()[0] == 1
# finally:
#     conn.close()

# [38] ex38_sqlite_parameterized
# import sqlite3
# conn=sqlite3.connect(":memory:")
# try:
#     conn.execute("create table users(name text)")
#     name="O'Reilly"
#     conn.execute("insert into users(name) values (?)", (name,))
#     row=conn.execute("select name from users").fetchone()
#     assert row == (name,)
# finally:
#     conn.close()

# [39] ex39_thread_join_timeout
# import threading
# done=[]
# def worker(): done.append(1)
# t=threading.Thread(target=worker)
# t.start()
# t.join(timeout=1)
# assert done == [1] and not t.is_alive()

# [40] ex40_event_instead_of_sleep
# import threading
# ready=threading.Event()
# def worker():
#     ready.set()
# t=threading.Thread(target=worker); t.start()
# observed = ready.wait(timeout=1)
# t.join(timeout=1)
# assert observed and not t.is_alive()

# [41] ex41_restore_global_state
# state={"mode":"prod"}
# before=state.copy()
# try:
#     state["mode"]="test"
#     inside=state["mode"]
# finally:
#     state.clear(); state.update(before)
# assert inside=="test"
# assert state==before

# [42] ex42_independent_tests
# import unittest
# class Demo(unittest.TestCase):
#     shared=[]
#     def setUp(self):
#         self.shared = []
#     def test_a(self):
#         self.shared.append(1)
#     def test_b(self):
#         self.assertEqual(self.shared, [])
# suite=unittest.TestSuite([Demo("test_a"), Demo("test_b")])
# r=unittest.TestResult(); suite.run(r)
# assert not r.failures and not r.errors

# [43] ex43_deterministic_uuid
# def create_user(name, id_factory):
#     return {"id": id_factory(), "name": name}
# result = create_user("Alice", lambda: "fixed-id")
# assert result == {"id": "fixed-id", "name": "Alice"}

# [44] ex44_bounded_wait
# import threading
# evt=threading.Event()
# result = evt.wait(timeout=0.001)
# assert result is False

# [45] ex45_skip_decorator
# import unittest
# class Demo(unittest.TestCase):
#     @unittest.skip("not ready")
#     def test_future(self):
#         self.fail("not ready")
# suite=unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
# r=unittest.TestResult(); suite.run(r)
# assert len(r.skipped)==1 and not r.failures

# [46] ex46_expected_failure
# import unittest
# class Demo(unittest.TestCase):
#     @unittest.expectedFailure
#     def test_bug(self):
#         self.assertEqual(1,2)
# suite=unittest.defaultTestLoader.loadTestsFromTestCase(Demo)
# r=unittest.TestResult(); suite.run(r)
# assert len(r.expectedFailures)==1

# [47] ex47_doctest_example
# import doctest, types, textwrap
# m=types.ModuleType("_ex47")
# m.__dict__["__name__"]="_ex47"
# exec(textwrap.dedent("""
# def double(x):
#     return x*2
# """), m.__dict__)
# m.double.__doc__ = """
# >>> double(3)
# 6
# """
# failures, tests = doctest.testmod(m, verbose=False)
# assert failures==0 and tests==1

# [48] ex48_doctest_ellipsis
# import doctest
# flags = doctest.ELLIPSIS
# checker=doctest.OutputChecker()
# ok=checker.check_output("value=<...>", "value=<object at 0x1234>", flags)
# assert ok

# [49] ex49_assert_not_just_execute
# def classify(x):
#     return "positive" if x > 0 else "non-positive"
# assert classify(1) == "positive"
# checked = True
# assert checked

# [50] ex50_branch_cases
# def classify(x):
#     return "positive" if x > 0 else "non-positive"
# cases = [(1, classify(1)), (0, classify(0))]
# assert cases == [(1, "positive"), (0, "non-positive")]

# [51] ex51_aaa_structure
# def discount(price, rate):
#     return price*(1-rate)
# price=100; rate=0.2
# result=discount(price, rate)
# assert result==80
# done=True
# assert done

# [52] ex52_one_behavior_per_test
# def first(items):
#     if not items: return None
#     return items[0]
# result = first([])
# assert result is None

# [53] ex53_stub_vs_mock
# from unittest.mock import Mock
# gateway=Mock()
# gateway.charge.return_value=True
# paid=gateway.charge(100)
# assert paid is True
# gateway.charge.assert_called_once_with(100)

# [54] ex54_spy_wraps
# from unittest.mock import Mock
# def real(x): return x*2
# spy = Mock(wraps=real)
# result = spy(3)
# assert result == 6
# spy.assert_called_once_with(3)

# [55] ex55_assert_warns
# import warnings, unittest
# def old():
#     warnings.warn("deprecated", DeprecationWarning)
# case=unittest.TestCase()
# with case.assertWarns(DeprecationWarning):
#     old()
# ok=True
# assert ok

# [56] ex56_assert_no_logs
# import logging, unittest
# logger=logging.getLogger("_ex56")
# case=unittest.TestCase()
# with case.assertNoLogs("_ex56", level="WARNING"):
#     logger.info("fine")
# ok=True
# assert ok

# [57] ex57_patch_object
# from unittest.mock import patch
# class API:
#     def ping(self): return "real"
# with patch.object(API, "ping", return_value="fake"):
#     result=API().ping()
# assert result=="fake"
# assert API().ping()=="real"

# [58] ex58_reset_mock
# from unittest.mock import Mock
# m=Mock(return_value=3)
# m(1)
# m.reset_mock()
# assert m.call_count==0
# assert m()==3
# assert m.call_count==1

# [59] ex59_factory_fixture
# def make_user(name="Alice", active=True):
#     return {"name":name, "active":active}
# u1=make_user()
# u2=make_user(name="Bob", active=False)
# assert u1=={"name":"Alice","active":True}
# assert u2=={"name":"Bob","active":False}

# [60] ex60_contract_test_shape
# class MemoryStore:
#     def __init__(self): self.d={}
#     def put(self,k,v): self.d[k]=v
#     def get(self,k): return self.d[k]
# class OtherStore:
#     def __init__(self): self.d={}
#     def put(self,k,v): self.d[k]=v
#     def get(self,k): return self.d[k]
# def contract(store):
#     store.put("x",1)
#     assert store.get("x")==1
# for cls in (MemoryStore, OtherStore):
#     contract(cls())
