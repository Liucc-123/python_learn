def hi():
    print("你好，我是水冠")
def doBeforeHi(func):
    print("我在 hi() 函数之前")
    func()
    print("我在 hi() 函数之后")

# 调用函数
doBeforeHi(hi) # 注意：hi 函数不要带小括号，因为我们要传递函数对象，而不是调用函数。