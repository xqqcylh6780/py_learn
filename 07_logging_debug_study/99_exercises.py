# -*- coding: utf-8 -*-
"""
logging + debugging 完整练习册 —— 52 题，自动判分
=================================================

运行：
    python 99_exercises.py

规则：
- 每题独立，补 TODO 后重复运行。
- 练习尽量检查“行为”而不是只检查某个字符串答案。
- 参考答案在文件最底部；建议先自己完成。
"""
from __future__ import annotations

import asyncio
import cProfile
import contextvars
import faulthandler
import inspect
import io
import logging
import logging.config
from logging.handlers import QueueHandler, QueueListener, RotatingFileHandler, SocketHandler
from pathlib import Path
from queue import Queue
import sys
import tempfile
import threading
import time
import timeit
import traceback
import tracemalloc
import warnings

_checks = []

def check(fn):
    _checks.append(fn)
    return fn


def fresh_logger(name: str) -> logging.Logger:
    """创建不会向 root 传播、不会继承旧 handler 的练习 logger。"""
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.filters.clear()
    logger.propagate = False
    logger.setLevel(logging.NOTSET)
    return logger

# 01 为什么用 logging
@check
def ex01_named_logger():
    """获取名为 course.worker 的 Logger。"""
    logger = None  # TODO
    assert isinstance(logger, logging.Logger)
    assert logger.name == "course.worker"

@check
def ex02_lazy_logging_arguments():
    """使用 logging 的参数化格式，而不是先做字符串插值。"""
    class Expensive:
        def __init__(self): self.calls = 0
        def __str__(self):
            self.calls += 1
            return "EXP"
    obj = Expensive()
    calls = []
    class FakeLogger:
        def debug(self, *args):
            calls.append(args)
    logger = FakeLogger()
    # TODO：用 logger.debug("value=%s", obj) 记录；不要 f-string / % 预格式化
    pass
    assert len(calls) == 1
    assert calls[0][0] == "value=%s" and calls[0][1] is obj
    assert obj.calls == 0, "参数化调用本身不应先把 obj 转成字符串"

# 02 级别
@check
def ex03_level_number():
    result = None  # TODO：logging.ERROR 的数值
    assert result == 40

@check
def ex04_effective_level():
    parent = fresh_logger("ex04")
    parent.setLevel(logging.WARNING)
    child = logging.getLogger("ex04.child")
    child.handlers.clear(); child.setLevel(logging.NOTSET); child.propagate = True
    result = None  # TODO：读取 child 的有效级别
    assert result == logging.WARNING

# 03 层级/传播
@check
def ex05_parent_logger_name():
    logger = logging.getLogger("app.db.query")
    result = None  # TODO：这个名字的直接父 logger 名称（确保先创建 app.db）
    # 提示：logging.getLogger("app.db")
    assert result == "app.db"

@check
def ex06_stop_propagation():
    logger = fresh_logger("ex06.child")
    logger.propagate = True
    # TODO：阻止记录继续传播给祖先
    pass
    assert logger.propagate is False

# 04 Handler
@check
def ex07_stream_handler():
    stream = io.StringIO()
    logger = fresh_logger("ex07")
    logger.setLevel(logging.INFO)
    # TODO：创建 StreamHandler(stream) 并加到 logger
    logger.info("hello")
    assert "hello" in stream.getvalue()

@check
def ex08_handler_level():
    stream = io.StringIO()
    logger = fresh_logger("ex08")
    logger.setLevel(logging.DEBUG)
    h = logging.StreamHandler(stream)
    # TODO：让 handler 只接收 WARNING 及以上
    logger.addHandler(h)
    logger.info("info")
    logger.warning("warn")
    assert "warn" in stream.getvalue()
    assert "info" not in stream.getvalue()

# 05 Formatter / LogRecord
@check
def ex09_formatter_fields():
    stream = io.StringIO()
    logger = fresh_logger("ex09")
    logger.setLevel(logging.INFO)
    h = logging.StreamHandler(stream)
    # TODO：格式必须包含 levelname、name、message
    formatter = None
    h.setFormatter(formatter)
    logger.addHandler(h)
    logger.info("hello")
    out = stream.getvalue()
    assert "INFO" in out and "ex09" in out and "hello" in out

@check
def ex10_logrecord_lineno():
    record = logging.LogRecord("x", logging.INFO, __file__, 123, "hi", (), None)
    result = None  # TODO：读取记录的行号
    assert result == 123

# 06 basicConfig / 配置意识
@check
def ex11_root_has_handlers():
    root = logging.getLogger()
    result = None  # TODO：返回 root.handlers 的副本列表
    assert isinstance(result, list)
    assert result is not root.handlers

@check
def ex12_force_semantics():
    # 知识题：basicConfig(force=True) 的核心作用是什么？
    result = None  # TODO：填字符串 "replace"
    assert result == "replace"

# 07 文件日志
@check
def ex13_utf8_file_handler():
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "x.log"
        logger = fresh_logger("ex13")
        logger.setLevel(logging.INFO)
        # TODO：创建 encoding='utf-8' 的 FileHandler(path)
        h = None
        assert isinstance(h, logging.FileHandler)
        logger.addHandler(h)
        logger.info("中文")
        h.close()
        assert path.read_text(encoding="utf-8").strip() == "中文"

@check
def ex14_remove_and_close_handler():
    logger = fresh_logger("ex14")
    h = logging.StreamHandler(io.StringIO())
    logger.addHandler(h)
    # TODO：从 logger 移除 h，并关闭它
    pass
    assert h not in logger.handlers
    assert h._closed is True

# 08 轮转
@check
def ex15_rotating_handler_type():
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "app.log"
        # TODO：maxBytes=100, backupCount=2
        h = None
        assert isinstance(h, RotatingFileHandler)
        assert h.maxBytes == 100 and h.backupCount == 2
        h.close()

@check
def ex16_rotation_backup_count():
    # 轮转日志希望最多保留 5 个历史备份。
    backup_count = None  # TODO
    assert backup_count == 5

# 09 异常日志
@check
def ex17_exception_traceback_logging():
    stream = io.StringIO()
    logger = fresh_logger("ex17")
    logger.setLevel(logging.ERROR)
    h = logging.StreamHandler(stream); logger.addHandler(h)
    try:
        1 / 0
    except ZeroDivisionError:
        # TODO：记录 "boom" 并附带当前异常 traceback
        pass
    out = stream.getvalue()
    assert "boom" in out and "ZeroDivisionError" in out

@check
def ex18_stacklevel_argument():
    captured = {}
    class Capture(logging.Handler):
        def emit(self, record):
            captured["func"] = record.funcName
    logger = fresh_logger("ex18"); logger.setLevel(logging.WARNING); logger.addHandler(Capture())
    def helper():
        # TODO：让 LogRecord 来源指向调用 helper 的 caller，而不是 helper
        pass
    def caller(): helper()
    caller()
    assert captured.get("func") == "caller"

# 10 extra / LoggerAdapter
@check
def ex19_extra_context():
    stream = io.StringIO()
    logger = fresh_logger("ex19"); logger.setLevel(logging.INFO)
    h = logging.StreamHandler(stream)
    h.setFormatter(logging.Formatter("%(request_id)s %(message)s")); logger.addHandler(h)
    # TODO：用 extra 传 request_id="r1"
    pass
    assert stream.getvalue().strip() == "r1 hello"

@check
def ex20_logger_adapter():
    logger = fresh_logger("ex20")
    # TODO：创建带 {"request_id":"r2"} 的 LoggerAdapter
    adapter = None
    assert isinstance(adapter, logging.LoggerAdapter)
    assert adapter.extra["request_id"] == "r2"

# 11 Filter
@check
def ex21_filter_drop():
    class DropSecret(logging.Filter):
        def filter(self, record):
            # TODO：消息包含 SECRET 时返回 False
            return True
    f = DropSecret()
    ok = logging.LogRecord("x", logging.INFO, __file__, 1, "hello", (), None)
    bad = logging.LogRecord("x", logging.INFO, __file__, 1, "SECRET token", (), None)
    assert f.filter(ok) is True
    assert f.filter(bad) is False

@check
def ex22_filter_inject():
    class ContextFilter(logging.Filter):
        def filter(self, record):
            # TODO：注入 record.request_id = "abc"
            return True
    record = logging.LogRecord("x", logging.INFO, __file__, 1, "m", (), None)
    assert ContextFilter().filter(record) is True
    assert hasattr(record, "request_id")
    assert record.request_id == "abc"

# 12 QueueHandler/QueueListener
@check
def ex23_queue_handler():
    q = Queue()
    # TODO
    h = None
    assert isinstance(h, QueueHandler)
    assert h.queue is q

@check
def ex24_queue_listener():
    q = Queue(); sink = logging.StreamHandler(io.StringIO())
    # TODO：创建 QueueListener(q, sink)
    listener = None
    assert isinstance(listener, QueueListener)
    assert sink in listener.handlers

# 13 dictConfig
@check
def ex25_dictconfig_version():
    config = {
        # TODO：dictConfig 必需的版本
    }
    assert config.get("version") == 1

@check
def ex26_dictconfig_existing_loggers():
    config = {"version": 1}
    # TODO：不要禁用已有 logger
    assert config.get("disable_existing_loggers") is False

# 14 库日志
@check
def ex27_library_logger_name():
    # 在真实模块里推荐 logging.getLogger(__name__)
    logger = None  # TODO
    assert isinstance(logger, logging.Logger)
    assert logger.name == __name__

@check
def ex28_null_handler():
    logger = fresh_logger("ex28")
    # TODO：添加 NullHandler
    assert any(isinstance(h, logging.NullHandler) for h in logger.handlers)

# 15 warnings
@check
def ex29_capture_warning():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        # TODO：发出 UserWarning("careful")
        pass
    assert len(caught) == 1
    assert issubclass(caught[0].category, UserWarning)
    assert str(caught[0].message) == "careful"

@check
def ex30_warning_as_error():
    raised = False
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", RuntimeWarning)
            # TODO：发出 RuntimeWarning("bad")
            pass
    except RuntimeWarning:
        raised = True
    assert raised is True

# 16 traceback
@check
def ex31_format_exc_contains_type():
    result = None
    try:
        {}["missing"]
    except KeyError:
        # TODO：用 traceback.format_exc()
        pass
    assert isinstance(result, str)
    assert "KeyError" in result and "missing" in result

@check
def ex32_traceback_exception():
    try:
        int("x")
    except ValueError as exc:
        # TODO
        tb_exc = None
    assert isinstance(tb_exc, traceback.TracebackException)

# 17 hooks
@check
def ex33_save_restore_excepthook():
    old = sys.excepthook
    def custom(t, v, tb): pass
    during = None
    # TODO：先 sys.excepthook = custom，把 during 设为当前 hook，再恢复 old
    pass
    assert during is custom
    assert sys.excepthook is old

@check
def ex34_threading_excepthook_exists():
    result = None  # TODO：读取 threading.excepthook
    assert callable(result)

# 18 pdb / breakpoint
@check
def ex35_breakpoint_callable():
    import builtins
    result = None  # TODO：取 builtins.breakpoint
    assert callable(result)

@check
def ex36_post_mortem_function():
    import pdb
    result = None  # TODO：取 pdb.post_mortem
    assert callable(result)

# 19 inspect
@check
def ex37_signature():
    def f(a, *, b=2): pass
    sig = None  # TODO
    assert str(sig) == "(a, *, b=2)"

@check
def ex38_current_function_name():
    def inner():
        frame = inspect.currentframe()
        try:
            # TODO：通过 frame 取当前函数名
            result = None
            return result
        finally:
            del frame
    assert inner() == "inner"

# 20 faulthandler
@check
def ex39_enable_faulthandler():
    was = faulthandler.is_enabled()
    called = False
    def enable_for_test():
        nonlocal called
        called = True
        faulthandler.enable()
    try:
        # TODO：调用 enable_for_test()
        pass
        assert called is True
        assert faulthandler.is_enabled() is True
    finally:
        if not was:
            faulthandler.disable()

@check
def ex40_faulthandler_api():
    result = None  # TODO：取 faulthandler.dump_traceback_later
    assert callable(result)

# 21 timing
@check
def ex41_perf_counter_measure():
    # TODO：用 perf_counter 获取两个时间点
    start = end = None
    assert isinstance(start, float) and isinstance(end, float)
    assert end >= start

@check
def ex42_timeit_result():
    # TODO：测量 sum(range(10)) 执行 10 次
    elapsed = None
    assert isinstance(elapsed, float) and elapsed >= 0

# 22 cProfile/pstats
@check
def ex43_profile_object():
    prof = None  # TODO
    assert isinstance(prof, cProfile.Profile)

@check
def ex44_profile_function():
    prof = cProfile.Profile()
    def work(): return sum(range(100))
    # TODO：用 prof.runcall(work) 执行并获取返回值
    result = None
    assert result == 4950
    stats = prof.getstats()
    assert stats

# 23 tracemalloc
@check
def ex45_tracemalloc_current_peak():
    tracemalloc.start()
    try:
        data = [str(i) for i in range(100)]
        # TODO：调用 get_traced_memory()
        result = None
        assert isinstance(result, tuple) and len(result) == 2
        assert result[1] >= result[0] >= 0
    finally:
        tracemalloc.stop()

@check
def ex46_snapshot_compare():
    tracemalloc.start()
    try:
        before = tracemalloc.take_snapshot()
        data = [bytearray(100) for _ in range(100)]
        after = tracemalloc.take_snapshot()
        # TODO：按 lineno 比较
        stats = None
        assert isinstance(stats, list)
        assert len(stats) > 0
    finally:
        tracemalloc.stop()

# 24 threading / asyncio
@check
def ex47_thread_excepthook_capture():
    seen = []
    old = threading.excepthook
    try:
        def hook(args):
            seen.append(args.exc_type)
        threading.excepthook = hook
        def boom():
            # TODO：在线程里抛 RuntimeError
            pass
        t = threading.Thread(target=boom)
        t.start(); t.join()
    finally:
        threading.excepthook = old
    assert seen == [RuntimeError]

@check
def ex48_await_task_exception():
    async def child():
        raise ValueError("bad")
    async def main():
        task = asyncio.create_task(child())
        caught = False
        try:
            # TODO：await task
            pass
        except ValueError:
            caught = True
        if not task.done():
            await asyncio.sleep(0)
        if task.done() and not caught:
            task.exception()  # 未完成 TODO 时也取走异常，避免未检索异常警告
        return caught
    assert asyncio.run(main()) is True

@check
def ex49_task_name():
    async def main():
        async def child(): return 1
        # TODO：创建 name="worker-1" 的 Task
        task = None
        assert isinstance(task, asyncio.Task)
        name = task.get_name()
        await task
        return name
    assert asyncio.run(main()) == "worker-1"

# 25 生产排错 / 安全日志
@check
def ex50_redact_secret():
    def redact(data):
        # TODO：返回新 dict，把 password/token 对应值替换为 "***"
        return None
    source = {"user": "a", "password": "p", "token": "t"}
    result = redact(source)
    assert result == {"user": "a", "password": "***", "token": "***"}
    assert source["password"] == "p", "不要原地修改输入"

@check
def ex51_avoid_duplicate_handler():
    logger = fresh_logger("ex51")
    def configure():
        # TODO：仅在没有 StreamHandler 时添加一个
        pass
    configure(); configure()
    assert sum(type(h) is logging.StreamHandler for h in logger.handlers) == 1

@check
def ex52_choose_debug_tool():
    """把症状映射到最适合的标准库诊断工具。"""
    tools = {
        "cpu_hot": None,       # TODO: "cProfile"
        "memory_growth": None, # TODO: "tracemalloc"
        "hang": None,          # TODO: "faulthandler"
        "step_code": None,     # TODO: "pdb"
    }
    assert tools == {
        "cpu_hot": "cProfile",
        "memory_growth": "tracemalloc",
        "hang": "faulthandler",
        "step_code": "pdb",
    }



# 26 ContextVar / LogRecordFactory
@check
def ex53_contextvar_set_reset():
    var = contextvars.ContextVar("ex53", default="-")
    token = None
    # TODO：set("req-1") 并保存返回 token
    assert isinstance(token, contextvars.Token)
    assert var.get() == "req-1"
    # TODO：用 token 恢复旧值
    assert var.get() == "-"

@check
def ex54_logrecord_factory_inject():
    old = logging.getLogRecordFactory()
    try:
        def factory(*args, **kwargs):
            record = old(*args, **kwargs)
            # TODO：record.request_id = "r54"
            return record
        logging.setLogRecordFactory(factory)
        record = logging.getLogger("ex54").makeRecord("ex54", logging.INFO, __file__, 1, "m", (), None)
        assert hasattr(record, "request_id")
        assert record.request_id == "r54"
    finally:
        logging.setLogRecordFactory(old)

# 27 sys.settrace
@check
def ex55_trace_receives_events():
    events = []
    def tracer(frame, event, arg):
        if frame.f_code.co_name == "target":
            events.append(event)
        return tracer
    def target():
        x = 1
        return x
    old = sys.gettrace()
    try:
        # TODO：安装 tracer
        target()
    finally:
        sys.settrace(old)
    assert "call" in events and "return" in events

@check
def ex56_restore_trace_function():
    old = sys.gettrace()
    def tracer(frame, event, arg): return tracer
    during = None
    try:
        # TODO：安装 tracer，并把 during = sys.gettrace()
        pass
    finally:
        sys.settrace(old)
    assert during is tracer
    assert sys.gettrace() is old

# 28 多进程/网络日志安全
@check
def ex57_socket_handler():
    # 只构造，不 emit，不会真正连接。
    h = None  # TODO：SocketHandler("localhost", 9999)
    assert isinstance(h, SocketHandler)
    h.close()

@check
def ex58_network_logging_security():
    answer = None  # TODO：填 "untrusted_pickle_is_unsafe"
    assert answer == "untrusted_pickle_is_unsafe"


def run_all():
    print("=" * 72)
    print("07_logging_debug_study 练习册")
    print("=" * 72)
    passed = 0
    for fn in _checks:
        try:
            fn()
        except AssertionError as e:
            print(f"[FAIL] {fn.__name__:<34} {e or '断言未通过'}")
        except Exception as e:
            print(f"[ERR ] {fn.__name__:<34} {type(e).__name__}: {e}")
        else:
            passed += 1
            print(f"[ OK ] {fn.__name__:<34}")
    print("-" * 72)
    print(f"通过 {passed}/{len(_checks)}")
    if passed == len(_checks):
        print("日志与调试课程通关。")

if __name__ == "__main__":
    run_all()

# ============================================================================
# 参考答案（建议做完再看）
# ============================================================================
"""
ex01
    logger = logging.getLogger("course.worker")

ex02
    logger.debug("value=%s", obj)

ex03
    result = logging.ERROR

ex04
    result = child.getEffectiveLevel()

ex05
    logging.getLogger("app.db")
    result = logger.parent.name

ex06
    logger.propagate = False

ex07
    h = logging.StreamHandler(stream)
    logger.addHandler(h)

ex08
    h.setLevel(logging.WARNING)

ex09
    formatter = logging.Formatter("%(levelname)s %(name)s %(message)s")

ex10
    result = record.lineno

ex11
    result = list(root.handlers)

ex12
    result = "replace"

ex13
    h = logging.FileHandler(path, encoding="utf-8")

ex14
    logger.removeHandler(h)
    h.close()

ex15
    h = RotatingFileHandler(path, maxBytes=100, backupCount=2)

ex16
    backup_count = 5

ex17
    logger.exception("boom")

ex18
    logger.warning("from caller", stacklevel=2)

ex19
    logger.info("hello", extra={"request_id": "r1"})

ex20
    adapter = logging.LoggerAdapter(logger, {"request_id": "r2"})

ex21
    return "SECRET" not in record.getMessage()

ex22
    record.request_id = "abc"
    return True

ex23
    h = QueueHandler(q)

ex24
    listener = QueueListener(q, sink)

ex25
    config = {"version": 1}

ex26
    config["disable_existing_loggers"] = False

ex27
    logger = logging.getLogger(__name__)

ex28
    logger.addHandler(logging.NullHandler())

ex29
    warnings.warn("careful", UserWarning)

ex30
    warnings.warn("bad", RuntimeWarning)

ex31
    result = traceback.format_exc()

ex32
    tb_exc = traceback.TracebackException.from_exception(exc)

ex33
    sys.excepthook = custom
    during = sys.excepthook
    sys.excepthook = old

ex34
    result = threading.excepthook

ex35
    result = builtins.breakpoint

ex36
    result = pdb.post_mortem

ex37
    sig = inspect.signature(f)

ex38
    result = frame.f_code.co_name

ex39
    enable_for_test()

ex40
    result = faulthandler.dump_traceback_later

ex41
    start = time.perf_counter()
    end = time.perf_counter()

ex42
    elapsed = timeit.timeit("sum(range(10))", number=10)

ex43
    prof = cProfile.Profile()

ex44
    result = prof.runcall(work)

ex45
    result = tracemalloc.get_traced_memory()

ex46
    stats = after.compare_to(before, "lineno")

ex47
    raise RuntimeError("boom")

ex48
    await task

ex49
    task = asyncio.create_task(child(), name="worker-1")

ex50
    result = dict(data)
    for key in ("password", "token"):
        if key in result:
            result[key] = "***"
    return result

ex51
    if not any(type(h) is logging.StreamHandler for h in logger.handlers):
        logger.addHandler(logging.StreamHandler(io.StringIO()))

ex52
    tools = {
        "cpu_hot": "cProfile",
        "memory_growth": "tracemalloc",
        "hang": "faulthandler",
        "step_code": "pdb",
    }

ex53
    token = var.set("req-1")
    assert var.get() == "req-1"
    var.reset(token)

ex54
    record.request_id = "r54"

ex55
    sys.settrace(tracer)

ex56
    sys.settrace(tracer)
    during = sys.gettrace()

ex57
    h = SocketHandler("localhost", 9999)

ex58
    answer = "untrusted_pickle_is_unsafe"
"""
