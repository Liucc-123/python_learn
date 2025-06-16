"""
下面是调用函数时可以使用的正式参数类型：
1、必须参数（位置参数）
2、关键字参数
3、默认参数
4、不定长参数（可选参数）
"""
from functools import reduce

print("=====不定长参数：元组形式======")


# 一个*表示该参数是不定长参数，以元组的形式导入数据
def printme(name, age=25, *varArgs):
    print("Name: ", name, "age:", age)
    print("不定长参数：")
    for arg in varArgs:
        print(arg)


printme("Tom", 30, "hello", "world")

print("=====不定长参数：字典形式======")


# 两个**也表示不定长参数，以字段的形式导入数据
def printinfo(name, **kwargs):
    print("name:", name)
    print("字典不定长参数：", kwargs)


printinfo("Tom", age=30, city="Beijing")

print("====================")
### 匿名函数
# 通过 lambda 表达式来创建一个匿名函数
# 语法：lambda arguments: expression
# arguments 是参数列表，expression 是表达式，表达式的计算结果就是匿名函数的返回值
# 注意
# 1、result既是变量名也是函数名
# 2、：左侧是参数列表，右侧是表达式
f = lambda: print("hello, world")
# 调用无参匿名函数
f()
result = lambda a: a + 10
print(result(10))
sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为：", sum(10, 20))
# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]
# 使用 filter 筛选出偶数
even_numbers = list(filter(lambda item: item % 2 == 0, numbers))
print("even_numbers:", even_numbers)
# 使用 reduce 计算所有数字的总和
multiNumber = reduce(lambda x, y: x * y, numbers)
print("multiNumber:", multiNumber)
# 将匿名函数封装到一个函数中
def myfunc(n):
    return lambda a: a * n
# myfunc返回一个 lambda 函数
doubleNum = myfunc(2)
tripleNum = myfunc(3)
print("doubleNum:", doubleNum(10))
print("tripleNum:", tripleNum(10))

