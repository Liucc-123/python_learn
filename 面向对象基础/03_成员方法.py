## 成员方法和函数几乎是一样的，只是形式上略有不同。成员方法参数列表的第一个参数必须是self，表示当前对象本身。
# 这个名字可以是其他，但强烈建议命名为 self，保持习惯上的统一。
class Person:
    # 成员属性
    age = None
    name = "tiga"
    # 成员方法
    def sayHello(self):
        # 属性必须通过 self 来访问
        print(f"hello, my name is {self.name}")
person = Person()
person.sayHello()
