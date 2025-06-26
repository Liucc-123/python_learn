# from...import 语句可以导入指定模块的具体资源。好处是可以避免导入整个模块，节省内存和加载时间。再一个是使用时不需要添加模块前缀。
from math import sqrt

num = 3.14
def sqrt(x): # 定义重名函数，会覆盖导入的 sqrt 函数
    return x * 2
print(sqrt(16))

pi = 3
# 导入 math 模块的 pi 常量，会覆盖上面定义的 pi 变量
from math import pi
print(pi * 5)