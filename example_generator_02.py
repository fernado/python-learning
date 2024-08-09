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
        优势：
            用好了，特别的节省内存

"""



# 去工厂定制1W件衣服

def order():
    lst = []
    for i in range(10000):
        lst.append(f"衣服{i}")
    return lst


lst = order()
print(lst)


def order_opt():
    lst = []
    for i in range(10000):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst

            lst = []


gen = order_opt()
print(gen)
# ['衣服0', '衣服1', '衣服2', '衣服3', ..'衣服49']
print(gen.__next__())
#['衣服50', '衣服51', '衣服52', '衣服53', ..'衣服99']
print(gen.__next__())