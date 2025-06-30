# Python 有两种错误很容易辨认：语法错误和异常。
# Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
## 语法错误
# 语法错误是在编写代码期间，ide 就能检测出来的错误，通常也是初学者经常会犯的错误
## 异常
# 异常是 Python 语法可能是正确的，但运行时才能看到报错，这种运行期间才能检测出来的错误，称之为异常。
# num = 10 / 0  # ZeroDivisionError: division by zero
## 异常处理
# 异常处理使用try/except语句
"""
    try:
        执行程序逻辑
    except:
        发生异常时的处理代码
"""
# try:
#     x = int(input("请输入一个数字: "))
# except ValueError:
#     print("您输入的不是数字，请再次尝试输入！")
# 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
# 一个 except 可以同时处理多种错误，使用元组来存放异常：
# except (RuntimeError, TypeError, NameError):
#     pass

# try/except...else语句
"""
    try:
        业务逻辑
    except:
        发生异常时执行的代码
    else:
        没有异常时执行的代码     
"""

# try-finally 语句
"""
    try:
        业务逻辑
    except:
        发生异常时执行的代码
    else:
        没有异常时执行的代码     
    finally:
        最终一定会执行的代码  
"""

# 抛出异常 raise
# Python使用raise 语句抛出一个指定异常
# x = 100
# if x > 5: raise RuntimeError("x 的值不能超过 5")

# 用户自定义异常
# 你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
# 注意：大多数异常名字都是以 Error 结尾
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(100)
except MyError as e:
    print(f"my exception occured, value: {e.value}")


