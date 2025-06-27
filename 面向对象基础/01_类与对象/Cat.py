class Cat:
    age = 23
    name = None
    color = None

    def __init__(self, age, name, color):
        self.age = age
        self.name = name
        self.color = color

    def introduce_myself(self):
        print(f"Hello, I am {self.name}, a {self.color} cat, and I am {self.age} years old.")


cat = Cat(20, "Tom", "Black")
cat.introduce_myself()