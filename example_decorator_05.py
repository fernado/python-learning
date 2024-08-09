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

"""

def master_(game):

    def inner(*args, **kwargs):
        print('Open game cheating')
        # 这里是目标函数的执行，是可以获取到目标函数的返回值的
        ret = game(*args, **kwargs)
        print('Close game cheating')
        return ret
    return inner


@master_
def play_dnf(username, password):
    print(f"I'm start dnf {username}={password}")
    print("Hello, I'm Fernando, Today is a pretty day.")
    return 'a beautiful dnf'


def play_lol(username, password, hero):
    print(f"I'm start lol {username}={password}={hero}")

    print("Hello, Lisa")

print('-----------------------')

ret = play_dnf("admin", "123456")
print(ret)
# play_lol("admin", "123456", "Dragu")

print("-------------------------------------------------------------------------------------")
def module_decorator(module_func):
    """装饰器函数，用来包装模块"""

    def wrapper(*args, **kwargs):
        print(module_func.__name__ + "start")
        print("模块执行前: 设置环境或其他操作")
        result = module_func(*args, **kwargs)
        print("模块执行后: 清理工作或其他操作")
        print(module_func.__name__ + "end")
        return result

    return wrapper


# 假设这是你想要包装的模块
@module_decorator
def my_module():
    print("这是模块的内容")


# 调用被装饰器包装的模块
my_module()