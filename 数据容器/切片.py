# 字符串切片，截取"hello"
str_a = "hello,world"
print(str_a[0:5:1])

# 列表切片，截取["tom", "nono"]
list_a = ["jack", "tom", 'yoyo', "nono", "hsp"]
print(list_a[1:4:2])

# 元组切片，截取(200, 300, 400, 500)
tuple_a = (100, 200, 300, 400, 500, 600)
print(tuple_a[1:5:1])

print("=" *30)
str_a = "hello,hspjy"
str_slice01 = str_a[:5] # hello
print("str_slice01", str_slice01)
str_slice02 = str_a[1::1]
print("str_slice02", str_slice02) # ello,hspjy
str_slice03 = str_a[::1]
print("str_slice03", str_slice03) # hello,hspjy
str_slice04 = str_a[2:5:]
print("str_slice04", str_slice04) # llo

print("=" *30)
str_b = "123456"
str_slice05 = str_b[-1::-1]
print("str_slice05", str_slice05) # 65

str_slice06 = str_b[-1:-6:-1]
print("str_slice06", str_slice06) # 65432

print("=" *30)
# 定义列表 list_name = ["Jack", "Lisa", "Hsp", "Paul", "Smith", "Kobe"]
# 取出前三个名字；取出后三个名字，，并且保证原来顺序
list_name = ["Jack", "Lisa", "Hsp", "Paul", "Smith", "Kobe"]
# 取出前三个名字
list_name_f = list_name[:3]
# 取出后三个名字，并且保证原来顺序
list_name_b = list_name[-1:-4:-1]
list_name_b.reverse()
print(f"前三个名字：{list_name_f}")
print(f"后三个名字：{list_name_b}")
