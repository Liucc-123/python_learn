#!/usr/bin/python3

# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[0:4])


list = ['tiga', '水冠', 1997, 2000]
print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list1 = ['侯卿', '旱魃', '莹勾']
list1.append('降臣')
print("更新后的列表 : ", list1)

list1 = ['侯卿', '旱魃', '莹勾']
del list1[1]
print("删除后的列表 : ", list1)

## 列表常见操作符
print("======================")
# len()
print(len([1, 2, 3]))
# + 操作符
print([1, 3, 5] + [2, 4, 6])
# * 操作符
print(['hi!'] * 4)
# in 判断元素是否存在于指定列表中
print(3 in [1, 2, 3])
# for 迭代
for e in [1, 2, 3]:
    print(e, end="\t")
print()
## 嵌套列表
list1 = ['a', 'b', 'c']
list2 = [12.4, '苹果', '太阳']
nested_list = [list1, list2]
# 访问第一个子列表：
print(f"第一个子列表：{nested_list[0]}")


def f1(my_list):
    print(f"②f1() my_list: {my_list} 地址：{id(my_list)} my_list[0]: {my_list[0]} 第一个元素地址：{id(my_list[0])}")
    my_list[0] = "陆林轩"
    print(f"③f1() my_list: {my_list} 地址：{id(my_list)} my_list[0]: {my_list[0]} 第一个元素地址：{id(my_list[0])}")


print("-" * 30 + "list" + "-" * 30)
my_list = ["李星云", "姬如雪", "张子凡"]
print(f"①my_list: {my_list} 地址：{id(my_list)} my_list[0]: {my_list[0]} 第一个元素地址：{id(my_list[0])}")
f1(my_list)
print(f"④my_list: {my_list} 地址：{id(my_list)} my_list[0]: {my_list[0]} 第一个元素地址：{id(my_list[0])}")

## 列表推导式
# 创建数值序列
squares = []
# 1、传统方法
for item in range(10):
    squares.append(item ** 2)
print("squares1:", squares)
# 2、列表推导式
squares = [item ** 2 for item in range(10)]
print("squares2:", squares)

# 获取列表中所有偶数
evens = [item for item in range(20) if item % 2 == 0]
print(evens)