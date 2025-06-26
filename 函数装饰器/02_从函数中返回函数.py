def hi(name="shuiguan"):
    def greet():
        return "现在你在 greet()函数里面"

    def welcome():
        return "现在你在 welcome()函数里面"

    if name == "shuiguan":
        return greet  # 注意不要带小括号，带小括号会直接调用函数
    else:
        return welcome  # 注意不要带小括号，带小括号会直接调用函数


a = hi()  # 变量 a 指向函数 greet()
print(a)  # <function hi.<locals>.greet at 0x100315bc0>
print(a())  # 现在你在 greet()函数里面
print("hi()():", hi()()) # hi()(): 现在你在 greet()函数里面

"""
细节说明：
1. 当写下 a = hi()时，hi()函数会被调用，默认参数是"shuiguan"，因此返回的是  greet 函数。
2. 我们还可以打印出hi()()，这将会输出：现在你在 greet()函数里面
3. 如果我们调用 hi("其他名字")，则会返回 welcome 函数。
"""
