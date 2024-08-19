"""

匿名函数：
    lambda表达式
    语法:
        变量 = lambda 参数，参数2，参数3...: 返回值
"""


def func():
    print(1234)
    return 999


ret = func()
print(ret)

################################


def add(a, b):
    return a + b


ret = add(1, 2)
print(ret)

################################

# <function <lambda> at 0x0102A778>
fn_add = lambda a, b: a + b
print(fn_add)
ret = fn_add(5, 2)
print(ret)
