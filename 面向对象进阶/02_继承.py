## 快速入门
# 编写父类
class Student:
    name = None
    age = None
    __score = None

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("分数必须在0到100之间")
        self.__score = score

    def get_score(self):
        return self.__score

    def show_info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 分数: {self.__score}")

class Pupil(Student):
    def __init__(self, name, age, score):
        super().__init__(name, age, score)

    def testing(self):
        print("小学生正在考试...")
class Graduate(Student):
    def __init__(self, name, age, score):
        super().__init__(name, age, score)

    def testing(self):
        print("研究生正在考试...")

# 测试代码
pupil = Pupil("小明", 10, 85)
pupil.show_info()
pupil.testing()

graduate = Graduate("小红", 22, 90)
graduate.show_info()
graduate.testing()
## 继承带来的好处
# 1. 代码复用：子类可以继承父类的属性和方法，减少代码重复。
# 2. 代码组织：通过继承，可以将相关的类组织在一起，形成层次结构，便于管理和维护。

## 继承的注意事项和使用细节
# 1. 子类继承了所有的属性和方法，非私有的属性和方法可以在子类直接访问，但是私有属性和方法在子类不能在子类直接访问，要通过父类提供公共的方法去访问。
# 2. 在多继承的情况下，如果多个父类有同名的方法，Python 会按照方法解析顺序（MRO）来决定调用哪个父类的方法。可以使用 `ClassName.__mro__` 查看 MRO。
# 创建示例类来演示MRO
class A:
    def show(self):
        print("A的show方法")

class B(A):
    def show(self):
        print("B的show方法")

class C(A):
    def show(self):
        print("C的show方法")

class D(B, C):
    pass

# 查看MRO
print(f"D类的MRO顺序：{D.__mro__}")
# 输出类似：(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 测试方法调用
d = D()
d.show()  # 将调用B类的show方法，因为B在MRO中排在C之前


## 练习题
# 练习题 1
class GrandPa:
    name = "大头爷爷"
    hobby = "旅游"


class Father(GrandPa):
    name = "大头爸爸"
    age = 39


class Son(Father):
    name = "大头儿子"


son = Son()
print(f"son.name is {son.name} and son.age is {son.age} and son.hobby is {son.hobby}") # 大头儿子 39  旅游

# 练习题 2
class Computer:
    cpu = None
    memory = None
    disk = None

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def get_details(self):
        return f"CPU: {self.cpu}, Memory: {self.memory}, Disk: {self.disk}"


class PC(Computer):
    brand = None

    def __init__(self, cpu, memory, disk, brand):
        # 初始化子类的属性——方式 1
        # self.cpu = cpu
        # self.memory = memory
        # self.disk = disk
        # self.brand = brand

        # 初始化子类的属性——方式 2
        # 通过 super().xx 方式可以去调用父类方法，这里通过 super().__init__(cpu, memory, disk, brand) 去调用父类的构造器
        super().__init__(cpu, memory, disk)
        self.brand = brand

    def print_info(self):
        print(f"品牌：{self.brand}\t{self.get_details()}")


pc = PC("inter", 32, 1000, "戴尔")
pc.print_info()




