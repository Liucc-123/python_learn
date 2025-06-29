class Cat:
    name = "波斯猫"
    age = 2

    def info(self, name):
        print(f"name: {name}")  # 加菲猫
        # 通过 self.属性名 可以访问对象的属性/成员变量
        print(f"属性 name：{self.name}")  # 波斯猫

    @staticmethod
    def ok():
        print("ok。。。")


cat = Cat()
cat.info("加菲猫")

# 静态方法有两种调用方式：
# 方式一：对象调用
cat.ok()
# 方式二：类名调用
Cat.ok()


# 练习题：创建一个类 Person，比较两个人的信息 name，age。如果都相同，表明这两个人的属性是相同的。


class Person:
    name = None
    age = None

    def compareTo(self, other):
        return self.name == other.__name and self.age == other.age


person1 = Person()
person1.name = "张三"
person1.age = 18
person2 = Person()
person2.name = "张三"
person2.age = 18
print("person1 == person2 ? ", person1.compareTo(person2))