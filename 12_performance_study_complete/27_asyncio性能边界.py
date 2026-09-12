"""27 asyncio：优势是高并发 I/O 的调度模型，不是让 CPU 计算变快。"""
import asyncio, time
async def job(i):
    await asyncio.sleep(0.01)
    return i
async def main():
    t=time.perf_counter(); r=await asyncio.gather(*(job(i) for i in range(20)))
    print(len(r), 'elapsed:', time.perf_counter()-t)
asyncio.run(main())
print('仍要限制并发数，避免连接、内存、服务端容量被压垮。')
