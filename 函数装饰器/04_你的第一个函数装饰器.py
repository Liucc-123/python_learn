# 手动包装原生函数
# def func_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
# # 使用@符号标注包装函数
# @func_decorator
# def sayHello():
#     print("你好，我是水冠")
from functools import wraps


# sayHello()
# # outputs: 你好，我是水冠
#
# wrappedFunc = func_decorator(sayHello)
# wrappedFunc()
# outputs:I am doing some boring work before executing a_func()
# 你好，我是水冠
# I am doing some boring work after executing a_func()

# sayHello()
# outputs: I am doing some boring work before executing a_func()
# 你好，我是水冠
# I am doing some boring work after executing a_func()
# print(sayHello.__name__) # outputs: wrapTheFunction
# 这里会输出：# wrapTheFunction，因为我们使用了装饰器函数func_decorator来包装sayHello函数。包装函数重写了原生函数 sayHello()的名字
# 如果我们想要保留原生函数的名字，可以使用functools.wraps装饰器来修饰包装函数
# 改写上面的函数
def func_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

# 使用@符号标注包装函数
@func_decorator
def sayHello():
    print("你好，我是水冠")

print(sayHello.__name__) # outputs: sayHello
