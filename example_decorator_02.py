"""
装饰器：本质上是一个闭包
    作用： 在不改变原有函数调用的情况下，给函数增加新的功能。
    直白：可以在函数前后添加新功能，但是不改变代码。

    在哪些地方使用：
        在用户登录的地方，日志，

    雏形：
        def wrapper(fn):   wrapper: 装饰器, fn: 目标函数
            def inner():
                # 在目标函数执行之前...
                fn()
                # 在目标函数执行之后...
            return inner   千万别加 ()

"""
def play_dnf():
    print("Hello, I'm Fernando, Today is a pretty day.")

def play_lol():
    print("Hello, Lisa")


# print('open game cheating')
# play_dnf()
# print('close game cheating')
#
#
# print('open game cheating')
# play_lol()
# print('close game cheating')

print('-----------------------')
def master(game):
    def inner():
        print('Open game cheating')
        game()
        print('Close game cheating')
    return inner

play_dnf = master(play_dnf)
play_lol = master(play_lol)
play_dnf()
play_lol()