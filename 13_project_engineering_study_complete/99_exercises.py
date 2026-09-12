# -*- coding: utf-8 -*-
"""
13_project_engineering_study_complete 练习册 —— 64 题
========================================

运行: python 99_exercises.py
所有 TODO 未完成时应 FAIL，不应 ERR。
参考答案在底部。
"""

import io
import sys
import tomllib
import zipfile
from pathlib import PurePosixPath, PureWindowsPath

_checks=[]
def check(fn):
    _checks.append(fn)
    return fn

@check
def ex01_project_files():
    def missing_required(files: set[str]) -> set[str]:
        pass  # TODO

    assert missing_required({"README.md"}) == {"pyproject.toml", "src", "tests"}
    assert missing_required({"README.md", "pyproject.toml", "src", "tests"}) == set()

@check
def ex02_venv_dir():
    result = None  # TODO
    assert result == ".venv"

@check
def ex03_module_pip():
    def module_command(executable: str, module: str, *args: str) -> list[str]:
        pass  # TODO

    assert module_command("python", "pip", "--version") == ["python", "-m", "pip", "--version"]
    assert module_command(sys.executable, "unittest") == [sys.executable, "-m", "unittest"]

@check
def ex04_interpreter_check():
    import sys
    result = None  # TODO
    assert result == sys.executable

@check
def ex05_requirement_spec():
    def compatible_range(name: str, minimum: str, next_major: int) -> str:
        pass  # TODO

    assert compatible_range("requests", "2.32", 3) == "requests>=2.32,<3"
    assert compatible_range("httpx", "0.28", 1) == "httpx>=0.28,<1"

@check
def ex06_constraints_meaning():
    result = None  # TODO
    assert result is False

@check
def ex07_lock_for_app():
    def dependency_policy(project_kind: str) -> str:
        pass  # TODO

    assert dependency_policy("library") == "compatible-range"
    assert dependency_policy("application") == "resolved-lock"

@check
def ex08_freeze_snapshot():
    result = None  # TODO
    assert result == "snapshot"

@check
def ex09_pyproject_sections():
    def standard_sections(data: dict[str, object]) -> set[str]:
        pass  # TODO

    data = {"build-system": {}, "project": {}, "tool": {"ruff": {}}, "custom": {}}
    assert standard_sections(data) == {"build-system", "project", "tool"}

@check
def ex10_parse_toml():
    import tomllib
    cfg=tomllib.loads('[project]\nname="demo"\n')
    result = None  # TODO
    assert result == "demo"

@check
def ex11_build_requires():
    def misplaced_runtime_dependencies(build_requires: list[str], runtime: list[str]) -> set[str]:
        pass  # TODO

    assert misplaced_runtime_dependencies(["setuptools", "requests"], ["requests"]) == {"requests"}
    assert misplaced_runtime_dependencies(["hatchling"], ["httpx"]) == set()

@check
def ex12_backend_key():
    result = None  # TODO
    assert result == "build-backend"

@check
def ex13_requires_python():
    def runtime_metadata(raw: bytes) -> tuple[str, list[str]]:
        pass  # TODO

    raw = b'[project]\nrequires-python=">=3.11"\ndependencies=["httpx>=0.28,<1"]\n'
    assert runtime_metadata(raw) == (">=3.11", ["httpx>=0.28,<1"])

@check
def ex14_optional_extra():
    result = None  # TODO
    assert result == ".[dev]"

@check
def ex15_src_path():
    def package_path(root, import_name: str, src_layout: bool):
        pass  # TODO

    from pathlib import Path
    assert package_path(Path("project"), "demo_app", True) == Path("project/src/demo_app")
    assert package_path(Path("project"), "demo_app", False) == Path("project/demo_app")

@check
def ex16_editable():
    result = None  # TODO
    assert result == ["python","-m","pip","install","-e","."]

@check
def ex17_distribution_import():
    def import_name(distribution: str, mapping: dict[str, str]) -> str | None:
        pass  # TODO

    mapping = {"beautifulsoup4": "bs4", "Pillow": "PIL"}
    assert import_name("pillow", mapping) == "PIL"
    assert import_name("unknown", mapping) is None

@check
def ex18_name_relation():
    result = None  # TODO
    assert result is False

@check
def ex19_resource_api():
    def safe_package_resource(path: str) -> bool:
        pass  # TODO

    assert safe_package_resource("templates/report.txt") is True
    assert safe_package_resource("../secret.txt") is False
    assert safe_package_resource("/tmp/data.txt") is False

@check
def ex20_cwd_assumption():
    result = None  # TODO
    assert result is False

@check
def ex21_metadata_version():
    def installed_version(name: str, lookup) -> str:
        pass  # TODO

    versions = {"demo-app": "1.4.2"}
    assert installed_version("demo-app", versions.get) == "1.4.2"
    assert installed_version("missing", versions.get) == "unknown"

@check
def ex22_single_version_source():
    result = None  # TODO
    assert result is True

@check
def ex23_argparse_return():
    def main(argv: list[str], output: list[str]) -> int:
        pass  # TODO

    output: list[str] = []
    assert main(["Alice"], output) == 0
    assert output == ["hello Alice"]

@check
def ex24_cli_testability():
    result = None  # TODO
    assert result is True

@check
def ex25_dunder_main():
    def module_entry_path(package_dir):
        pass  # TODO

    from pathlib import Path
    assert module_entry_path(Path("src/demo_app")) == Path("src/demo_app/__main__.py")

@check
def ex26_system_exit():
    result = None  # TODO
    assert result == "SystemExit"

@check
def ex27_project_scripts():
    def split_reference(reference: str) -> tuple[str, str]:
        pass  # TODO

    assert split_reference("demo_app.cli:main") == ("demo_app.cli", "main")

@check
def ex28_entry_object_ref():
    result = None  # TODO
    assert result == "demo_app.cli:main"

@check
def ex29_config_priority():
    def resolve(default, file_value=None, env_value=None, cli_value=None):
        pass  # TODO

    assert resolve(8000, 8080, 9000, 7000) == 7000
    assert resolve(8000, 0, None, None) == 0

@check
def ex30_none_vs_falsy():
    value=0
    result = None  # TODO
    assert result == 0

@check
def ex31_secret_in_git():
    def unsafe_sinks(sinks: set[str]) -> set[str]:
        pass  # TODO

    assert unsafe_sinks({"secret-manager", "git", "logs", "environment"}) == {"git", "logs"}

@check
def ex32_mask_secret():
    secret="abcdefghij"
    result = None  # TODO
    assert result == "ab***ij"

@check
def ex33_data_paths():
    def data_paths(root):
        pass  # TODO

    from pathlib import Path
    assert data_paths(Path("/app")) == {
        "config": Path("/app/config"),
        "data": Path("/app/data"),
        "cache": Path("/app/cache"),
    }

@check
def ex34_pathlib_join():
    from pathlib import Path
    root=Path("data")
    result = None  # TODO
    assert result == Path("data")/"cache"

@check
def ex35_exit_code_mapping():
    def exit_code(status: str) -> int:
        pass  # TODO

    assert exit_code("ok") == 0
    assert exit_code("usage-error") == 2
    assert exit_code("failure") == 1

@check
def ex36_business_sys_exit():
    result = None  # TODO
    assert result is False

@check
def ex37_subprocess_arguments():
    def python_child(code: str) -> list[str]:
        pass  # TODO

    assert python_child("print('ok')") == [sys.executable, "-c", "print('ok')"]

@check
def ex38_subprocess_timeout():
    result = None  # TODO
    assert result is True

@check
def ex39_metadata_fields():
    def identity(metadata: dict[str, str]) -> tuple[str, str, str | None]:
        pass  # TODO

    meta = {"Name": "demo-app", "Version": "1.0", "Requires-Python": ">=3.11"}
    assert identity(meta) == ("demo-app", "1.0", ">=3.11")

@check
def ex40_entry_points_plugins():
    result = None  # TODO
    assert result is True

@check
def ex41_artifact_kind():
    def kind(filename: str) -> str:
        pass  # TODO

    assert kind("demo-1.0.tar.gz") == "sdist"
    assert kind("demo-1.0-py3-none-any.whl") == "wheel"
    assert kind("README.md") == "unknown"

@check
def ex42_wheel_ext():
    result = None  # TODO
    assert result == ".whl"

@check
def ex43_wheel_members():
    def members(raw: bytes) -> set[str]:
        pass  # TODO

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("demo/__init__.py", "")
        archive.writestr("demo-1.0.dist-info/METADATA", "Name: demo\n")
    assert members(buffer.getvalue()) == {
        "demo/__init__.py",
        "demo-1.0.dist-info/METADATA",
    }

@check
def ex44_dist_info():
    result = None  # TODO
    assert result is not None
    assert result.endswith(".dist-info")

@check
def ex45_editable_command():
    def command(project: str = ".", extra: str | None = None) -> list[str]:
        pass  # TODO

    assert command() == [sys.executable, "-m", "pip", "install", "-e", "."]
    assert command(".", "dev")[-1] == ".[dev]"

@check
def ex46_editable_metadata():
    result = None  # TODO
    assert result is True

@check
def ex47_workflow_order():
    def valid_workflow(steps: list[str]) -> bool:
        pass  # TODO

    good = ["create-venv", "install", "test", "build", "install-smoke"]
    assert valid_workflow(good) is True
    assert valid_workflow(["build", "test", "install"]) is False

@check
def ex48_workflow_order():
    result = None  # TODO
    assert result == "test-first"

@check
def ex49_release_chain():
    def valid_release(steps: list[str]) -> bool:
        pass  # TODO

    assert valid_release(["test", "build", "inspect", "install-smoke", "publish"]) is True
    assert valid_release(["build", "publish", "test"]) is False

@check
def ex50_long_token_git():
    result = None  # TODO
    assert result is False

@check
def ex51_install_target():
    def installer(artifact_kind: str) -> str:
        pass  # TODO

    assert installer("cli-application") == "pipx"
    assert installer("project-library") == "project-venv"

@check
def ex52_cli_entrypoint():
    result = None  # TODO
    assert result is True

@check
def ex53_release_record():
    def complete(record: dict[str, str]) -> bool:
        pass  # TODO

    required = {"version", "tag", "commit", "released-at", "changes"}
    assert complete({key: "value" for key in required}) is True
    assert complete({"version": "1.0", "tag": "v1.0"}) is False

@check
def ex54_republish_same_version():
    result = None  # TODO
    assert result is False

@check
def ex55_ci_matrix():
    def jobs(pythons: list[str], systems: list[str]) -> set[tuple[str, str]]:
        pass  # TODO

    assert jobs(["3.12", "3.13"], ["linux", "windows"]) == {
        ("3.12", "linux"),
        ("3.12", "windows"),
        ("3.13", "linux"),
        ("3.13", "windows"),
    }

@check
def ex56_matrix():
    result = None  # TODO
    assert result is True

@check
def ex57_required_gates():
    def missing(required: set[str], passed: set[str]) -> set[str]:
        pass  # TODO

    required = {"test", "type", "build"}
    assert missing(required, {"test", "build"}) == {"type"}
    assert missing(required, required) == set()

@check
def ex58_tools_more_better():
    result = None  # TODO
    assert result is False

@check
def ex59_docker_contents():
    def forbidden(paths: list[str]) -> set[str]:
        pass  # TODO

    paths = ["src/app.py", ".env", ".git/config", "pyproject.toml"]
    assert forbidden(paths) == {".env", ".git/config"}

@check
def ex60_docker_replaces_testing():
    result = None  # TODO
    assert result is False

@check
def ex61_windows_path_resolution():
    def resolve(base: str, relative: str) -> PureWindowsPath:
        pass  # TODO

    assert resolve(r"C:\ProgramData\Demo", "logs/app.log") == PureWindowsPath(
        r"C:\ProgramData\Demo\logs\app.log"
    )

@check
def ex62_packaging_dependency_mgmt():
    result = None  # TODO
    assert result is False

@check
def ex63_deployment_readiness():
    def ready(checks: dict[str, bool]) -> bool:
        pass  # TODO

    good = {"install": True, "smoke": True, "config": True, "logs": True, "rollback": True}
    assert ready(good) is True
    assert ready({**good, "rollback": False}) is False

@check
def ex64_rollback():
    result = None  # TODO
    assert result is True

def run_all():
    print("="*70)
    print("13_project_engineering_study_complete 练习册")
    print("="*70)
    passed=failed=errors=0
    for fn in _checks:
        try:
            fn()
        except AssertionError as e:
            failed += 1
            print(f"[FAIL] {fn.__name__:<34} {e or ''}")
        except Exception as e:
            errors += 1
            print(f"[ERR ] {fn.__name__:<34} {type(e).__name__}: {e}")
        else:
            passed += 1
            print(f"[ OK ] {fn.__name__}")
    print("-"*70)
    print(f"通过 {passed}/{len(_checks)} | FAIL={failed} | ERR={errors}")
    return passed,failed,errors

if __name__ == "__main__":
    run_all()

# ====================================================================
# 参考答案
# ====================================================================
# ex01_project_files
#     return {"pyproject.toml", "README.md", "src", "tests"} - files
#
# ex02_venv_dir
#     result = ".venv"
#
# ex03_module_pip
#     return [executable, "-m", module, *args]
#
# ex04_interpreter_check
#     result = sys.executable
#
# ex05_requirement_spec
#     return f"{name}>={minimum},<{next_major}"
#
# ex06_constraints_meaning
#     result = False
#
# ex07_lock_for_app
#     return {"library": "compatible-range", "application": "resolved-lock"}[project_kind]
#
# ex08_freeze_snapshot
#     result = "snapshot"
#
# ex09_pyproject_sections
#     return set(data) & {"build-system", "project", "tool"}
#
# ex10_parse_toml
#     result = cfg["project"]["name"]
#
# ex11_build_requires
#     return set(build_requires) & set(runtime)
#
# ex12_backend_key
#     result = "build-backend"
#
# ex13_requires_python
#     data = tomllib.loads(raw.decode())["project"]
#     return data["requires-python"], data["dependencies"]
#
# ex14_optional_extra
#     result = ".[dev]"
#
# ex15_src_path
#     return root / "src" / import_name if src_layout else root / import_name
#
# ex16_editable
#     result = ["python","-m","pip","install","-e","."]
#
# ex17_distribution_import
#     return next((v for k, v in mapping.items() if k.casefold() == distribution.casefold()), None)
#
# ex18_name_relation
#     result = False
#
# ex19_resource_api
#     p = PurePosixPath(path)
#     return not p.is_absolute() and ".." not in p.parts
#
# ex20_cwd_assumption
#     result = False
#
# ex21_metadata_version
#     return lookup(name) or "unknown"
#
# ex22_single_version_source
#     result = True
#
# ex23_argparse_return
#     output.append(f"hello {argv[0]}")
#     return 0
#
# ex24_cli_testability
#     result = True
#
# ex25_dunder_main
#     return package_dir / "__main__.py"
#
# ex26_system_exit
#     result = "SystemExit"
#
# ex27_project_scripts
#     return tuple(reference.split(":", 1))
#
# ex28_entry_object_ref
#     result = "demo_app.cli:main"
#
# ex29_config_priority
#     return next(v for v in (cli_value, env_value, file_value, default) if v is not None)
#
# ex30_none_vs_falsy
#     result = 100 if value is None else value
#
# ex31_secret_in_git
#     return sinks & {"git", "logs", "traceback", "image"}
#
# ex32_mask_secret
#     result = secret[:2] + "***" + secret[-2:]
#
# ex33_data_paths
#     return {name: root / name for name in ("config", "data", "cache")}
#
# ex34_pathlib_join
#     result = root / "cache"
#
# ex35_exit_code_mapping
#     return {"ok": 0, "usage-error": 2, "failure": 1}[status]
#
# ex36_business_sys_exit
#     result = False
#
# ex37_subprocess_arguments
#     return [sys.executable, "-c", code]
#
# ex38_subprocess_timeout
#     result = True
#
# ex39_metadata_fields
#     return metadata["Name"], metadata["Version"], metadata.get("Requires-Python")
#
# ex40_entry_points_plugins
#     result = True
#
# ex41_artifact_kind
#     if filename.endswith(".tar.gz"): return "sdist"
#     if filename.endswith(".whl"): return "wheel"
#     return "unknown"
#
# ex42_wheel_ext
#     result = ".whl"
#
# ex43_wheel_members
#     with zipfile.ZipFile(io.BytesIO(raw)) as archive: return set(archive.namelist())
#
# ex44_dist_info
#     result = "demo-1.0.dist-info"
#
# ex45_editable_command
#     target = f"{project}[{extra}]" if extra else project
#     return [sys.executable, "-m", "pip", "install", "-e", target]
#
# ex46_editable_metadata
#     result = True
#
# ex47_workflow_order
#     return steps == ["create-venv", "install", "test", "build", "install-smoke"]
#
# ex48_workflow_order
#     result = "test-first"
#
# ex49_release_chain
#     return steps == ["test", "build", "inspect", "install-smoke", "publish"]
#
# ex50_long_token_git
#     result = False
#
# ex51_install_target
#     return "pipx" if artifact_kind == "cli-application" else "project-venv"
#
# ex52_cli_entrypoint
#     result = True
#
# ex53_release_record
#     return {"version", "tag", "commit", "released-at", "changes"} <= record.keys()
#
# ex54_republish_same_version
#     result = False
#
# ex55_ci_matrix
#     return {(python, system) for python in pythons for system in systems}
#
# ex56_matrix
#     result = True
#
# ex57_required_gates
#     return required - passed
#
# ex58_tools_more_better
#     result = False
#
# ex59_docker_contents
#     return {path for path in paths if path == ".env" or path.startswith(".git/")}
#
# ex60_docker_replaces_testing
#     result = False
#
# ex61_windows_path_resolution
#     return PureWindowsPath(base) / PureWindowsPath(relative)
#
# ex62_packaging_dependency_mgmt
#     result = False
#
# ex63_deployment_readiness
#     return all(checks.get(name, False) for name in ("install", "smoke", "config", "logs", "rollback"))
#
# ex64_rollback
#     result = True
#
