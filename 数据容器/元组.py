# 定义一个包含 6 个元素的元组
tuple_color = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')
print(tuple_color)

# 有两种方式创建空元组
tup1 = ()
tup2 = tuple()
print("空元组1:", tup1)
print("空元组2:", tup2)

# for循环遍历
for color in tuple_color:
    print(color, end=' ')
print()

# 元组只有一个元组时，需要在元素后加逗号
tup1 = (5)
print(type(tup1))
single_tuple = ('red',)
print(type(single_tuple))

# 访问元组
tup1 = ('Google', 'OPENAI', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)
# 元组中的列表元素是可以修改的，但不能修改列表本身：
tup4 = ([1, 2, 3], [4, 5, 6])
tup4[0][0] = 10
print(tup4)
# tup4[0] = [7, 8, 9]  # 这行会报错，因为不能修改元组中的列表元素

# 删除元组
tup = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

# print(tup)
# del tup
# print("删除后的元组 tup : ", tup)

# 练习
"""
定义一个元组：("大话西游", "周星驰", 80, ["周星驰", "小甜甜"])
信息为：(片名, 导演, 票价, 演员列表)
"""
tuple_movie = ("大话西游", "周星驰", 80, ["周星驰", "小甜甜"])
print("电影信息：")
print(f"片名: {tuple_movie[0]}")
print(f"导演: {tuple_movie[1]}")
print(f"票价: {tuple_movie[2]}")
print(f"演员列表: {tuple_movie[3]}")
# 删除 "小甜甜"， 增加演员 "牛魔王"，“猪八戒”
tuple_movie[3].remove("小甜甜")
tuple_movie[3].extend(["牛魔王", "猪八戒"])
print(f"更新后的演员列表: {tuple_movie[3]}")

