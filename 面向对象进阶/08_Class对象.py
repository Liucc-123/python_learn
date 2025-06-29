class Monster:
    name = "怪物"
    hp = 100

    def say_hi(self):
        print(f"{self.name} 说：你好！")

print(Monster) # 万物皆对象，类本身也是一个对象
print(f"{Monster.name} - {Monster.hp}")

Monster.say_hi(Monster) # 调用类方法，需要传入类本身作为self参数