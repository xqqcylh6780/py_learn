"""07 基准设计：重复、隔离、代表性输入、避免 I/O 噪声。"""
import statistics, time

def benchmark(fn, repeat=7):
    samples=[]
    for _ in range(repeat):
        t=time.perf_counter(); fn(); samples.append(time.perf_counter()-t)
    return {'min': min(samples), 'median': statistics.median(samples), 'samples': samples}

print(benchmark(lambda: sum(range(10000))))
print('微基准常看 min/median，不应只跑一次就下结论。')
