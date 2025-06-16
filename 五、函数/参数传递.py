# 不可更改类型
"""
字符串、元祖（tuple）、数字属于不可更改类型。当不可更改类型对象的值被改变时，并不是值被修改了，而是创建了一个新的对象。
"""
# 可更改类型
"""
列表（list）、字典（dict）属于可更改类型
"""

# 函数传递不可变对象实例
def change(a):
    print(id(a)) # 指向的是同一个对象
    a = 20
    print(id(a))
a = 5
print(id(a))
change(a)

print("================")
# 修改可变对象
def changeMutable(myList):
    "修改传入的列表"
    print(id(myList)) # 指向的是同一个对象
    myList.append([1, 2, 3, 4])
    print(id(myList))

# 函数传递可更改对象实例
numList = [1, 2, 3, 4, 5]
print(id(numList))
changeMutable(numList)

