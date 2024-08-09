"""

for variable in 可迭代:
    pass

iterable: 可迭代的东西
    str, list, tuple, dict, set, open()

可迭代的数据类型都会提供一个叫迭代器的东西，这个迭代器可以帮我们把数据类型中所有数据逐一获取


获取地带器的两种方案
    1. iter() 内置函数可以直接拿到迭代器
    2. __iter__() 特殊方法

从迭代器获取数据:
    1. next() 内置函数
    2. __next__() 特殊方法
"""


it = iter("你叫什么")
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) StopIteration 迭代已经停止，不可以从迭代器获取数据


it = "来吧".__iter__()
print(it)
print(it.__next__())
print(it.__next__())