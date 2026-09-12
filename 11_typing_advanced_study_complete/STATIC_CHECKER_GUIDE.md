# 静态检查器练习指南

教程本身只依赖 Python 标准库。真正验证 Protocol、variance、overload、类型缩窄等静态规则时，建议另外安装一种静态检查器。

## Pyright

```powershell
pip install pyright
pyright static_cases/01_good_generic.py
pyright static_cases/02_intentional_errors.py
pyright static_cases/03_protocol_demo.py
```

后两个文件故意包含错误，应该看到诊断信息。

## mypy

```powershell
pip install mypy
mypy static_cases/01_good_generic.py
mypy static_cases/02_intentional_errors.py
mypy static_cases/03_protocol_demo.py
```

不同检查器在少量边缘规则和新特性支持时间上可能不同。项目应固定一个主检查器、Python 版本和配置，而不是为了消除所有检查器差异而大量使用 `Any` 或 `# type: ignore`。
