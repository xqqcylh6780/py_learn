# -*- coding: utf-8 -*-
"""
32 pytest 与现代测试工具生态
===================

直接运行本文件即可观察示例。
"""
print("本仓库这一包坚持标准库可运行，因此主线使用 unittest。")
print("但真实 Python 项目必须认识现代测试生态。")

print(r"""
pytest
------
常见优势：
- 普通 assert 就有丰富失败信息
- fixture
- @pytest.mark.parametrize
- monkeypatch
- tmp_path
- caplog / capsys
- 插件生态

coverage.py
-----------
测 statement / branch coverage。
高覆盖率不等于高质量测试，但能发现明显遗漏区域。

Hypothesis
----------
Property-based testing。
不是手写几个固定样例，而是声明性质，让工具生成大量输入。
适合解析器、序列化、数学性质、边界输入。

tox / nox
---------
在多个 Python 版本、依赖组合或任务环境中重复运行测试。

pytest-xdist
------------
并行跑测试。前提是测试真正隔离，不能争抢固定端口和共享文件。

CI
--
GitHub Actions / GitLab CI 等负责每次提交自动执行：
lint -> type check -> unit -> integration -> packaging
""")

print("推荐学习顺序：")
print("1. 先真正理解 unittest/TestCase/mock/隔离/测试设计")
print("2. 再学 pytest，重点学 fixture 和 parametrize")
print("3. 接 coverage.py")
print("4. 有复杂输入空间时学 Hypothesis")
print("5. 最后接 CI、tox/nox、多版本矩阵")

print("\n关键点：框架会变，测试设计原则不会。")
