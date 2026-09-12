"""供 05_module_package_study 教程使用的小型演示包。"""

PACKAGE_NAME = "demo_pkg"

from .greeter import greet

__all__ = ["PACKAGE_NAME", "greet"]
