"""
装饰器：本质上是一个闭包
    作用： 在不改变原有函数调用的情况下，给函数增加新的功能。
    直白：可以在函数前后添加新功能，但是不改变代码。

    在哪些地方使用：
        在用户登录的地方，日志，

    雏形：
        def wrapper(fn):   wrapper: 装饰器, fn: 目标函数
            def inner(*args, **kwargs):
                # 在目标函数执行之前...
                fn(*args, **kwargs)
                # 在目标函数执行之后...
            return inner   千万别加 ()

"""

def master_(game):
    # args 是元组，kwargs 是字典
    # 这里的*,**表示接收所有的参数，打包成元组和字典
    # (admin, 123456)
    def inner(*args, **kwargs):
        print('Open game cheating')
        # 这里的*,**表示把args元组和kwargs字典打散成位置参数以及关键字参数传递进去
        # game('admin', '123456')
        game(*args, **kwargs)
        print('Close game cheating')
    return inner

@master_
def play_dnf(username, password):
    print(f"I'm start dnf {username}={password}")
    print("Hello, I'm Fernando, Today is a pretty day.")

@master_
def play_lol(username, password, hero):
    print(f"I'm start lol {username}={password}={hero}")

    print("Hello, Lisa")

print('-----------------------')

play_dnf("admin", "123456")
play_lol("admin", "123456", "Dragu")
