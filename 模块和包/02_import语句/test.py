import sys
import fibo

import support

support.print_func("水冠")
print(sys.path)

fibo.fib(100)
print(fibo.fib2(100))
print(fibo.__name__)

# 如果 fibo 模块的 fib 函数经常使用，可以将其赋值给本地的一个变量
fib = fibo.fib
fib(50)