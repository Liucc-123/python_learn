# 封装：将复杂的内部逻辑封装起来，暴露简单的接口对外提供出去。典型的例子就是电视机，使用者只需要通过遥控器来控制电视机的开关、音量等，而不需要了解电视机内部的电路和工作原理。
# 私有属性/方法：在类中定义的属性或方法前加上双下划线（__）前缀，表示该属性或方法是私有的，只能在类内部访问，外部无法直接访问。

# 创建职员类（Clerk），属性：name, job, salary
# 1、不能随便查看职员 Clerk 的职位和工资等隐私，比如职员 ("tiger", "python 工程师", 20000)
# 2、提供公共方法，可以对职员和工资进行操作

class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 提供公共的方法，对私有属性操作（根据实际的业务编写即可）
    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job

    # 私有方法
    def __hi(self):
        print("hi()")

    # 提供公共方法，操作私有方法
    def f1(self):
        self.__hi()


clerk = Clerk("tiger", "python 工程师", 20000)
print(clerk.name)

# print(clerk.__job)  # AttributeError: 'Clerk' object has no attribute '__ job'
print(clerk.get_job())
clerk.set_job("Java 工程师")
print(clerk.get_job())

# 私有方法不能在类的外部直接调用
# clerk.hi()  # AttributeError: 'Clerk' object has no attribute 'hi'

# 通过公共方法，调用私有方法
clerk.f1()

## 注意事项和细节
# python语言的动态特性，会出现伪私有属性的情况
clerk.__job = "JavaScript 工程师" # 说明：这里的 __job 是伪私有属性，实际上是 Clerk 类的一个新属性，并不是类中定义的私有属性 __job
print(clerk.__job)  # 输出：JavaScript 工程师

## 练习：Account 类要求具有属性：姓名（长度为 2-4 位）、余额（必须 > 20）、密码（必须是六位），如果不满足，则给出提示
# 通过 set_xx 的方法给 Account 的属性赋值
# 编写 query_info() 接收姓名和密码，如果姓名和密码正确，返回该账号信息
class Account:
    def __init__(self, name, balance, password):
        self.set_name(name)
        self.set_balance(balance)
        self.set_password(password)

    def set_name(self, name):
        if 2 <= len(name) <= 4:
            self.name = name # 动态创建属性
        else:
            raise ValueError("姓名长度必须在 2-4 位之间")

    def set_balance(self, balance):
        if balance > 20:
            self.balance = balance
        else:
            raise ValueError("余额必须大于 20")

    def set_password(self, password):
        if len(password) == 6:
            self.password = password
        else:
            raise ValueError("密码必须是六位")

    def query_info(self, name, password):
        if self.name == name and self.password == password:
            return f"姓名: {self.name}, 余额: {self.balance}"
        else:
            return "姓名或密码错误"
tim = Account("Tim", 18, "123456")
print(tim.query_info("Tim", "123456"))