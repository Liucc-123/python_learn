# 题目： 编写一个名为 format_name() 的函数，它接收两个字符串参数 first_name 和 last_name。
# 函数应返回一个格式化为 "Lastname, Firstname"（首字母大写）的全名字符串。
def format_name(first_name: str, last_name: str):
    return f"{cap_first(last_name)}, {cap_first(first_name)}"

def cap_first(s):
    return s[:1].upper() + s[1:] if s else ''


print(format_name("jOhN", "doE"))

