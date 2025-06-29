## 什么是魔术方法
# 魔术方法是 Python 中的一种特殊方法，它们以双下划线开头和结尾（例如 `__init__`、`__str__` 等）。会在对象需要的时候自动调用，而不需要程序员手动触发调用。
# 常见的魔术方法有：
# - `__init__`: 构造器，用于初始化对象。
# - `__str__`: 用于定义对象的字符串表示。
# - `__repr__`: 用于定义对象的官方字符串表示。
# - `__add__`: 用于定义加法操作。
# - `__len__`: 用于定义对象的长度。
# - `__eq__`: 用于定义对象的相等比较。

# str魔术方法说明：默认是返回对象在内存在的地址（十六进制）
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写object 类的 __str__ 方法
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    def __eq__(self, other):
        # self 和 other 是同一个类型的对象且各属性值相同
        return self.name == other.name and self.age == other.age and type(self) == type(other)
p1 = Person("tiga", 23)
# print(p1) # 默认情况输出：<__main__.Person object at 0x104cc1550>
print(p1)

# eq魔术方法说明：默认是比较对象在内存中的地址是否相同
p2 = Person("tiga", 23)
# print("p1 == p2:", p1 == p2)  # 输出：False，因为 p1 和 p2 是两个不同的对象
# print("p1 == p2:", p1 == p2)  # 输出：True，因为我们重写了 __eq__ 方法
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog = Dog("tiga", 23)
print("p1 == dog:", p1 == dog)  # 输出：False，因为 p1 和 dog 是不同类型的对象