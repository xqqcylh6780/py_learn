# -*- coding: utf-8 -*-
"""
模块与包练习册 —— 48 题，自动判分
=================================

运行：
    python 99_exercises.py

每两题对应一节教程。先自己完成 TODO，再看文件底部参考答案。
练习尽量验证“导入语义”，而不是只背术语。
"""

import importlib
import importlib.util
import sys
import types
from pathlib import Path
from typing import TYPE_CHECKING

_checks = []


def check(fn):
    _checks.append(fn)
    return fn


# 01 模块是什么与 import 执行
@check
def ex01_module_object():
    import demo_pkg.math_tools as m
    result = None  # TODO：判断 m 是否是模块对象
    assert result is True


@check
def ex02_module_namespace():
    import demo_pkg.math_tools as m
    result = None  # TODO：从模块命名空间字典中取 PI
    assert result == m.PI


# 02 __name__ / __main__
@check
def ex03_is_entry_module():
    def is_entry(name):
        return None  # TODO
    assert is_entry("__main__") is True
    assert is_entry("pkg.tool") is False


@check
def ex04_main_guard_behavior():
    calls = []
    def run(name):
        # TODO：只有 name == '__main__' 时 append('main')
        pass
    run("pkg.mod")
    assert calls == []
    run("__main__")
    assert calls == ["main"]


# 03 sys.path
@check
def ex05_path_contains_current_dir():
    here = str(Path(__file__).resolve().parent)
    result = None  # TODO：判断当前教程目录是否能从 sys.path 找到
    assert result is True


@check
def ex06_find_existing_spec():
    spec = None  # TODO：查 demo_pkg.math_tools 的 spec
    assert spec is not None
    assert spec.name == "demo_pkg.math_tools"


# 04 package / __init__.py
@check
def ex07_package_has_path():
    import demo_pkg
    result = None  # TODO
    assert result is True


@check
def ex08_package_level_api():
    import demo_pkg
    result = None  # TODO：通过包级 API 调 greet
    assert result == "Hello, Alice!"


# 05 绝对/相对导入
@check
def ex09_absolute_import():
    module = None  # TODO：导入 demo_pkg.subpkg.formatter 模块对象
    assert module is not None
    assert module.__name__ == "demo_pkg.subpkg.formatter"
    assert module.excited("x") == "HELLO, X!"


@check
def ex10_relative_import_with_importlib():
    module = None  # TODO：用 importlib.import_module('.greeter', package='demo_pkg')
    assert module is not None
    assert module.__name__ == "demo_pkg.greeter"


# 06 import 写法与绑定
@check
def ex11_alias_binding():
    import demo_pkg.math_tools as mt
    alias = None  # TODO：让 alias 指向同一个模块对象
    assert alias is mt


@check
def ex12_from_import_snapshot():
    temp = types.ModuleType("_exercise_temp_mod")
    temp.value = 1
    local_value = None  # TODO：模拟 from mod import value 后本地绑定的值
    temp.value = 2
    assert local_value == 1
    assert temp.value == 2


# 07 __all__
@check
def ex13_read_all():
    import demo_pkg
    result = None  # TODO
    assert result == ["PACKAGE_NAME", "greet"]


@check
def ex14_filter_public_names():
    names = ["a", "_b", "c", "__magic__"]
    result = None  # TODO：只保留不以下划线开头的名字
    assert result == ["a", "c"]


# 08 sys.modules
@check
def ex15_sys_modules_lookup():
    import demo_pkg.greeter as g
    result = None  # TODO：从 sys.modules 按全名取对象
    assert result is g


@check
def ex16_cached_import_identity():
    a = importlib.import_module("demo_pkg.math_tools")
    b = importlib.import_module("demo_pkg.math_tools")
    result = None  # TODO
    assert result is True


# 09 importlib / reload
@check
def ex17_dynamic_import():
    name = "demo_pkg.greeter"
    module = None  # TODO
    assert module is not None
    assert module.greet("D") == "Hello, D!"


@check
def ex18_reload_returns_module():
    import demo_pkg.math_tools as m
    result = None  # TODO：reload m
    assert result is m


# 10 python -m
@check
def ex19_build_m_command():
    module = "demo_pkg.subpkg.formatter"
    cmd = None  # TODO：构造 [sys.executable, '-m', module]
    assert cmd == [sys.executable, "-m", module]


@check
def ex20_build_pip_command():
    args = None  # TODO：构造当前 Python 对应 pip --version 命令列表
    assert args == [sys.executable, "-m", "pip", "--version"]


# 11 循环导入
@check
def ex21_dependency_direction():
    # domain <- services <- web，返回一个不会反向依赖的边集合
    edges = None  # TODO：例如 {('services','domain'), ('web','services')}
    assert edges == {("services", "domain"), ("web", "services")}


@check
def ex22_local_import_delay():
    def load_greeter():
        # TODO：函数调用时再 import 并返回 greet
        return None
    fn = load_greeter()
    assert callable(fn)
    assert fn("X") == "Hello, X!"


# 12 TYPE_CHECKING
@check
def ex23_type_checking_runtime():
    result = None  # TODO：正常运行时 TYPE_CHECKING 的布尔值
    assert result is False


@check
def ex24_type_only_branch():
    def should_import_at_runtime(type_checking_value):
        return None  # TODO：TYPE_CHECKING 风格分支在 runtime 不应执行
    assert should_import_at_runtime(False) is False
    assert should_import_at_runtime(True) is True


# 13 ModuleSpec
@check
def ex25_spec_name_origin():
    spec = importlib.util.find_spec("demo_pkg.math_tools")
    result = None  # TODO：返回 (spec.name, spec.origin 是否为字符串)
    assert result == ("demo_pkg.math_tools", True)


@check
def ex26_package_spec_search_locations():
    spec = importlib.util.find_spec("demo_pkg")
    result = None  # TODO：包是否具有 submodule_search_locations
    assert result is True


# 14 finder / loader
@check
def ex27_find_spec_without_import_api():
    spec = None  # TODO：使用 importlib.util.find_spec('json')
    assert spec is not None
    assert spec.name == "json"


@check
def ex28_meta_path_nonempty():
    result = None  # TODO
    assert result is True


# 15 namespace package
@check
def ex29_namespace_package_rule():
    def can_be_namespace(has_init_py):
        return None  # TODO：本题抽象规则：没有 __init__.py 时才返回 True
    assert can_be_namespace(False) is True
    assert can_be_namespace(True) is False


@check
def ex30_package_path_is_iterable():
    import demo_pkg
    result = None  # TODO：把 __path__ 转 list
    assert isinstance(result, list)
    assert len(result) >= 1


# 16 pycache
@check
def ex31_cache_path():
    result = None  # TODO：用 cache_from_source(__file__)
    assert isinstance(result, str)
    assert "__pycache__" in result
    assert result.endswith(".pyc")


@check
def ex32_cache_tag():
    result = None  # TODO
    assert result == sys.implementation.cache_tag
    assert isinstance(result, str)


# 17 resources
@check
def ex33_read_package_resource():
    from importlib import resources
    import demo_pkg.resources
    result = None  # TODO：读取 config.json 文本
    assert isinstance(result, str)
    assert '"app":"py_learn"' in result.replace(" ", "")


@check
def ex34_parse_package_resource():
    import json
    from importlib import resources
    import demo_pkg.resources
    result = None  # TODO：读取并 json.loads
    assert isinstance(result, dict)
    assert result["app"] == "py_learn"
    assert result["version"] == 1


# 18 项目结构
@check
def ex35_fully_qualified_name():
    package = "myapp"
    layer = "services"
    module = "user"
    result = None  # TODO
    assert result == "myapp.services.user"


@check
def ex36_detect_sys_path_hack():
    lines = ["import os", "sys.path.append('../..')", "from app import x"]
    result = None  # TODO：返回包含 'sys.path.append' 的行
    assert result == ["sys.path.append('../..')"]


# 19 导入副作用
@check
def ex37_lazy_factory():
    calls = []
    def create_client():
        calls.append("created")
        return object()
    # TODO：不要在这里提前调用 create_client；只把工厂保存到 factory
    factory = None
    assert calls == []
    assert callable(factory)
    factory()
    assert calls == ["created"]


@check
def ex38_import_time_safe_constant():
    # 顶层适合轻量常量；本题返回一个不可变配置 tuple
    config = None  # TODO
    assert config == ("localhost", 8000)
    assert isinstance(config, tuple)


# 20 插件加载
@check
def ex39_load_plugin_callable():
    def load(module_name, attr):
        # TODO：动态导入、getattr，并验证 callable；否则 TypeError
        return None
    fn = load("demo_pkg.greeter", "greet")
    assert callable(fn)
    assert fn("P") == "Hello, P!"
    try:
        load("demo_pkg.math_tools", "PI")
    except TypeError:
        pass
    else:
        raise AssertionError("非 callable 必须抛 TypeError")


@check
def ex40_allowlist_plugin_name():
    allowed = {"demo_pkg.greeter", "demo_pkg.math_tools"}
    def validate(name):
        # TODO：不在 allowlist 时抛 ValueError；在时原样返回
        return None
    assert validate("demo_pkg.greeter") == "demo_pkg.greeter"
    try:
        validate("os")
    except ValueError:
        pass
    else:
        raise AssertionError("未拒绝非 allowlist 模块")


# 21 module __getattr__ / __dir__
@check
def ex41_module_getattr_contract():
    def module_getattr(name):
        # TODO：name == 'answer' 返回 42；否则必须 AttributeError(name)
        return None
    assert module_getattr("answer") == 42
    try:
        module_getattr("missing")
    except AttributeError as e:
        assert e.args == ("missing",)
    else:
        raise AssertionError("未知属性应抛 AttributeError")


@check
def ex42_module_dir_contract():
    def module_dir():
        # TODO：返回排序后的 ['answer', 'version']
        return None
    assert module_dir() == ["answer", "version"]


# 22 公共 API
@check
def ex43_public_api_tuple():
    public = None  # TODO：稳定公开 API 名字
    assert public == ("Client", "AppError")


@check
def ex44_internal_name_convention():
    names = ["Client", "_ClientImpl", "AppError", "_helpers"]
    result = None  # TODO：筛出约定上的公共名字
    assert result == ["Client", "AppError"]


# 23 import 排错
@check
def ex45_module_not_found_subclass():
    result = None  # TODO：ModuleNotFoundError 是否是 ImportError 子类
    assert result is True


@check
def ex46_real_module_origin():
    import json
    result = None  # TODO：返回 ("origin", json 的 __file__)
    expected = getattr(json, "__file__", None)
    assert result == ("origin", expected)


# 24 常见陷阱
@check
def ex47_bad_shadow_names():
    files = ["json.py", "app.py", "typing.py", "user.py", "asyncio.py"]
    stdlib_names = {"json", "typing", "asyncio"}
    result = None  # TODO：返回会遮蔽这些标准库名的文件名
    assert result == ["json.py", "typing.py", "asyncio.py"]


@check
def ex48_preferred_import_style():
    choices = {
        "star": "from pkg import *",
        "explicit": "from pkg import Client, AppError",
    }
    result = None  # TODO：选择更适合公共业务代码的显式导入字符串
    assert result == "from pkg import Client, AppError"


def run_all():
    print("=" * 72)
    print("模块与包练习册")
    print("=" * 72)
    passed = 0
    for fn in _checks:
        label = f"{fn.__name__:<38}"
        try:
            fn()
        except AssertionError as e:
            print(f"[FAIL] {label} {e or '断言没通过'}")
        except Exception as e:
            print(f"[ERR ] {label} {type(e).__name__}: {e}")
        else:
            passed += 1
            print(f"[ OK ] {label}")
    print("-" * 72)
    print(f"通过 {passed}/{len(_checks)}")
    if passed == len(_checks):
        print("模块与包专题通关。")


if __name__ == "__main__":
    run_all()


# ============================================================================
# 参考答案
# ============================================================================
"""
ex01
    result = isinstance(m, types.ModuleType)

ex02
    result = m.__dict__["PI"]

ex03
    return name == "__main__"

ex04
    if name == "__main__":
        calls.append("main")

ex05
    result = here in [str(Path(p or '.').resolve()) for p in sys.path]

ex06
    spec = importlib.util.find_spec("demo_pkg.math_tools")

ex07
    result = hasattr(demo_pkg, "__path__")

ex08
    result = demo_pkg.greet("Alice")

ex09
    module = importlib.import_module("demo_pkg.subpkg.formatter")

ex10
    module = importlib.import_module(".greeter", package="demo_pkg")

ex11
    alias = mt

ex12
    local_value = temp.value

ex13
    result = demo_pkg.__all__

ex14
    result = [name for name in names if not name.startswith("_")]

ex15
    result = sys.modules["demo_pkg.greeter"]

ex16
    result = (a is b)

ex17
    module = importlib.import_module(name)

ex18
    result = importlib.reload(m)

ex19
    cmd = [sys.executable, "-m", module]

ex20
    args = [sys.executable, "-m", "pip", "--version"]

ex21
    edges = {("services", "domain"), ("web", "services")}

ex22
    from demo_pkg.greeter import greet
    return greet

ex23
    result = TYPE_CHECKING

ex24
    return bool(type_checking_value)

ex25
    result = (spec.name, isinstance(spec.origin, str))

ex26
    result = spec.submodule_search_locations is not None

ex27
    spec = importlib.util.find_spec("json")

ex28
    result = len(sys.meta_path) > 0

ex29
    return not has_init_py

ex30
    result = list(demo_pkg.__path__)

ex31
    result = importlib.util.cache_from_source(__file__)

ex32
    result = sys.implementation.cache_tag

ex33
    result = resources.files(demo_pkg.resources).joinpath("config.json").read_text(encoding="utf-8")

ex34
    text = resources.files(demo_pkg.resources).joinpath("config.json").read_text(encoding="utf-8")
    result = json.loads(text)

ex35
    result = f"{package}.{layer}.{module}"

ex36
    result = [line for line in lines if "sys.path.append" in line]

ex37
    factory = create_client

ex38
    config = ("localhost", 8000)

ex39
    module = importlib.import_module(module_name)
    value = getattr(module, attr)
    if not callable(value):
        raise TypeError(attr)
    return value

ex40
    if name not in allowed:
        raise ValueError(name)
    return name

ex41
    if name == "answer":
        return 42
    raise AttributeError(name)

ex42
    return sorted(["version", "answer"])

ex43
    public = ("Client", "AppError")

ex44
    result = [name for name in names if not name.startswith("_")]

ex45
    result = issubclass(ModuleNotFoundError, ImportError)

ex46
    result = ("origin", getattr(json, "__file__", None))

ex47
    result = [f for f in files if Path(f).stem in stdlib_names]

ex48
    result = choices["explicit"]
"""
