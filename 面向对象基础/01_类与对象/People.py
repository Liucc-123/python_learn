#!/usr/bin/python3

# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print(f"我叫{self.name}，今年{self.age}岁，体重{self.__weight}公斤。")


# 实例化类
p = People('水冠', 10, 30)
p.speak()