# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

# 创建字典
myDict = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}
print(myDict['name'])
# print(myDict['address'])  # KeyError: 'address'，因为字典中没有这个键
# 修改字典
tinydict = {'Name': 'tiga', 'Age': 23, 'Class': 'First'}
tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "北京大学"  # 添加键值对
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])
# 删除字典
tinydict = {'Name': 'tiga', 'Age': 7, 'Class': 'First'}
del tinydict['Name']  # 删除键 'Name'
print("删除后的字典：", tinydict)  # {'Age': 7, 'Class': 'First'}
print("字典的字符串表示：", str(tinydict))  # 字典的字符串表示
tinydict.clear()  # 清空字典
print(tinydict)
del tinydict  # 删除字典