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


login_flag = False

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        if login_flag is False:
            print('Please finish logon action')
            while 1:
                username = input("username>>>")
                password = input("password>>>")
                if username == "admin" and password == "123456":
                    print("Welcome")
                    login_flag = True
                    break
                else:
                    print("Wrong")

        ret = fn(*args, **kwargs)
        return ret
    return inner


@login_verify
def create():
    print("create user")

@login_verify
def retrieve():
    print("retrieve user")

@login_verify
def update():
    print("update user")

@login_verify
def delete():
    print("delete user")

create()
retrieve()
update()
delete()