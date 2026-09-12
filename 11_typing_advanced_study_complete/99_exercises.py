# -*- coding: utf-8 -*-
"""11_typing_advanced_study_complete 自动练习册：64 题

运行：python 99_exercises.py
初始应为 0/64。参考答案在文件最底部（纯注释）。
注意：静态类型系统的一部分能力只有 pyright/mypy 才能完整验证；本练习册尽量用运行时
反射 + 行为测试验证你填写的类型对象/声明结构，static_cases/ 则用于真正静态检查。
"""
import inspect
import typing
from collections.abc import Callable
from typing import (
    Any, Annotated, ClassVar, Final, Literal, LiteralString, NewType, Never,
    NoReturn, NotRequired, Protocol, ReadOnly, Required, Self, TypedDict,
    TypeGuard, TypeIs, TypeVar, Unpack, assert_never, dataclass_transform,
    get_args, get_origin, get_overloads, get_type_hints, overload, runtime_checkable,
)

_checks = []
def check(fn):
    _checks.append(fn); return fn

def fail_if(value, bad=None):
    assert value != bad

# 01-04 基础
@check
def ex01_annotation_not_runtime_check():
    def f(x: int) -> int: return x
    result = None  # TODO: 调用 f('x')，证明运行时不会因注解自动拒绝
    assert result == 'x'

@check
def ex02_modern_list_annotation():
    annotation = None  # TODO: list[int]
    assert get_origin(annotation) is list and get_args(annotation) == (int,)

@check
def ex03_any_annotation():
    annotation = None  # TODO: Any
    assert annotation is Any

@check
def ex04_object_annotation():
    annotation = None  # TODO: object
    assert annotation is object

@check
def ex05_optional_union():
    annotation = None  # TODO: int | None
    assert set(get_args(annotation)) == {int, type(None)}

@check
def ex06_literal_modes():
    annotation = None  # TODO: Literal['r', 'w']
    assert get_origin(annotation) is Literal and get_args(annotation) == ('r','w')

@check
def ex07_type_alias_statement():
    # TODO: 用 type 语句把 Pair 定义成 tuple[int, int]
    type Pair = None
    assert isinstance(Pair, typing.TypeAliasType)
    assert Pair.__value__ == tuple[int, int]

@check
def ex08_generic_type_alias():
    # TODO: type Pair[T] = tuple[T, T]
    type Pair = tuple[object, object]
    assert len(Pair.__type_params__) == 1
    assert get_args(Pair[int]) == (int,)

# 05-08 泛型基础
@check
def ex09_generic_identity():
    # TODO: 改成 def identity[T](x: T) -> T
    def identity(x: object) -> object: return x
    assert len(getattr(identity, '__type_params__', ())) == 1
    hints = identity.__annotations__
    t = identity.__type_params__[0]
    assert hints['x'] is t and hints['return'] is t

@check
def ex10_generic_first_behavior():
    def first[T](xs: list[T]) -> T: return xs[0]
    result = None  # TODO: first(['a','b'])
    assert result == 'a'

@check
def ex11_generic_class():
    # TODO: class Box[T]，构造器保存 value，get 返回 value
    class Box:
        def __init__(self, value): self.value = value
        def get(self): return self.value
    assert len(getattr(Box, '__type_params__', ())) == 1
    assert Box[int](3).get() == 3

@check
def ex12_bound_typevar():
    class Animal: pass
    # TODO: TypeVar('A', bound=Animal)
    A = TypeVar('A')
    assert A.__bound__ is Animal

@check
def ex13_constrained_typevar():
    # TODO: TypeVar('Text', str, bytes)
    Text = TypeVar('Text')
    assert Text.__constraints__ == (str, bytes)

@check
def ex14_default_type_parameter():
    # TODO: class Box[T = str]
    class Box[T]: pass
    t = Box.__type_params__[0]
    assert t.has_default() and t.__default__ is str

@check
def ex15_generic_default_alias():
    # TODO: type Cache[K = str, V = object] = dict[K, V]
    type Cache[K, V] = dict[K, V]
    ks = Cache.__type_params__
    assert ks[0].has_default() and ks[0].__default__ is str
    assert ks[1].has_default() and ks[1].__default__ is object

@check
def ex16_sequence_covariance_idea():
    from collections.abc import Sequence
    annotation = None  # TODO: Sequence[str]
    assert get_origin(annotation) is Sequence and get_args(annotation) == (str,)

# 09-12 Self/Protocol
@check
def ex17_self_annotation():
    class Builder:
        def add(self, x: str) -> None:  # TODO: return Self
            return self
    assert Builder.add.__annotations__.get('return') is Self

@check
def ex18_self_chain_behavior():
    class B:
        def add(self, x: int) -> Self: return self
    result = None  # TODO: B().add(1).add(2)
    assert isinstance(result, B)

@check
def ex19_protocol_definition():
    # TODO: 让 Closable 成为 Protocol
    class Closable:
        def close(self) -> None: ...
    assert typing.is_protocol(Closable)

@check
def ex20_protocol_structural_use():
    class P(Protocol):
        def ping(self) -> str: ...
    class X:
        def ping(self) -> str: return 'pong'
    obj = None  # TODO: X()
    assert obj is not None
    assert obj.ping() == 'pong'

@check
def ex21_runtime_checkable():
    # TODO: 加 @runtime_checkable
    class HasName(Protocol):
        name: str
    class X: name = 'x'
    assert getattr(HasName, '_is_runtime_protocol', False) is True
    assert isinstance(X(), HasName)

@check
def ex22_protocol_members():
    class P(Protocol):
        x: int
        def run(self) -> None: ...
    result = None  # TODO: typing.get_protocol_members(P)
    assert result == frozenset({'x','run'})

@check
def ex23_runtime_protocol_is_shallow():
    @runtime_checkable
    class P(Protocol):
        def run(self, x: int) -> int: ...
    class Wrong:
        def run(self): return 'wrong'
    result = None  # TODO: isinstance(Wrong(), P)
    assert result is True

@check
def ex24_protocol_call_method():
    class Writer(Protocol):
        def write(self, s: str) -> int: ...
    class W:
        def write(self, s: str) -> int: return len(s)
    def use(w: Writer) -> int: return w.write('abc')
    result = None  # TODO: use(W())
    assert result == 3

# 13-16 TypedDict/Callable
@check
def ex25_typed_dict_required():
    class Row(TypedDict):
        id: int
        name: str
    result = None  # TODO: Row.__required_keys__
    assert result == frozenset({'id','name'})

@check
def ex26_typed_dict_runtime_dict():
    class Row(TypedDict): id: int
    value = None  # TODO: {'id': 1}，注解可写 value: Row
    assert type(value) is dict and value == {'id':1}

@check
def ex27_notrequired():
    class C(TypedDict):
        host: str
        token: str  # TODO: 改成 NotRequired[str]
    assert 'token' in C.__optional_keys__ and 'host' in C.__required_keys__

@check
def ex28_required_total_false():
    class C(TypedDict, total=False):
        host: str  # TODO: Required[str]
        port: int
    assert C.__required_keys__ == frozenset({'host'})
    assert C.__optional_keys__ == frozenset({'port'})

@check
def ex29_readonly_key():
    class C(TypedDict):
        version: int  # TODO: ReadOnly[int]
    ann = C.__annotations__['version']
    assert get_origin(ann) is ReadOnly and get_args(ann) == (int,)

@check
def ex30_callable_annotation():
    annotation = None  # TODO: Callable[[int, int], int]
    assert get_origin(annotation) in (Callable, typing.Callable)
    args = get_args(annotation)
    assert args[-1] is int

@check
def ex31_callback_protocol():
    # TODO: 让 F 成 Protocol，并声明 __call__(x:int, *, prefix:str='')->str
    class F:
        pass
    assert typing.is_protocol(F)
    assert '__call__' in typing.get_protocol_members(F)

@check
def ex32_callable_behavior():
    def apply(fn: Callable[[int], int], x: int) -> int: return fn(x)
    result = None  # TODO: apply(lambda x: x*3, 4)
    assert result == 12

# 17-20 ParamSpec/overload/variadics
@check
def ex33_paramspec():
    P = None  # TODO: typing.ParamSpec('P')
    assert isinstance(P, typing.ParamSpec)

@check
def ex34_paramspec_wrapper():
    P = typing.ParamSpec('P'); R = TypeVar('R')
    def deco(fn: Callable[P, R]) -> Callable[P, R]:
        def wrap(*args: P.args, **kwargs: P.kwargs) -> R: return fn(*args, **kwargs)
        return wrap
    @deco
    def add(a:int,b:int)->int:return a+b
    result = None  # TODO: add(2,3)
    assert result == 5

@check
def ex35_concatenate():
    P = typing.ParamSpec('P')
    annotation = None  # TODO: Callable[typing.Concatenate[int, P], str]
    assert get_origin(annotation) in (Callable, typing.Callable)
    params, ret = get_args(annotation)
    assert get_origin(params) is typing.Concatenate
    assert get_args(params) == (int, P) and ret is str

@check
def ex36_overload_count():
    @overload
    def f(x:int)->int: ...
    @overload
    def f(x:str)->str: ...
    def f(x): return x
    result = None  # TODO: len(get_overloads(f))
    assert result == 2

@check
def ex37_overload_runtime_impl():
    @overload
    def f(x:int)->int: ...
    @overload
    def f(x:str)->str: ...
    def f(x): return x
    result = None  # TODO: f('x')
    assert result == 'x'

@check
def ex38_typevartuple():
    Ts = None  # TODO: typing.TypeVarTuple('Ts')
    assert isinstance(Ts, typing.TypeVarTuple)

@check
def ex39_variadic_generic_function():
    # TODO: def ident[*Ts](x: tuple[*Ts]) -> tuple[*Ts]
    def ident(x: tuple[object, ...]) -> tuple[object, ...]: return x
    assert len(getattr(ident,'__type_params__',())) == 1
    assert isinstance(ident.__type_params__[0], typing.TypeVarTuple)

@check
def ex40_unpack_tuple_annotation():
    Ts = typing.TypeVarTuple('Ts')
    annotation = None  # TODO: tuple[Unpack[Ts]]
    assert get_origin(annotation) is tuple
    assert get_origin(get_args(annotation)[0]) is Unpack

# 21-24 kwargs / narrowing / directives
@check
def ex41_unpack_kwargs():
    class Opt(TypedDict, total=False): timeout: float
    ann = None  # TODO: Unpack[Opt]
    assert get_origin(ann) is Unpack and get_args(ann) == (Opt,)

@check
def ex42_kwargs_behavior():
    class Opt(TypedDict, total=False): retries: int
    def f(**kwargs: Unpack[Opt]): return kwargs
    result = None  # TODO: f(retries=3)
    assert result == {'retries':3}

@check
def ex43_typeguard_annotation():
    def p(xs:list[object]) -> bool:  # TODO: -> TypeGuard[list[str]]
        return all(isinstance(x,str) for x in xs)
    ann = p.__annotations__['return']
    assert get_origin(ann) is TypeGuard and get_args(ann) == (list[str],)

@check
def ex44_typeis_annotation():
    def p(x:object) -> bool:  # TODO: -> TypeIs[str]
        return isinstance(x,str)
    ann = p.__annotations__['return']
    assert get_origin(ann) is TypeIs and get_args(ann) == (str,)

@check
def ex45_narrow_isinstance():
    def upper(x: object) -> str:
        # TODO: isinstance 缩窄；不是 str 返回 repr(x)
        return ''
    assert upper('abc') == 'ABC' and upper(12) == '12'

@check
def ex46_cast_does_not_convert():
    obj: object = 'x'
    value = None  # TODO: typing.cast(str, obj)
    assert value is obj and type(value) is str

@check
def ex47_assert_type_runtime_identity():
    x = [1,2]
    y = None  # TODO: typing.assert_type(x, list[int])
    assert y is x

@check
def ex48_get_type_hints():
    def f(x:int)->str:return str(x)
    result = None  # TODO: get_type_hints(f)
    assert result == {'x':int,'return':str}

# 25-28 qualifiers / NewType / Never / Annotated
@check
def ex49_final_annotation():
    annotation = None  # TODO: Final[int]
    assert get_origin(annotation) is Final and get_args(annotation) == (int,)

@check
def ex50_classvar_annotation():
    annotation = None  # TODO: ClassVar[str]
    assert get_origin(annotation) is ClassVar and get_args(annotation) == (str,)

@check
def ex51_override_decorator():
    class B:
        def run(self)->str:return 'b'
    class C(B):
        # TODO: 在 run 上添加 @typing.override
        def run(self)->str:return 'c'
    assert getattr(C.run, '__override__', False) is True

@check
def ex52_newtype():
    UserId = None  # TODO: NewType('UserId', int)
    assert isinstance(UserId, typing.NewType)
    assert UserId.__supertype__ is int and UserId(3) == 3

@check
def ex53_never_annotation():
    annotation = None  # TODO: Never
    assert annotation is Never

@check
def ex54_noreturn_annotation():
    annotation = None  # TODO: NoReturn
    assert annotation is NoReturn

@check
def ex55_annotated():
    annotation = None  # TODO: Annotated[int, 'positive']
    assert get_origin(annotation) is Annotated
    assert get_args(annotation) == (int,'positive')

@check
def ex56_assert_never_unreachable():
    def f(x: Literal['a']) -> str:
        if x == 'a': return 'A'
        assert_never(x)
    result = None  # TODO: f('a')
    assert result == 'A'

# 29-32 工程边界
@check
def ex57_literalstring():
    annotation = None  # TODO: LiteralString
    assert annotation is LiteralString

@check
def ex58_type_checking_runtime():
    result = None  # TODO: typing.TYPE_CHECKING
    assert result is False

@check
def ex59_forward_reference():
    class Node:
        def __init__(self, parent: 'Node | None' = None): self.parent=parent
    hints = None  # TODO: get_type_hints(Node.__init__, localns={'Node': Node})
    assert hints is not None
    assert set(get_args(hints['parent'])) == {Node, type(None)}

@check
def ex60_dataclass_transform():
    @dataclass_transform()
    def model(cls): return cls
    result = None  # TODO: getattr(model, '__dataclass_transform__', None)
    assert isinstance(result, dict)

@check
def ex61_type_params_introspection():
    def f[T](x:T)->T:return x
    result = None  # TODO: f.__type_params__
    assert result is not None
    assert len(result)==1 and isinstance(result[0], TypeVar)

@check
def ex62_typealiastype_runtime():
    type UserIds = list[int]
    result = None  # TODO: isinstance(UserIds, typing.TypeAliasType)
    assert result is True

@check
def ex63_no_default_sentinel():
    T = TypeVar('T')
    result = None  # TODO: T.__default__
    assert result is typing.NoDefault

@check
def ex64_type_parameter_default():
    T = TypeVar('T', default=str)
    result = None  # TODO: T.has_default()
    assert result is True and T.__default__ is str


def run_all():
    print('='*68)
    print('11_typing_advanced_study_complete - 64 道练习')
    print('='*68)
    passed=failed=errors=0
    for fn in _checks:
        try:
            fn()
        except AssertionError as e:
            failed += 1; print(f'[FAIL] {fn.__name__:<34} {e}')
        except Exception as e:
            errors += 1; print(f'[ERR ] {fn.__name__:<34} {type(e).__name__}: {e}')
        else:
            passed += 1; print(f'[ OK ] {fn.__name__:<34}')
    print('-'*68)
    print(f'通过 {passed}/{len(_checks)} | FAIL={failed} | ERR={errors}')
    return passed, failed, errors

if __name__ == '__main__':
    run_all()

# ============================================================================
# 参考答案（纯注释；建议先自己完成）
# ============================================================================
# ex01: result = f('x')
# ex02: annotation = list[int]
# ex03: annotation = Any
# ex04: annotation = object
# ex05: annotation = int | None
# ex06: annotation = Literal['r', 'w']
# ex07: type Pair = tuple[int, int]
# ex08: type Pair[T] = tuple[T, T]
# ex09: def identity[T](x: T) -> T: return x
# ex10: result = first(['a','b'])
# ex11: class Box[T]: ...（__init__ 保存 value；get()->T）
# ex12: A = TypeVar('A', bound=Animal)
# ex13: Text = TypeVar('Text', str, bytes)
# ex14: class Box[T = str]: pass
# ex15: type Cache[K = str, V = object] = dict[K, V]
# ex16: annotation = Sequence[str]
# ex17: def add(self, x: str) -> Self: return self
# ex18: result = B().add(1).add(2)
# ex19: class Closable(Protocol): ...
# ex20: obj = X()
# ex21: @runtime_checkable 放在 HasName 上
# ex22: result = typing.get_protocol_members(P)
# ex23: result = isinstance(Wrong(), P)
# ex24: result = use(W())
# ex25: result = Row.__required_keys__
# ex26: value: Row = {'id': 1}
# ex27: token: NotRequired[str]
# ex28: host: Required[str]
# ex29: version: ReadOnly[int]
# ex30: annotation = Callable[[int, int], int]
# ex31: class F(Protocol): def __call__(self, x:int, *, prefix:str='')->str: ...
# ex32: result = apply(lambda x: x*3, 4)
# ex33: P = typing.ParamSpec('P')
# ex34: result = add(2,3)
# ex35: annotation = Callable[typing.Concatenate[int, P], str]
# ex36: result = len(get_overloads(f))
# ex37: result = f('x')
# ex38: Ts = typing.TypeVarTuple('Ts')
# ex39: def ident[*Ts](x: tuple[*Ts]) -> tuple[*Ts]: return x
# ex40: annotation = tuple[Unpack[Ts]]
# ex41: ann = Unpack[Opt]
# ex42: result = f(retries=3)
# ex43: -> TypeGuard[list[str]]
# ex44: -> TypeIs[str]
# ex45: if isinstance(x,str): return x.upper(); return repr(x)
# ex46: value = typing.cast(str, obj)
# ex47: y = typing.assert_type(x, list[int])
# ex48: result = get_type_hints(f)
# ex49: annotation = Final[int]
# ex50: annotation = ClassVar[str]
# ex51: 在 C.run 上添加 @typing.override
# ex52: UserId = NewType('UserId', int)
# ex53: annotation = Never
# ex54: annotation = NoReturn
# ex55: annotation = Annotated[int, 'positive']
# ex56: result = f('a')
# ex57: annotation = LiteralString
# ex58: result = typing.TYPE_CHECKING
# ex59: hints = get_type_hints(Node.__init__, localns={'Node': Node})
# ex60: result = getattr(model, '__dataclass_transform__', None)
# ex61: result = f.__type_params__
# ex62: result = isinstance(UserIds, typing.TypeAliasType)
# ex63: result = T.__default__
# ex64: result = T.has_default()
