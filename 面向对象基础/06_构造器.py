class Person:
    name = None
    age = None


    def __init__(self, name, age):
        """构造器"""
        # 构造器将接收到的 name 和 age 参数传递到当前对象的属性 name和 age
        # self 就是当前创建对象
        print("构造器正在被调用...")
        self.name = name
        self.age = age
p1 = Person("tiga", 23)
print(f"p1的名称是{p1.name}, p1的年龄是{p1.age}")

## 注意事项
# 1、Python 只能有一个构造器，即使写了多个构造器，也只有最后一个是生效的。不像 Java 得构造器是可以重载的，Python 没有方法重载，只有方法重写
# 2、构造器不能有返回值，构造器返回值是 None
# 3、Python 可以动态的生成对象属性值

class Animal:
    name = None
    age = None
    color =  None
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def __init__(self, name):
        self.name = name
        # return "hello" # 无法从 __init__ 返回值
    def printme(self):
        print("name:", self.name, "age:", self.age, "color:", self.color)
# 1、构造器只能有一个
# tiger = Animal("tiger", 23, "white")
# 上面这行会报错：
# tiger = Animal("tiger", 23, "white")
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: Animal.__init__() takes 2 positional arguments but 4 were given
# 因为Animal类有效的构造器是最下面那个
tiger = Animal("tiger")
tiger.printme() # name: tiger age: None color: None