"""
1. 函数可以作为参数传递
2. 函数可以作为返回值进行返回
3. 函数名称可以当初变量一样进行赋值操作
"""


# 1. 函数可以作为参数传递
def func():
    print("""I'm a function""")

def func2(fn):
    fn()

func2(func)


# 2. 函数可以作为返回值进行返回
def func3():
    def inner():
        print(123)
    return inner


ret = func3()
ret()

# 3. 函数名称可以当初变量一样进行赋值操作
def func3():
    print("""I'm a function3""")

def func4():
    print("""I'm a function4""")

func3 = func4
func3()