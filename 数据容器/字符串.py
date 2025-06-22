# 在 Python 中可以使用单引号'、双引号"、三重引号"""来创建字符串。
str1 = 'Hello, World!'  # 单引号字符串
str2 = "Hello, World!"  # 双引号字符串
str3 = """
    《浪淘沙·北国风光》  毛泽东
    北国风光，千里冰封，万里雪飘。
    望长城内外，惟余莽莽；大河上下，顿失滔滔。
    山舞银蛇，原驰蜡象，欲与天公试比高。
    须晴日，看红装素裹，分外妖娆。
    江山如此多娇，引无数英雄竞折腰。
    惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。
    一代天骄，成吉思汗，只识弯弓射大雕。
    俱往矣，数风流人物，还看今朝。
"""
print(str1)
print(str2)
print(str3)

var1 = 'Hello World!'

print("已更新字符串 : ", var1[:6] + 'tiga!')

# % 格式化字符串
name = "tiga"
age = 25
print("我的名字是 %s, 今年 %d 岁。" % (name, age))
# f-string 格式化字符串
print(f"我的名字是 {name}, 今年 {age} 岁。")

## 练习题
"""
定义一个字符串，str_names="tom jack mary nono smith hsp"
统计一共有多个人名；如果有"hsp"则替换成"老韩";如果人名是英文，则把首字母改为大写
str.capitalize()：字符串首字符改为大写
"""

str_names = str("李星云 姬如雪 张子凡 nono  prometheus")

str_names_list = str_names.split(" ")
print(f"人名的个数：{len(str_names_list)}")
str_names_re = str_names.replace("张子凡", "陆林轩")
print(str_names_re)

str_names_upper = ""
for ele in str_names_list:
    if ele.isalpha(): # 判断是否为英文字符
        str_names_upper += ele.capitalize() + " "

# 去掉两边的" "
str_names_upper = str_names_upper.strip(" ")
print(str_names_upper)
