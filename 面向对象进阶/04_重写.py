# 方法重写也成为方法覆盖，是指子类重新定义父类中已经存在的方法。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f"我叫{self.name}, 今年{self.age}岁")

class Student(Person):
    def __init__(self, name, age, id, score):
        super().__init__(name, age)  # 调用父类的构造器
        self.id = id
        self.score = score

    def say(self):
        # 重写父类的 say 方法
        print(f"我叫{self.name}, 今年{self.age}岁, 学号是{self.id}, 成绩是{self.score}")

Person("张三", 20).say()  # 调用父类的 say 方法
Student("李四", 21, "2023001", 95).say()  # 调用子类的 say 方法，重写了父类的方法
