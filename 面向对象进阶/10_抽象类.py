## 默认情况下，Python 是不提供抽象类的支持的，但可以通过使用 `abc` 模块来实现抽象类和抽象方法。
# 当类继承了 abc 模块的 ABC 类，并使用 `@abstractmethod` 装饰器来定义抽象方法时，这个类就成为了抽象类。
# 抽象类是不能被实例化的，必须由子类实现所有的抽象方法才能实例化。
# 继承抽象类的子类必须实现所有的抽象方法，否则子类也会成为抽象类，不能被实例化。
# 抽象类也可以定义普通方法
from abc import ABC, abstractmethod


# 抽象类
class Employee(ABC):
    def __init__(self, name, id, salary):
        self.__name = name
        self.__salary = salary
        self.__id = id

    def get_annual(self):
        return self.__salary() * 12

    def get_name(self):
        return self.__name

    # 抽象方法
    @abstractmethod
    def work(self):
        pass

# 普通员工类 CommonEmployee
class CommonEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)

    def work(self):
        print(f"普通员工 {self.get_name()} 正在工作...")
# 经理类 Manager
class Manager(Employee):
    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus

    def work(self):
        print(f"经理 {self.get_name()} 正在管理...")

    def get_annual(self):
        return super().get_annual() + self.bonus
worker = CommonEmployee("小段", "2023001", 4500)
worker.work()

manager = Manager("刘总", "2023002", 25000, 200000)
manager.work()
