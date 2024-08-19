"""
生成器：
    生成器的本质是迭代器

    创建生成器的两种方案：
        1. 生成器函数
        2. 生成器表达式

    生成器函数
        生成器函数中有一个关键字yield
        生蹭墙函数执行的时候，并不会执行函数，得到的是生成器

        yield: 只要函数中出现了yield，它就是一个生成器函数
            作用：
                1. 可以返回数据
                2. 可以分段的执行函数中的内容，通过__next__()可以执行到下一个yield

"""


def func():
    print(1234)
    return 99

ret = func()
print(ret)

def func2():
    print(12345)
    yield 999 # yield 也有返回的意思

ret = func2()
print(ret) # <generator object func2 at 0x012D7418>
print(ret.__next__())  # yield只有执行next的时候才会返回数据


def func3():
    print(1234)
    yield 6666
    print(4567)
    yield 9999

ret = func3()
# 1234
# 6666
print(ret.__next__())
# 4567
# 9999
print(ret.__next__())