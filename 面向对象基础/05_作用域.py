# 在面向对象编程中，主要的变量就是成员变量和局部变量
# 局部变量一般定义在方法内，作用域是方法内部
# 属性(成员变量)一般定义在类内部，作用域是整个类
class Cat:
    # 属性(成员变量)
    name = None
    age = None

    # n1, n2, result 就是局部变量
    def cal(self, n1, n2):
        result = n1 + n2
        print(f"result = {result}")
