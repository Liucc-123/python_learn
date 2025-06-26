## 日志场景
from functools import wraps

def logit(func):
    """装饰器函数，用于记录函数调用的日志"""
    @wraps(func) # 保留原函数的原信息
    def wrapper(*args, **kwargs):
        # print(f"函数{func.__name__}被调用")
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return wrapper

# 原生函数
@logit
def addition_func(x):
    """做一些加法运算的操作"""
    return x + x
result = addition_func(4)
print(result)

