# 以下对象的 bool 值全部为 false
print(bool(0))
print(bool(""))
print(bool(None))
print(bool([]))
print(bool({}))
print(bool(tuple()))
print(bool(set()))

content = "abc"
if(content):
    print("内容不为空")
else:
    print("内容为空")