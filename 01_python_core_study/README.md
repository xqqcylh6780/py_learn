# 01_python_core_study

这是一套面向 **Python 3.11+ / 3.13 推荐环境** 的核心语言学习包。

它不是“Hello World 入门课”，而是补齐真正写 Python 项目时必须掌握的语言语义。重点不是背语法，而是回答：

- Python 的变量到底是什么？
- 赋值、修改对象、复制对象有什么区别？
- mutable / immutable / hashable 有什么关系？
- `is`、`==`、`in` 分别在比较什么？
- 函数参数为什么会出现“外面跟着变”和“外面不变”两种情况？
- 默认参数为什么会保存上一次状态？
- `/`、`*`、`*args`、`**kwargs` 的完整规则是什么？
- LEGB、`global`、`nonlocal`、闭包之间有什么关系？
- 为什么循环里的 lambda 经常全部得到最后一个值？
- `match/case` 为什么不是简单的 switch？
- 什么情况下应该用推导式、生成器表达式、`enumerate`、`zip`？
- Unicode 文本和 bytes 为什么不能混为一谈？
- 浮点数为什么不能简单认为是十进制精确值？

## 目录

| # | 文件 | 核心内容 |
|---:|---|---|
| 01 | `01_名字对象与引用.py` | 名字绑定、对象身份、共享引用、重新绑定 |
| 02 | `02_类型可变性与可哈希性.py` | mutable / immutable / hashable |
| 03 | `03_数值模型与精度.py` | int、float、`/`、`//`、`%`、浮点误差 |
| 04 | `04_字符串Unicode与bytes.py` | Unicode、UTF-8、encode/decode、str/bytes |
| 05 | `05_序列list_tuple_range与切片.py` | list、tuple、range、切片、二维列表陷阱 |
| 06 | `06_dict与set核心语义.py` | dict、set、哈希键、集合运算、字典合并 |
| 07 | `07_真值None与短路逻辑.py` | truthiness、None、and/or、any/all |
| 08 | `08_比较身份成员关系与链式比较.py` | `==`、`is`、`in`、链式比较 |
| 09 | `09_赋值解包星号与海象运算符.py` | 解包、星号、交换、`:=` |
| 10 | `10_if_match与结构化模式匹配.py` | if/elif、match/case、序列/映射/守卫模式 |
| 11 | `11_for_while_range_enumerate_zip.py` | 循环、range、enumerate、zip、strict |
| 12 | `12_break_continue与循环else.py` | break、continue、for/while else |
| 13 | `13_推导式与生成器表达式.py` | list/dict/set comprehension、generator expression |
| 14 | `14_函数是一等对象.py` | 高阶函数、返回函数、partial |
| 15 | `15_函数参数完整规则.py` | `/`、`*`、`*args`、`**kwargs`、参数展开 |
| 16 | `16_默认参数求值与参数传递.py` | 默认值求值时机、call-by-sharing |
| 17 | `17_LEGB_global_nonlocal与闭包.py` | 作用域、UnboundLocalError、闭包 |
| 18 | `18_lambda闭包与延迟绑定.py` | lambda、key function、late binding |
| 19 | `19_常用内置函数与排序.py` | sorted、sort、key、稳定排序、min/max、map/filter |
| 20 | `20_f字符串格式化与repr.py` | f-string、格式规格、`!r`、调试表达式 |
| 21 | `21_迭代协议基础.py` | `iter()`、`next()`、StopIteration、一次性迭代器 |
| 22 | `22_核心语法高频陷阱.py` | 10 类真实项目高频坑综合复习 |
| 23 | `23_运算符优先级与位运算.py` | 算术优先级、位运算、位掩码、条件表达式 |
| 99 | `99_exercises.py` | 52 道自动判分练习 |

## 推荐学习顺序

严格按 `01 -> 23` 即可。

每节都可以直接运行：

```powershell
python 01_名字对象与引用.py
```

学完若干节后运行练习：

```powershell
python 99_exercises.py
```

练习一开始大量 `FAIL` / `ERR` 是正常的，因为其中保留了 TODO。

## 与其他目录的边界

这套课程有意不把所有高级主题重复塞进来：

- 异常系统：放到 `04_exception_study/`
- `collections` 标准库容器：放到 `02_collections_study/`
- 描述符、元类、数据模型、上下文管理器、生成器深入：放到 `03_oop_study/`
- 线程、进程、asyncio：放到 `10_concurrency_study/`
- 模块、包、import 机制：后续 `05_module_package_study/`
- 文件与路径：后续 `06_file_io_study/`
- logging / debugging：后续单独学习包
- typing 高级部分：后续单独学习包

这样每个目录职责清楚，避免同一个知识点重复讲很多遍。

## 学完后的标准

不要以“文件看完了”为标准。至少应该能不查资料解释下面这些问题：

1. `a = b = []` 为什么可能造成共享状态？
2. 为什么 tuple 自己不可变，但里面的 list 还能变化？
3. 为什么 `(1, 2)` 能当 dict key，而 `([1], 2)` 不行？
4. 为什么 `0.1 + 0.2 == 0.3` 可能是 False？
5. `str` 与 `bytes` 的边界在哪里？
6. `[[0] * 3] * 3` 为什么会共享三行？
7. `dict.get()` 与 `dict[key]` 为什么不是同一个语义？
8. 为什么 `value or default` 可能错误处理 0？
9. `is` 与 `==` 应该分别什么时候用？
10. `for...else` 的 else 到底什么时候执行？
11. `/` 和 `*` 在函数签名里是什么意思？
12. 为什么可变默认参数会记住历史调用？
13. Python 参数传递为什么既不是简单“传值”，也不是 C++ 意义的“传引用”？
14. 什么情况会产生 `UnboundLocalError`？
15. `nonlocal` 修改的是哪一层变量？
16. 为什么 `[lambda: i for i in range(3)]` 最后经常都是 2？
17. generator expression 为什么比 list comprehension 更惰性？
18. Python 排序为什么可以依赖稳定性做多级排序？
19. 可迭代对象和迭代器是什么关系？
20. 为什么真实项目里可读性通常比“一行写完”更重要？

能解释并完成 `99_exercises.py` 的 52 题，才算这一阶段真正掌握。
