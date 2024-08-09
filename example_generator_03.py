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



推导式：
    简化代码
    语法：
        列表推导式： [数据 for 循环 if 判断]
        集合推导式： {数据 for 循环 if 判断}
        字典推导式： {k:v for 循环 if 判断}

    不要把推导式妖魔化
    元组没有推导式
    (数据 for 循环 if 判断) ====> 这种不叫元组推导式，其叫做生成器表达式


"""


lst = []
for i in range(10):
    lst.append(i)


print(lst)

# 列表推导式
lst = [i for i in range(10)]
print(lst)

# 创建一个列表[1,3,5,7,9]
lst = [i for i in range(1, 10, 2)]
print(lst)

lst = [i for i in range(10) if i % 2 == 1]
print(lst)

# 生成50件衣服
lst = [f"衣服{i}" for i in range(50)]
print(lst)

# 将如下列表中所有的英文字母改成大写
lst1 = ["allen", "tony", "kevin"]
lst2 = [item.upper() for item in lst1]
print(lst2)

# 集合推导式
s = {i for i in range(10)}
print(s)

# 请将下列的列表修改成字典，要求索引作为key, 数据作为value

lst = ['周星驰', "许巍", "刘德华"]
dct = {i:lst[i] for i in range(len(lst))}
print(dct)

