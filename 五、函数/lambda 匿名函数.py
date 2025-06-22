# lambda 语法格式
# lambda arguments: expression

# 1、无参的匿名函数
f = lambda: print("你好，这是一个无参函数")
f()
# 2、函数计算参数 a+10的结果，并返回
var = lambda a: a + 10
print(f"结果为{var(15)}")
# 3、lambda 函数也可以设置多个参数，用逗号隔开
# 计算矩形（a，b）的面积
area = lambda a, b: a * b
print(f"矩形面积为{area(10, 5)}")

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

