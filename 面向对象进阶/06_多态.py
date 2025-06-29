## 练习题
# 定义员工类Employee
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # 定义一个方法来获取员工的年工资
    def get_annual(self):
        return self.get_salary() * 12

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary


# 普通员工 Worker
class Worker(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(f"工人 {self.get_name()} 正在工作...")


# 经理类 Manager
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def manage(self):
        print(f"经理 {self.get_name()} 正在管理...")

    # 重写 get_annual 方法 经理年工资 = 月工资 * 12 + 奖金
    def get_annual(self):
        return super().get_annual() * 12 + self.bonus


# 获取任何员工的年工资
def show_emp_annual(emp: Employee):
    print(f"{emp.get_name()}的年工资为{float(emp.get_annual())}")


# 员工工作
def working(emp: Employee):
    # 如果是普通员工，调用 work 方法
    if isinstance(emp, Worker):
        emp.work()
    elif isinstance(emp, Manager):
        emp.manage()
    else:
        print("未知员工类型，无法工作")


# 测试入口
worker = Worker("小段", 4500)
manager = Manager("刘总", 25000,  200000)

show_emp_annual(worker)
show_emp_annual(manager)

working(worker)
working(manager)
