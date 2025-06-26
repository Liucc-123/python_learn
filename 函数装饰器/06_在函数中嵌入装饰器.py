### 包装器函数也是可以带有参数的，继续实现日志记录函数，参数是用户指定的文件路径，创建一个包裹函数，能输出日志到我们指定的日志文件。
from functools import wraps

def logit(logfile='out.log'):
    """装饰器函数，用于记录函数调用的日志到指定文件"""
    def decorator(func):
        @wraps(func)  # 保留原函数的元信息
        def wrapper(*args, **kwargs):
            with open(logfile, 'a') as f:
                f.write(f"{func.__name__} was called\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@logit() # 注意这里包装器函数需要带小括号，因为现在包装器函数是有参数的
def myfunc1():
    pass
@logit("log.txt")  # 可以指定日志文件路径
def myfunc2():
    pass
myfunc1()
myfunc2()

