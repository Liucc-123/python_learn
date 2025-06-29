# 标注@staticmethod的函数是静态方法，静态方法不需要传递self参数
class Monster:
    name = "怪物"
    hp = 100

    @staticmethod
    def say_hi():
        print(f"{Monster.name} 说：你好！")
# 静态方法有两种调用方式
# 方式一：通过类名直接调用（推荐）
Monster.say_hi()
# 方式二：通过实例调用
Monster().say_hi()