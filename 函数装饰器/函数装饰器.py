## 一切皆对象
def hi(name="yasoob"):
    return "hi " + name


print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
# print(hi()) # name 'hi' is not defined
# outputs: NameError

print(greet())
# outputs: 'hi yasoob'
print("="*30)
## 在函数中定义函数
def hi(name="shuiguan"):
    print("现在你在 hi()函数里面")
    def greet():
        return "现在你在 greet()函数里面"
    def welcome():
        return "现在你在 welcome()函数里面"
    print(greet())
    print(welcome())
    print("现在你在 hi()函数的最后")

hi()
# welcome() # NameError: name 'welcome' is not defined
