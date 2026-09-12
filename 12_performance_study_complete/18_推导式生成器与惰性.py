"""18 列表推导式 vs 生成器：主要区别常常是内存与惰性，不是“谁永远更快”。"""
import sys
lst=[x*x for x in range(10000)]
gen=(x*x for x in range(10000))
print('list shallow bytes:', sys.getsizeof(lst))
print('generator bytes   :', sys.getsizeof(gen))
print('如果结果要反复使用，列表可能更合适；只流式消费一次时生成器可省内存。')
