# 1、编写A01，定义方法max_lst，实现求某个float 列表list = [1.1, 2.9, -1.9, 67.9]的最大值，并返回。
import random
from math import pi


class A01:
    def max_lst(self, list):
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max


a01 = A01()
float_result = a01.max_lst([1.1, 2.9, -1.9, 67.9])
print(f"max:{float_result}")


# 2、编写类Book，定义方法update_price，实现更改某本书的价格，具体：如果价格>150，则更改为150，如果价格>100，更改为100，否则不变。
class Book:
    price: int = None

    def __init__(self, price):
        self.price = price

    def update_price(self, price):
        if price >= 150:
            self.price = 150
        elif price >= 100:
            self.price = 100
        else:
            self.price = price

    def printme(self):
        print(f"price:{self.price}")


book = Book(124)
book.update_price(125)
book.printme()


# 3、定义一个圆类Circle，定义属性：半径，提供显示圆周长功能的方法，提供显示圆面积的方法。
class Circle:
    radius: float = None

    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        """
        计算圆的周长
        :return: 返回圆的周长
        """
        return 2 * pi * self.radius

    def calculate_area(self):
        """
        计算圆的面积
        :return:
        """
        return round(pi * self.radius ** 2, 2)  # 保留 2 位小数


circle = Circle(4)
print(circle.calculate_circumference())
print(circle.calculate_area())


# 4、编程创建一个Cal计算类，在其中定义2个成员变量表示两个操作数，定义四个方法实现求和、差、乘、商（要求除数为0的话，要提示）并创建对象，分别测试。
class Cal:
    num1 = None
    num2 = None

    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def operation_add(self):
        return self.num1 + self.num2

    def operation_sub(self):
        return self.num1 - self.num2

    def operation_mul(self):
        return self.num1 * self.num2

    def operation_div(self):
        if self.num2 == 0:
            return "除数不能为0"
        return round(self.num1 / self.num2, 2)


result1 = Cal(1, 0)
print(f"求和计算结果：{result1.operation_add()}")
print(f"求差计算结果：{result1.operation_sub()}")
print(f"求乘计算结果：{result1.operation_mul()}")
print(f"求商计算结果：{result1.operation_div()}")


# 5、定义Music类，里面有音乐名name，音乐时长times属性，并有播放play功能，和返回本身属性信息的方法 get_info。
class Music:
    name: str = None
    times: float = None

    def __init__(self, name: str, times: float):
        self.name = name
        self.times = times

    def get_info(self):
        print("音乐名：{0}，时长：{1}".format(self.name, self.times))


命运交响曲 = Music("命运交响曲", 4.5)
命运交响曲.get_info()


# 6、分析下列代码输出结果。
class Demo:
    i = 100

    def m(self):
        self.i += 1  # 101
        j = self.i  # 100
        print("i =", self.i)
        print("j =", j)


d1 = Demo()
d2 = d1
d2.m()  # 101 101

print(d1.i)  # 101
print(d2.i)  # 101


# 7、石头剪刀布游戏，0表示石头，1表示剪刀，2表示布。
class Tom:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.choices = ['石头', '剪刀', '布']

    def play(self):
        user_choice = int(input("请猜拳（0-石头，1-剪刀，2-布）"))
        if user_choice not in [0, 1, 2]:
            print("请输入 [0-2]之间的数字")
            return
        computer_choice = random.randint(0, 2)
        if user_choice == computer_choice:
            print("平局")
        elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (
                user_choice == 2 and computer_choice == 0):
            print("tom获胜！")
            self.wins += 1
        else:
            print("电脑获胜！")
            self.losses += 1

    def show_scores(self):
        print(f"tom赢了{self.wins}局，输了{self.losses}局")


Tom = Tom()
Tom.play()
Tom.play()
Tom.play()
Tom.show_scores()
