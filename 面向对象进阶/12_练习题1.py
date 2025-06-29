# 1. 定义一个Person类，属性：name，age，job，创建Person，有3个person对象，并按照age从大到小排序。
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"{self.name}, {self.age}, {self.job}"


p1 = Person("zhangsan", 45, "农民")
p2 = Person("lisi", 36, "作家")
p3 = Person("王五", 69, "导演")


# 实现年龄从大到小排序
# 方案一：冒泡排序
def bubble_order(peoples: list[Person]):
    n = len(peoples)
    for i in range(n):
        for j in range(0, n - i - 1):
            if peoples[j].age < peoples[j + 1].age:  # 从大到小排序
                peoples[j], peoples[j + 1] = peoples[j + 1], peoples[j]


# 方案二：使用内置的 sorted 函数

print("按照 age 从大到小排列：")
people_list = [p1, p2, p3]
# bubble_order(people_list)
people_list.sort(key=lambda ele: ele.age, reverse=True)
for person in people_list:
    print(person, end="\t")
