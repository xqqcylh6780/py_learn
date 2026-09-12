"""26 多进程不是免费并行：任务太小可能越并行越慢。"""
import pickle
payload=list(range(10000))
blob=pickle.dumps(payload)
print('传输前序列化大小:', len(blob), 'bytes')
print('要考虑：进程启动、pickle、管道/队列、上下文切换、结果汇总。')
print('实践中应增大任务粒度、批处理，并避免反复传巨大对象。')
