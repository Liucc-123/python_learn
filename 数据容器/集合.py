set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合
print(f"set1:{set1}, 类型是：{type(set1)}")
print(f"set2:{set2}, 类型是：{type(set2)}")

# 集合去重
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"去重后的集合：{basket}")
# 判断集合是否在集合内
print(f"是否包含 'apple'：{'apple' in basket}")
# 两个集合之间的运算
setA = set('abracadabra')
setB = set('alacazam')
print(setA) # {'c', 'd', 'b', 'a', 'r'}
print(setB) # {'c', 'a', 'z', 'l', 'm'}
# 1、求交集 a & b
print(setA & setB) # {'c', 'a'}
print(setA.intersection(setB))
# 2、求并集 a | b
print(setA | setB) # {'b', 'm', 'd', 'r', 'a', 'l', 'c', 'z'}
# 3、求差集 a - b
print(setA - setB) # {'r', 'd', 'b'}
# 4、对称差集 a ^ b（不同时包含在集合 A 或集合 B 中的元素）
print(setA ^ setB) # {'r', 'd', 'b', 'z', 'l', 'm'}

# 集合推导式
set1 = {x for x in 'abracadabra' if x not in 'abc'}
print(set1) # {'r', 'd'}

## 集合基本操作
# 添加元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Baidu")
print(thisset) # {'Runoob', 'Google', 'Baidu', 'Taobao'}

# 通过 update() 方法添加多个元素
thisset.update({1,3})
print(thisset) # {'Runoob', 1, 'Google', 3, 'Baidu', 'Taobao'}

# 删除元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao") # {'Google', 'Runoob'}
print(thisset)
# thisset.remove("facebook") # KeyError: 'facebook'，如果元素不存在会报错
thisset.discard("facebook") # 不存在也不会报错
print(thisset)
# 随机删除一个元素
thisset = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(thisset.pop())
# 计算元素的个数
thisset = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(len(thisset)) # 4
# 清空集合
thisset.clear()
print(thisset) # set()