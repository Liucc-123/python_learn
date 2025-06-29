class Doctor:
    def __init__(self, name, age, sal, job, gender):
        self.name = name
        self.age = age
        self.sal = sal
        self.job = job
        self.gender = gender
    def __eq__(self, other):
        # 判断两个 Doctor 对象是否相等
        return (self.name == other.name and
                self.age == other.age and
                self.sal == other.sal and
                self.job == other.job and
                self.gender == other.gender and
                isinstance(other, Doctor))
# 测试
doctor1 = Doctor("张医生", 35, 12000, "外科医生", "男")
doctor2 = Doctor("张医生", 35, 12000, "外科医生", "男")
print(doctor1 == doctor2)