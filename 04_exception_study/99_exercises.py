# -*- coding: utf-8 -*-
"""
04_exception_study 练习册 —— 44 题自动判分
========================================

运行：
    python 99_exercises.py

规则：
- 把 TODO 补完
- 每题独立判分
- 参考答案在文件最底部
"""

import asyncio
import contextlib
import io
import logging
import warnings

_CHECKS = []


def check(fn):
    _CHECKS.append(fn)
    return fn


@check
def ex01_catch_value_error():
    """把非法 int 转换变成 None。"""
    def parse(text):
        # TODO
        return int(text)
    assert parse("12") == 12
    assert parse("x") is None


@check
def ex02_exception_object():
    """捕获异常并返回异常类型名。"""
    def kind():
        try:
            1 / 0
        except ZeroDivisionError as exc:
            result = None  # TODO
            return result
    assert kind() == "ZeroDivisionError"


@check
def ex03_exception_hierarchy():
    """判断 FileNotFoundError 是否属于 OSError 家族。"""
    result = None  # TODO
    assert result is True


@check
def ex04_do_not_catch_baseexception():
    """填入通常业务异常应该继承的基类。"""
    Base = object  # TODO
    class AppError(Base):
        pass
    assert issubclass(AppError, Exception)
    assert not issubclass(AppError, KeyboardInterrupt)


@check
def ex05_multiple_exceptions():
    def parse(text):
        try:
            return int(text)
        # TODO：同时捕获 ValueError / TypeError
        except ():  # 替换这里
            return None
    assert parse("x") is None
    assert parse(None) is None


@check
def ex06_small_try_block():
    """只捕获 int() 的 ValueError，合法输入正常翻倍。"""
    def f(text):
        # TODO
        return None
    assert f("21") == 42
    assert f("bad") is None


@check
def ex07_else_branch():
    events = []
    try:
        n = int("7")
    except ValueError:
        events.append("error")
    else:
        # TODO
        pass
    assert events == ["success:7"]


@check
def ex08_finally_runs():
    events = []
    def f():
        try:
            events.append("try")
            return 1
        finally:
            # TODO
            pass
    assert f() == 1
    assert events == ["try", "cleanup"]


@check
def ex09_raise_validation_error():
    def age(value):
        # TODO：负数时抛 ValueError
        return value
    assert age(10) == 10
    try:
        age(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("age(-1) 应抛 ValueError")


@check
def ex10_reraise_same_exception():
    original = None
    caught = None
    try:
        try:
            exc = ValueError("x")
            original = exc
            raise exc
        except ValueError:
            # TODO：原样继续抛出
            pass
    except ValueError as exc:
        caught = exc
    assert caught is original


@check
def ex11_raise_from():
    class ConfigError(Exception):
        pass
    try:
        try:
            int("bad")
        except ValueError as exc:
            # TODO：抛 ConfigError，并显式保留 exc 为 cause
            raise ConfigError("bad config")
    except ConfigError as exc:
        assert isinstance(exc.__cause__, ValueError)


@check
def ex12_from_none():
    def lookup(d, key):
        try:
            return d[key]
        except KeyError:
            # TODO：隐藏上下文展示
            raise ValueError("missing")
    try:
        lookup({}, "x")
    except ValueError as exc:
        assert exc.__suppress_context__ is True


@check
def ex13_custom_base_exception():
    # TODO：让 ValidationError 继承 AppError
    class AppError(Exception):
        pass
    class ValidationError(Exception):
        pass
    assert issubclass(ValidationError, AppError)


@check
def ex14_exception_fields():
    class FieldError(Exception):
        def __init__(self, field, value):
            # TODO：保存两个字段，并初始化基类 message
            pass
    exc = FieldError("age", -1)
    assert exc.field == "age"
    assert exc.value == -1
    assert "age" in str(exc)


@check
def ex15_translate_layer_exception():
    class RepoError(Exception):
        pass
    class ServiceError(Exception):
        pass
    def repo():
        raise RepoError("db down")
    def service():
        try:
            repo()
        except RepoError as exc:
            # TODO
            raise
    try:
        service()
    except ServiceError as exc:
        assert isinstance(exc.__cause__, RepoError)
    else:
        raise AssertionError("应抛 ServiceError")


@check
def ex16_recovery_boundary():
    def cache_get(key):
        raise KeyError(key)
    def load(key):
        try:
            return cache_get(key)
        except KeyError:
            # TODO：缓存 miss 时回退到“database”
            return None
    assert load("x") == "database"


@check
def ex17_contextmanager_cleanup():
    events = []
    @contextlib.contextmanager
    def resource():
        events.append("open")
        try:
            yield
        finally:
            # TODO
            pass
    try:
        with resource():
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    assert events == ["open", "close"]


@check
def ex18_do_not_suppress_unintentionally():
    @contextlib.contextmanager
    def manager():
        try:
            yield
        except ValueError:
            # TODO：不要吞掉，继续传播
            pass
    propagated = False
    try:
        with manager():
            raise ValueError("x")
    except ValueError:
        propagated = True
    assert propagated is True


@check
def ex19_assert_vs_validation():
    def set_port(port):
        # TODO：不要用 assert；非法时 ValueError
        return port
    assert set_port(80) == 80
    try:
        set_port(0)
    except ValueError:
        pass
    else:
        raise AssertionError("port=0 应抛 ValueError")


@check
def ex20_assert_internal_invariant():
    data = [3, 1, 2]
    result = sorted(data)
    # TODO：用 assert 检查元素数量不变
    assert True
    assert result == [1, 2, 3]


@check
def ex21_format_traceback():
    import traceback
    try:
        1 / 0
    except ZeroDivisionError:
        text = None  # TODO：得到当前 traceback 字符串
    assert "ZeroDivisionError" in text


@check
def ex22_sys_exception():
    import sys
    try:
        {}["x"]
    except KeyError:
        exc = None  # TODO：Python 3.11+
    assert isinstance(exc, KeyError)


@check
def ex23_logging_exception():
    stream = io.StringIO()
    logger = logging.getLogger("exercise23")
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(logging.ERROR)
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    try:
        1 / 0
    except ZeroDivisionError:
        # TODO：记录 message + traceback
        logger.error("failed")
    text = stream.getvalue()
    assert "failed" in text
    assert "ZeroDivisionError" in text


@check
def ex24_log_once_boundary():
    """这里用计数模拟日志：底层不记录，边界只记录一次。"""
    logs = []
    def inner():
        raise ValueError("bad")
    def middle():
        # TODO：不要 logs.append，直接传播
        inner()
    try:
        middle()
    except ValueError as exc:
        logs.append(type(exc).__name__)
    assert logs == ["ValueError"]


@check
def ex25_add_note():
    exc = ValueError("bad row")
    # TODO：添加 "row=7"
    assert "row=7" in exc.__notes__


@check
def ex26_preserve_same_exception_with_note():
    original = None
    caught = None
    try:
        try:
            original = ValueError("bad")
            raise original
        except ValueError as exc:
            # TODO：add_note("file=data.csv") 后原样抛出
            pass
    except ValueError as exc:
        caught = exc
    assert caught is original
    assert "file=data.csv" in caught.__notes__


@check
def ex27_exception_group_size():
    group = ExceptionGroup("x", [ValueError("a"), TypeError("b")])
    result = None  # TODO
    assert result == 2


@check
def ex28_exception_group_split():
    group = ExceptionGroup("x", [ValueError("a"), TypeError("b"), ValueError("c")])
    matched, rest = group.split(ValueError)
    value_count = None  # TODO
    rest_count = None   # TODO
    assert value_count == 2
    assert rest_count == 1


@check
def ex29_async_exception_propagates():
    async def fail():
        raise ValueError("bad")
    async def runner():
        try:
            await fail()
        except ValueError:
            return "caught"  # TODO 可保留或改写
    assert asyncio.run(runner()) == "caught"


@check
def ex30_async_timeout():
    async def runner():
        try:
            async with asyncio.timeout(0.001):
                await asyncio.sleep(0.05)
        # TODO：捕获正确的超时异常
        except RuntimeError:
            return "timeout"
    assert asyncio.run(runner()) == "timeout"


@check
def ex31_warning_category():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        # TODO：发出 UserWarning("careful")
        pass
    assert len(caught) == 1
    assert caught[0].category is UserWarning


@check
def ex32_warning_to_error():
    raised = False
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)  # 防止未完成时污染练习输出
        # TODO：把上面的过滤策略改成 error，让 UserWarning 变成异常
        try:
            warnings.warn("x", UserWarning)
        except UserWarning:
            raised = True
    assert raised is True


@check
def ex33_builtin_exception_contract():
    def repeat(text, count):
        if not isinstance(text, str):
            # TODO
            raise ValueError("wrong")
        if count < 0:
            # TODO
            raise TypeError("wrong")
        return text * count
    try:
        repeat(123, 2)
    except TypeError:
        pass
    else:
        raise AssertionError("text 类型错应抛 TypeError")
    try:
        repeat("a", -1)
    except ValueError:
        pass
    else:
        raise AssertionError("count 值非法应抛 ValueError")


@check
def ex34_do_not_parse_message():
    class NotFoundError(Exception):
        pass
    def load(found):
        if not found:
            raise NotFoundError("whatever text")
        return 1
    result = None
    try:
        load(False)
    except NotFoundError:
        # TODO：按类型处理，不解析字符串
        result = "not_found"
    assert result == "not_found"


@check
def ex35_no_swallow():
    propagated = False
    try:
        try:
            raise RuntimeError("boom")
        except RuntimeError:
            # TODO：继续传播
            pass
    except RuntimeError:
        propagated = True
    assert propagated


@check
def ex36_narrow_catch():
    class Explodes:
        def __int__(self):
            raise RuntimeError("unexpected bug")

    def parse(text):
        try:
            return int(text)
        # TODO：不要 except Exception，只处理预期解析失败
        except Exception:
            return None

    assert parse("x") is None
    try:
        parse(Explodes())
    except RuntimeError:
        pass
    else:
        raise AssertionError("RuntimeError 不应被解析错误处理逻辑吞掉")


@check
def ex37_preserve_cause():
    class PublicError(Exception):
        pass
    try:
        try:
            {}["x"]
        except KeyError as exc:
            # TODO
            raise PublicError("lookup failed")
    except PublicError as exc:
        assert isinstance(exc.__cause__, KeyError)


@check
def ex38_no_finally_return():
    """修复逻辑：异常必须能传播。"""
    propagated = False
    def f():
        try:
            raise ValueError("x")
        finally:
            # TODO：这里不能 return
            return 123
    try:
        f()
    except ValueError:
        propagated = True
    assert propagated


@check
def ex39_sensitive_data_not_in_message():
    password = "secret123"
    try:
        # TODO：抛出的错误信息不能包含 password
        raise ValueError(f"login failed password={password}")
    except ValueError as exc:
        assert password not in str(exc)


@check
def ex40_boundary_design():
    class ServiceError(Exception):
        pass
    def service():
        raise ServiceError("down")
    def endpoint():
        try:
            service()
        except ServiceError:
            # TODO：边界转换为稳定响应
            return None
    assert endpoint() == (503, {"error": "service unavailable"})


@check
def ex41_eafp_dict():
    data = {"x": 1}
    def get_y():
        # TODO：直接读取 data["y"]，用 KeyError 回退 0
        return None
    assert get_y() == 0


@check
def ex42_narrow_eafp():
    class BrokenMapping:
        def __getitem__(self, key):
            raise RuntimeError("storage broken")

    def parse(mapping):
        try:
            return int(mapping["port"])
        # TODO：只捕获预期的 KeyError / ValueError / TypeError
        except Exception:
            return 8000
    assert parse({}) == 8000
    assert parse({"port": "bad"}) == 8000
    assert parse({"port": "9000"}) == 9000
    try:
        parse(BrokenMapping())
    except RuntimeError:
        pass
    else:
        raise AssertionError("非预期 RuntimeError 不应被吞掉")


@check
def ex43_system_exceptions():
    # TODO：验证 KeyboardInterrupt 不属于 Exception
    result = None
    assert result is True


@check
def ex44_cli_boundary():
    def run():
        raise KeyboardInterrupt
    def main():
        try:
            run()
        # TODO：捕获 Ctrl+C 并返回 130
        except Exception:
            return 1

    # 未完成时也不能让整个练习册被 Ctrl+C 语义中断，所以题目外层兜住用于判分。
    try:
        result = main()
    except KeyboardInterrupt:
        result = None
    assert result == 130


def run_all():
    print("=" * 72)
    print("04_exception_study 自动练习")
    print("=" * 72)
    passed = 0
    for fn in _CHECKS:
        try:
            fn()
        except AssertionError as exc:
            print(f"[FAIL] {fn.__name__:<36} {exc or '断言未通过'}")
        except Exception as exc:
            print(f"[ERR ] {fn.__name__:<36} {type(exc).__name__}: {exc}")
        else:
            passed += 1
            print(f"[ OK ] {fn.__name__:<36}")
    print("-" * 72)
    print(f"通过 {passed}/{len(_CHECKS)}")
    if passed == len(_CHECKS):
        print("异常处理通关。")


if __name__ == "__main__":
    run_all()


# ============================================================================
# 参考答案（建议先自己做）
# ============================================================================
"""
ex01
    try:
        return int(text)
    except ValueError:
        return None

ex02
    result = type(exc).__name__

ex03
    result = issubclass(FileNotFoundError, OSError)

ex04
    Base = Exception

ex05
    except (ValueError, TypeError):

ex06
    try:
        n = int(text)
    except ValueError:
        return None
    return n * 2

ex07
    events.append(f"success:{n}")

ex08
    events.append("cleanup")

ex09
    if value < 0:
        raise ValueError("age cannot be negative")

ex10
    raise

ex11
    raise ConfigError("bad config") from exc

ex12
    raise ValueError("missing") from None

ex13
    class ValidationError(AppError):
        pass

ex14
    self.field = field
    self.value = value
    super().__init__(f"{field}={value!r}")

ex15
    raise ServiceError("service unavailable") from exc

ex16
    return "database"

ex17
    events.append("close")

ex18
    raise

ex19
    if not 1 <= port <= 65535:
        raise ValueError("invalid port")

ex20
    assert len(result) == len(data)

ex21
    text = traceback.format_exc()

ex22
    exc = sys.exception()

ex23
    logger.exception("failed")

ex24
    middle 中保持：inner()

ex25
    exc.add_note("row=7")

ex26
    exc.add_note("file=data.csv")
    raise

ex27
    result = len(group.exceptions)

ex28
    value_count = len(matched.exceptions)
    rest_count = len(rest.exceptions)

ex29
    当前实现已经正确；关键是 await 后在调用方捕获。

ex30
    except TimeoutError:

ex31
    warnings.warn("careful", UserWarning)

ex32
    warnings.simplefilter("error", UserWarning)  # 替换题目里的 ignore

ex33
    text 类型错误 -> raise TypeError
    count 值非法 -> raise ValueError

ex34
    当前 except NotFoundError 的做法就是正确方向。

ex35
    raise

ex36
    except ValueError:

ex37
    raise PublicError("lookup failed") from exc

ex38
    删除 finally 中的 return；可写 pass 或清理逻辑。

ex39
    raise ValueError("login failed")

ex40
    return 503, {"error": "service unavailable"}

ex41
    try:
        return data["y"]
    except KeyError:
        return 0

ex42
    except (KeyError, ValueError, TypeError):

ex43
    result = not issubclass(KeyboardInterrupt, Exception)

ex44
    except KeyboardInterrupt:
        return 130
"""
