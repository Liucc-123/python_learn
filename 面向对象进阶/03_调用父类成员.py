# 如果子类和父类出现同名属性或方法，可以通过父类名、super()函数来调用父类的属性或方法。
# class A:
#     n1 = 100
#
#     def run(self):
#         print("A-run()...")
#
#
# class B(A):
#     n1 = 200
#
#     def run(self):
#         print("B-run()...")
#
#     # 通过父类名去访问父类的成员
#     def say(self):
#         print(f"父类的 n1 ={A.n1} 本类的 n1 ={self.n1}")
#         # 调用父类的 run
#         A.run(self)
#
#         # 调用本类的 run()
#         self.run()
#
#     # 通过 super()方式去访问父类对象
#     def hi(self):
#         print(f"父类的 n1 ={super().n1}")
#
#
# b = B()
# b.say()
# b.hi()

## 注意事项和细节
# 1. 子类不能直接访问父类的私有属性和方法
# class A:
#     n1 = 100
#     __n2 = 600
#
#     def run(self):
#         print("A-run()...")
#
#     def __jump(self):
#         print("A-jump()...")
#
#
# class B(A):
#     # 子类不能直接访问父类的私有成员
#     def say(self):
#         # print(A.__n2)  # AttributeError: type object 'A' has no attribute '_B_ _n2'. Did you mean: '_A__n2'?
#         # print(super().__n2)  # AttributeError: 'super' object has no attribute '_B__n2'
#         #
#         # A.__jump(self)
#         # super().jump()
#         print("B-say()...")
# b = B()
# b.say()

# 访问不限于直接父类，而是从当前类开始向上级父类逐步查找，直到找到为止
class Base:
    n3 = 800

    def fly(self):
        print("Base-fly()...")


class A(Base):
    n1 = 100
    __n2 = 600

    def run(self):
        print("A-run()...")

    def __jump(self):
        print("A-jump()...")


class B(A):
    # 访问不限于直接父类，而是建立从子类向上级父类的查找关系 B-> A-> Base...
    def say(self):
        print(Base.n3, A.n3, super().n3)

        Base.fly(self)
        A.fly(self)
        super().fly()
        self.fly()


b = B()
b.say()

## 练习题
# 1. 分析下面的代码，看看输出什么内容？
class A:
    n1 = 300
    n2 = 500
    n3 = 600

    def fly(self):
        print("A-fly()...")


class B(A):
    n1 = 200
    n2 = 400

    def fly(self):
        print("B-fly()...")


class C(B):
    n1 = 100

    def fly(self):
        print("C-fly()...")

    def say(self):
        print(self.n1)  # 100
        print(self.n2)  # 400
        print(self.n3)  # 600
        print(super().n1)  # 200
        print(B.n1)  # 200
        print(C.n1)  # 100

        C.fly(self)
        A.fly(self)


c = C()
c.say()
# 2. 针对上面的程序，想在C的say()中，调用C的fly()和A的fly()，应该如何调用？
# 答：C 调用 C 类自己的 fly 方法，A 调用 A 类自己的 fly 方法，因为各自都有各自的同名方法




