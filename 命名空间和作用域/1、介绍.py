## 生命周期
# 一般有三种命名空间：
# - 内置名称：Python 内置的名称，比如函数名 abs、char 和异常名称 Exception、BaseException 等
# - 全局名称：在模块中定义的资源名称（变量、函数名、类等）
# - 局部名称：在函数中定义的属性、参数等

# 命名空间查找顺序：局部名称 -> 全局名称 -> 内置名称。如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常:
# NameError: name 'runoob' is not defined。

# 命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束了，资源也随之释放。
# var1 是全局名称
var1 = 5


def some_func():
    # var2 是局部名称
    var2 = 6

    def some_inner_func():
        # var3 是内嵌的局部名称
        var3 = 7

## 作用域
# 官方定义：作用域就是一个 Python 程序可以直接访问命名空间的正文区域
# 作用域有四种：
# - L（Local）：最内层，比如一个函数/类定义内部
# - E（Enclosing）：闭包函数外层，比如一个函数内部定义了另一个函数，内层函数可以访问外层函数的变量
# - G（Global）：当前脚本的最外层，比如当前模块的全局变量定义，函数定义
# - B（Built-in）：已经内建在 Python 中的名称，比如函数名 abs、char 和异常名称 Exception、BaseException 等
# Python 查找变量的顺序：local -> enclosing -> global -> built-in
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
# 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。
import builtins
dir(builtins)

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）
# 是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
if True:
    msg = 'I am Iron man'
print(msg)

## 全局变量和局部变量
# 全局变量：在函数外部定义的变量，在整个程序内都是可以访问的
# 局部变量：在函数内部定义的变量，只能在函数内部访问

## global 和 nonlocal 关键字
# 当内部作用域想要修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字
# 1、如果内部想修改的外部变量 target 所属作用域是全局作用域，就需要使用 global 关键字，表明当前引用的变量是全局的：
num = 10
def edit_num():
    # num = 200
    global num # global关键字生命当前变量用的是全局变量 num
    num = 200
    print("edit_num: ",num) # 200
edit_num()
print(f"num: {num}") # 10
# 2、如果内部想修改的外部变量 target 所属作用域是闭包作用域，就需要使用  nonlocal 关键字，表明当前引用的变量是闭包的：

def get_fruit():
    fruit = "apple" # 闭包 enclosing
    def inner_func():
        nonlocal fruit # nonlocal关键字表明当前变量引用的是外部（闭包）变量fruit
        fruit = "orange"
        print(f"fruit: {fruit}")
    inner_func()
    print(f"get_fruit: {fruit}")
# 测试
get_fruit()

## 总结
# 1. 全局变量在函数外部定义，在整个文件中可以访问
# 2. 局部变量在函数内部定义，仅在函数内部可以访问
# 3. global 关键字可以在函数内修改全局变量
# 4. nonlocal 关键字可以在闭包函数内修改外部函数变量