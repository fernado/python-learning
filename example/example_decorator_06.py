"""
装饰器：本质上是一个闭包
    作用： 在不改变原有函数调用的情况下，给函数增加新的功能。
    直白：可以在函数前后添加新功能，但是不改变代码。

    在哪些地方使用：
        在用户登录的地方，日志，

    通用装饰器的写法：
        def wrapper(fn):   wrapper: 装饰器, fn: 目标函数
            def inner(*args, **kwargs):
                # 在目标函数执行之前...
                ret = fn(*args, **kwargs)
                # 在目标函数执行之后...
                return ret
            return inner   千万别加 ()

        @wrapper
        def target():
            pass

        target()


    一个函数可以被多个装饰器装饰
    @wrapper1
    @wrapper2
    def target():
        print("I'm the target()")

    规则和规律: wrapper1 wrapper2 TARGET wrapper2 wrapper1


    
"""

def wrapper1(fn):  # fn: wrapper2.inner
    def inner(*args, **kwargs):
        print("enter wrapper1")    # 1
        ret = fn(*args, **kwargs)  # wrapper2.inner
        print("exit wrapper1")  # 5
        return ret
    return inner

def wrapper2(fn):  # fn: target
    def inner(*args, **kwargs):
        print("enter wrapper2")  # 2
        ret = fn(*args, **kwargs)  # target
        print("exit wrapper2")  # 4
        return ret

    return inner


@wrapper1  # target = wrapper1(wrapper2.inner)  ==> target: wrapper1.inner
@wrapper2  # target = wrapper2(target)   ==> target: wrapper2.inner
def target():
    print("I'm target()")  # 3

"""
enter wrapper1
enter wrapper2
I'm target()
exit wrapper2
exit wrapper1
"""
target()