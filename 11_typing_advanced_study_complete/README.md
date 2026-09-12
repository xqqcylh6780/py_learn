# 11_typing_advanced_study_complete

现代 Python 类型系统进阶课程。目标不是“把 `: int` 写满”，而是理解类型之间的关系、
让 IDE/静态检查器真正帮你发现接口错误，并知道哪些东西**只存在于静态阶段**。

## 运行环境

- 主目标：**Python 3.13**
- 课程大量使用 Python 3.12 的 PEP 695 新泛型语法
- 泛型默认参数、`TypeIs`、`ReadOnly` 等内容以 Python 3.13 为基线
- 教程本身只依赖标准库 `typing`
- `pyright` / `mypy` 属于推荐的外部静态检查器，不是运行教程的硬依赖

## 课程目录

1. 类型提示的边界与心智模型
2. 现代注解语法与运行时对象
3. Any 与 object
4. Union / None / Literal
5. `type` 语句、类型别名与 TypeAlias
6. TypeVar 与泛型函数
7. 泛型类与 PEP 695 新语法
8. bound / constraints
9. Python 3.13 泛型默认参数
10. 协变、逆变与不变
11. Self
12. Protocol 结构化子类型
13. runtime_checkable 与运行时协议
14. TypedDict 基础
15. Required / NotRequired / ReadOnly
16. Callable 与回调 Protocol
17. ParamSpec
18. Concatenate
19. overload
20. TypeVarTuple
21. Unpack + `**kwargs`
22. TypeGuard 与 TypeIs
23. 控制流类型缩窄
24. cast / assert_type / reveal_type
25. Final / ClassVar / final / override
26. NewType
27. Never / NoReturn / assert_never
28. Annotated
29. LiteralString
30. TYPE_CHECKING / 前向引用 / 循环依赖
31. dataclass_transform
32. `.pyi` / `py.typed` / mypy / pyright 工程实践

## 学习方式

```powershell
cd 11_typing_advanced_study_complete
python 01_类型提示的边界与心智模型.py
python 99_exercises.py
```

每节后做对应练习。练习册初始应为 `0/64`。

## 一个很重要的区别

这套课程同时涉及两种世界：

```text
Python runtime                 static type checker
--------------                 -------------------
真正执行代码                    在运行前分析代码
大多数注解不强制类型             检查参数/返回值/泛型关系
isinstance 等运行时行为          Protocol/variance/overload 等静态规则
```

所以仅运行 `.py` 无法验证所有类型知识。`static_cases/` 中专门放了供 pyright/mypy 检查的例子，
其中 `02_intentional_errors.py`、`03_protocol_demo.py` 故意包含静态错误。

## 推荐检查器

二选一即可：

```powershell
pyright 11_typing_advanced_study_complete
# 或
mypy 11_typing_advanced_study_complete
```

不要同时为了两个检查器的所有非标准扩展写代码；项目应固定一个主检查器及其版本/配置。

## 学完应能回答

- `Any` 和 `object` 到底差在哪？
- 泛型为什么比 `Any` 精确？
- bound 与 constraints 有何区别？
- `list[Cat]` 为什么不能安全地当 `list[Animal]`？
- `Self`、Protocol、TypedDict 分别解决什么接口问题？
- ParamSpec 为什么是类型化装饰器的关键？
- overload 和普通 `|` 联合有什么信息量差别？
- TypeGuard 与 TypeIs 如何影响控制流缩窄？
- `cast()` 为什么不能修复运行时类型错误？
- `.pyi`、`py.typed` 与库发布有什么关系？
