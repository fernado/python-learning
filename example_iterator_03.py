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


模拟for循环工作原理
迭代器统一了不同数据类型的遍历工作

迭代器特性：
    1. 只能向前，不能反复
    2. 特别节省内存
    3. 惰性机制

"""

s = 'a string data'
it = s.__iter__()

for mm in it:
    print(mm)

