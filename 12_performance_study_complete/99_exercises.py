# -*- coding: utf-8 -*-
"""12_performance_study_complete 练习册：60 题。空白状态应为 0/60。"""

_CHECKS=[]
def check(fn):
    _CHECKS.append(fn); return fn

@check
def ex01_metric_tuple():
    """根据观测名称提取延迟、吞吐和内存指标。"""
    # TODO_01
    def selected_metrics(observations):
        pass
    assert selected_metrics({'latency': 0.2, 'errors': 1, 'memory': 64}) == ('latency', 'memory')
    assert selected_metrics({'throughput': 200}) == ('throughput',)

@check
def ex02_workflow():
    """验证测量、定位、修改、复测的先后关系。"""
    # TODO_02
    def valid_workflow(steps):
        pass
    assert valid_workflow(['baseline', 'profile', 'optimize', 'remeasure']) is True
    assert valid_workflow(['optimize', 'baseline', 'remeasure']) is False

@check
def ex03_set_lookup():
    """把列表转成适合重复成员测试的结构。"""
    xs=list(range(10))
    # TODO_03
    lookup = None
    assert isinstance(lookup,set) and 9 in lookup

@check
def ex04_complexity():
    """选择 set 平均成员测试复杂度。"""
    # TODO_04
    result = None
    assert result == 'O(1) average'

@check
def ex05_timeit_callable():
    """用 timeit.timeit 测 callable 10 次。"""
    import timeit
    f=lambda: sum(range(10))
    # TODO_05
    result = None
    assert isinstance(result,float) and result >= 0

@check
def ex06_repeat_count():
    """用 timeit.repeat 返回 3 个样本。"""
    import timeit
    # TODO_06
    result = None
    assert isinstance(result,list) and len(result)==3

@check
def ex07_perf_counter():
    """取得高精度经过时间计时器函数对象。"""
    import time
    # TODO_07
    timer = None
    assert timer is time.perf_counter

@check
def ex08_process_time():
    """取得只统计进程 CPU 时间的计时器。"""
    import time
    # TODO_08
    timer = None
    assert timer is time.process_time

@check
def ex09_profile_object():
    """创建 cProfile.Profile。"""
    import cProfile
    # TODO_09
    prof = None
    assert isinstance(prof,cProfile.Profile)

@check
def ex10_profile_runcall():
    """用 Profile.runcall 执行函数并返回结果。"""
    import cProfile
    prof=cProfile.Profile()
    def f(): return 42
    # TODO_10
    result = None
    assert result == 42

@check
def ex11_pstats():
    """从 profiler 创建 pstats.Stats。"""
    import cProfile, pstats
    p=cProfile.Profile(); p.runcall(lambda: sum(range(10)))
    # TODO_11
    stats = None
    assert isinstance(stats,pstats.Stats)

@check
def ex12_sort_cumtime():
    """按累计时间排序 Stats。"""
    import cProfile,pstats
    p=cProfile.Profile(); p.runcall(lambda: None)
    stats=pstats.Stats(p)
    # TODO_12
    result = None
    assert result is stats

@check
def ex13_median():
    """计算样本中位数。"""
    import statistics
    samples=[1,100,2,3,4]
    # TODO_13
    result = None
    assert result == 3

@check
def ex14_repeat_samples():
    """生成 5 个独立样本而不是只测一次。"""
    samples=[1,2,3,4,5]
    # TODO_14
    result = None
    assert result == len(samples) == 5

@check
def ex15_getsizeof():
    """取得对象浅层大小。"""
    import sys
    x=[1,2,3]
    # TODO_15
    result = None
    assert result == sys.getsizeof(x)

@check
def ex16_shallow_size():
    """判断 getsizeof 是否递归统计子对象。"""
    # TODO_16
    result = None
    assert result is False

@check
def ex17_outer_plus_rows():
    """统计二维列表外层+各行浅层大小。"""
    import sys
    x=[[1],[2]]
    # TODO_17
    result = None
    assert result == sys.getsizeof(x)+sum(sys.getsizeof(r) for r in x)

@check
def ex18_shared_refs():
    """共享引用是否应在“深层总大小”里无脑重复计数。"""
    # TODO_18
    result = None
    assert result is False

@check
def ex19_tracemalloc_start():
    """启动 tracemalloc。"""
    import tracemalloc
    tracemalloc.stop()
    # TODO_19
    tracemalloc.start() if False else None  # TODO
    assert tracemalloc.is_tracing()

@check
def ex20_tracemalloc_snapshot():
    """创建 tracemalloc 快照。"""
    import tracemalloc
    tracemalloc.start()
    # TODO_20
    snap = None
    assert isinstance(snap,tracemalloc.Snapshot)

@check
def ex21_getrefcount():
    """调用 CPython 引用计数观察 API。"""
    import sys
    x=[]
    # TODO_21
    result = None
    assert isinstance(result,int) and result >= 1

@check
def ex22_refcount_contract():
    """业务逻辑是否应依赖具体引用计数值。"""
    # TODO_22
    result = None
    assert result is False

@check
def ex23_gc_collect():
    """主动触发一次循环垃圾回收。"""
    import gc
    # TODO_23
    result = None
    assert isinstance(result,int)

@check
def ex24_gc_enabled():
    """检查 GC 是否启用。"""
    import gc
    # TODO_24
    result = None
    assert result == gc.isenabled()

@check
def ex25_weak_value_dict():
    """创建弱值字典。"""
    import weakref
    # TODO_25
    cache = None
    assert isinstance(cache,weakref.WeakValueDictionary)

@check
def ex26_weakref_goal():
    """弱缓存是否应阻止对象被回收。"""
    # TODO_26
    result = None
    assert result is False

@check
def ex27_dis_bytecode():
    """取得函数的字节码指令列表。"""
    import dis
    def f(x): return x+1
    # TODO_27
    result = None
    assert result and all(isinstance(i,dis.Instruction) for i in result)

@check
def ex28_bytecode_spec():
    """CPython 字节码是否属于稳定语言规范。"""
    # TODO_28
    result = None
    assert result is False

@check
def ex29_call_hotspot():
    """只有热点占比和调用规模都足够时才考虑调用级微优化。"""
    # TODO_29
    def worth_micro_optimizing(profile_share, calls):
        pass
    assert worth_micro_optimizing(0.45, 2_000_000) is True
    assert worth_micro_optimizing(0.01, 2_000_000) is False
    assert worth_micro_optimizing(0.45, 20) is False

@check
def ex30_abstraction_tradeoff():
    """普通非热点业务代码应优先可维护性。"""
    # TODO_30
    result = None
    assert result == 'maintainability'

@check
def ex31_deque():
    """创建适合两端队列操作的数据结构。"""
    from collections import deque
    # TODO_31
    q = None
    assert isinstance(q,deque)

@check
def ex32_membership_structure():
    """大量重复成员测试优先的数据结构。"""
    values=range(10)
    # TODO_32
    lookup = None
    assert isinstance(lookup,set)

@check
def ex33_join():
    """把字符串片段高效组合。"""
    parts=["a","b","c"]
    # TODO_33
    result = None
    assert result == 'abc'

@check
def ex34_plus_rule():
    """根据片段数量选择直接拼接或 join。"""
    # TODO_34
    def combine(parts):
        pass
    assert combine(['a', 'b']) == 'ab'
    assert combine(['a', 'b', 'c', 'd']) == 'abcd'

@check
def ex35_generator():
    """创建惰性平方生成器。"""
    # TODO_35
    g = None
    assert g is not None and iter(g) is g and list(g)==[0,1,4]

@check
def ex36_list_when_reuse():
    """需要反复遍历结果时，可物化成 list。"""
    # TODO_36
    result = None
    assert result == [0,1,4]

@check
def ex37_local_alias():
    """把全局函数绑定到局部名字。"""
    import math
    # TODO_37
    sqrt = None
    assert sqrt is math.sqrt

@check
def ex38_lookup_measure():
    """只有测量结果超过噪声区间时才接受局部改写。"""
    # TODO_38
    def meaningful_improvement(before, after, noise_ratio=0.03):
        pass
    assert meaningful_improvement(1.0, 0.8) is True
    assert meaningful_improvement(1.0, 0.99) is False
    assert meaningful_improvement(1.0, 1.1) is False

@check
def ex39_lru_cache():
    """创建有界 LRU 缓存装饰器后的函数。"""
    from functools import lru_cache
    def f(x): return x*x
    # TODO_39
    cached = None
    assert cached is not None and cached(3)==9 and hasattr(cached,'cache_info')

@check
def ex40_cache_clear():
    """清空 lru_cache。"""
    from functools import lru_cache
    @lru_cache(maxsize=4)
    def f(x): return x
    f(1)
    # TODO_40
    result = None
    assert result is None and f.cache_info().currsize==0

@check
def ex41_slots():
    """定义 slots 类。"""
    # TODO_41
    class Item:
            pass  # TODO
    assert hasattr(Item,'__slots__')

@check
def ex42_slots_rule():
    """根据实例规模和动态属性需求判断 slots 是否值得评估。"""
    # TODO_42
    def slots_candidate(instance_count, needs_dynamic_attributes):
        pass
    assert slots_candidate(1_000_000, False) is True
    assert slots_candidate(10, False) is False
    assert slots_candidate(1_000_000, True) is False

@check
def ex43_list_comp():
    """已知要全部结果时用列表推导式。"""
    # TODO_43
    result = None
    assert result == [0,1,4,9]

@check
def ex44_prealloc_rule():
    """Python list 是否需要像 C 数组一样总是手工预分配。"""
    # TODO_44
    result = None
    assert result is False

@check
def ex45_stringio():
    """创建内存文本流。"""
    import io
    # TODO_45
    buf = None
    assert isinstance(buf,io.StringIO)

@check
def ex46_batching():
    """计算批处理后的往返次数。"""
    # TODO_46
    def round_trips(item_count, batch_size):
        pass
    assert round_trips(100, 20) == 5
    assert round_trips(101, 20) == 6
    assert round_trips(0, 20) == 0

@check
def ex47_pickle_size():
    """得到 pickle 序列化字节长度。"""
    import pickle
    obj=list(range(20))
    # TODO_47
    result = None
    assert result == len(pickle.dumps(obj))

@check
def ex48_serialization_tradeoff():
    """根据互操作和输入信任边界选择示例格式。"""
    # TODO_48
    def choose_format(cross_language, trusted_python_only):
        pass
    assert choose_format(True, False) == 'json'
    assert choose_format(False, True) == 'pickle'
    assert choose_format(False, False) == 'json'

@check
def ex49_cpu_strategy():
    """按任务性质选择并发模型的起点。"""
    # TODO_49
    def strategy(task_kind, async_library=False):
        pass
    assert strategy('cpu') == 'processes'
    assert strategy('io', async_library=True) == 'asyncio'
    assert strategy('io', async_library=False) == 'threads'

@check
def ex50_io_strategy():
    """大量 I/O 等待是否适合并发隐藏等待。"""
    # TODO_50
    result = None
    assert result is True

@check
def ex51_pickle_payload():
    """模拟多进程 IPC 序列化。"""
    import pickle
    x=list(range(10))
    # TODO_51
    blob = None
    assert isinstance(blob,bytes) and pickle.loads(blob)==x

@check
def ex52_task_granularity():
    """比较计算收益与调度、序列化成本。"""
    # TODO_52
    def worth_process_pool(compute_ms, overhead_ms):
        pass
    assert worth_process_pool(500, 20) is True
    assert worth_process_pool(5, 20) is False

@check
def ex53_gather():
    """并发等待两个 async 任务。"""
    import asyncio
    async def f(x):
        await asyncio.sleep(0)
        return x
    # TODO_53
    async def run():
            return None  # TODO
    result = asyncio.run(run())
    assert result == [1,2]

@check
def ex54_async_cpu():
    """asyncio 是否自动让纯 CPU 函数获得多核加速。"""
    # TODO_54
    result = None
    assert result is False

@check
def ex55_median_regression():
    """比较两个中位数。"""
    import statistics
    a=[1,1,1]; b=[2,2,2]
    # TODO_55
    result = None
    assert result is True

@check
def ex56_ci_noise():
    """用中位数和容忍比例判断性能回归。"""
    # TODO_56
    def regressed(baseline, current, tolerance=0.10):
        pass
    assert regressed([1.0, 1.1, 0.9], [1.3, 1.2, 1.4]) is True
    assert regressed([1.0, 1.1, 0.9], [1.02, 1.05, 0.98]) is False

@check
def ex57_snapshot_diff():
    """比较两个 tracemalloc 快照。"""
    import tracemalloc
    tracemalloc.start(); a=tracemalloc.take_snapshot(); x=[str(i) for i in range(20)]; b=tracemalloc.take_snapshot()
    # TODO_57
    result = None
    assert isinstance(result,list)

@check
def ex58_leak_first_question():
    """区分稳定缓存与持续增长的保留对象。"""
    # TODO_58
    def keeps_growing(samples):
        pass
    assert keeps_growing([100, 120, 140, 160]) is True
    assert keeps_growing([100, 140, 138, 141]) is False

@check
def ex59_priority():
    """优化优先级通常先考虑算法/数据结构还是纳秒微优化。"""
    # TODO_59
    result = None
    assert result == 'algorithm/data-structure'

@check
def ex60_remeasure():
    """复测改善并同时检查行为测试。"""
    # TODO_60
    def optimization_accepted(baseline, current, tests_pass):
        pass
    assert optimization_accepted(10.0, 7.0, True) is True
    assert optimization_accepted(10.0, 7.0, False) is False
    assert optimization_accepted(10.0, 10.5, True) is False

def run_all():
    passed=0; errs=0
    print('='*64); print('12_performance_study_complete 练习册'); print('='*64)
    for fn in _CHECKS:
        try:
            fn()
        except AssertionError:
            print(f'[FAIL] {fn.__name__}')
        except Exception as e:
            errs += 1
            print(f'[ERR ] {fn.__name__}: {type(e).__name__}: {e}')
        else:
            passed += 1
            print(f'[ OK ] {fn.__name__}')
    print('-'*64)
    print(f'通过 {passed}/{len(_CHECKS)}')
    print(f'ERR={errs}')
    return passed, errs

if __name__ == '__main__':
    run_all()

# ====================== 参考答案 ======================
# TODO_01
# return tuple(name for name in ('latency','throughput','memory') if name in observations)
#
# TODO_02
# return steps == ['baseline','profile','optimize','remeasure']
#
# TODO_03
# lookup = set(xs)
#
# TODO_04
# result = 'O(1) average'
#
# TODO_05
# result = timeit.timeit(f, number=10)
#
# TODO_06
# result = timeit.repeat('1+1', repeat=3, number=10)
#
# TODO_07
# timer = time.perf_counter
#
# TODO_08
# timer = time.process_time
#
# TODO_09
# prof = cProfile.Profile()
#
# TODO_10
# result = prof.runcall(f)
#
# TODO_11
# stats = pstats.Stats(p)
#
# TODO_12
# result = stats.sort_stats('cumtime')
#
# TODO_13
# result = statistics.median(samples)
#
# TODO_14
# result = len(samples)
#
# TODO_15
# result = sys.getsizeof(x)
#
# TODO_16
# result = False
#
# TODO_17
# result = sys.getsizeof(x)+sum(sys.getsizeof(r) for r in x)
#
# TODO_18
# result = False
#
# TODO_19
# tracemalloc.start()
#
# TODO_20
# snap = tracemalloc.take_snapshot()
#
# TODO_21
# result = sys.getrefcount(x)
#
# TODO_22
# result = False
#
# TODO_23
# result = gc.collect()
#
# TODO_24
# result = gc.isenabled()
#
# TODO_25
# cache = weakref.WeakValueDictionary()
#
# TODO_26
# result = False
#
# TODO_27
# result = list(dis.get_instructions(f))
#
# TODO_28
# result = False
#
# TODO_29
# return profile_share >= 0.10 and calls >= 10_000
#
# TODO_30
# result = 'maintainability'
#
# TODO_31
# q = deque()
#
# TODO_32
# lookup = set(values)
#
# TODO_33
# result = ''.join(parts)
#
# TODO_34
# return parts[0] + parts[1] if len(parts) == 2 else ''.join(parts)
#
# TODO_35
# g = (x*x for x in range(3))
#
# TODO_36
# result = [x*x for x in range(3)]
#
# TODO_37
# sqrt = math.sqrt
#
# TODO_38
# return after < before * (1 - noise_ratio)
#
# TODO_39
# cached = lru_cache(maxsize=8)(f)
#
# TODO_40
# result = f.cache_clear()
#
# TODO_41
# class Item:
#         __slots__ = ('x',)
#
# TODO_42
# return instance_count >= 10_000 and not needs_dynamic_attributes
#
# TODO_43
# result = [x*x for x in range(4)]
#
# TODO_44
# result = False
#
# TODO_45
# buf = io.StringIO()
#
# TODO_46
# if batch_size <= 0: raise ValueError('batch_size must be positive')
# return (item_count + batch_size - 1) // batch_size
#
# TODO_47
# result = len(pickle.dumps(obj))
#
# TODO_48
# return 'pickle' if trusted_python_only and not cross_language else 'json'
#
# TODO_49
# if task_kind == 'cpu': return 'processes'
# return 'asyncio' if async_library else 'threads'
#
# TODO_50
# result = True
#
# TODO_51
# blob = pickle.dumps(x)
#
# TODO_52
# return compute_ms > overhead_ms
#
# TODO_53
# async def run():
#         return await asyncio.gather(f(1), f(2))
# result = asyncio.run(run())
#
# TODO_54
# result = False
#
# TODO_55
# result = statistics.median(b) > statistics.median(a)
#
# TODO_56
# import statistics
# return statistics.median(current) > statistics.median(baseline) * (1 + tolerance)
#
# TODO_57
# result = b.compare_to(a, 'lineno')
#
# TODO_58
# return len(samples) >= 3 and all(b > a for a, b in zip(samples, samples[1:]))
#
# TODO_59
# result = 'algorithm/data-structure'
#
# TODO_60
# return tests_pass and current < baseline
#
