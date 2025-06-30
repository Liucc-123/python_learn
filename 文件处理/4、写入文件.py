# mode 模式：
# w：写入模式，文件不存在则创建；文件存在，会清空之前的全部内容！！！
# w+：写入读取
# r：读取模式，前提是文件已经存在
# r+：读取写入，前提是文件已经存在
# a：追加模式，在文件末尾写入内容
# a+：追加读取
# 在/Users/mac/刘创创 目录下，创建文件 write.txt，并写入 10行“让天下大同”
with open("/Users/mac/刘创创/write.txt", "w+", encoding="utf-8") as f:
    for _ in range(10):
        f.write("让天下大同\n")
    # 将文件指针移动到文件开头
    f.seek(0)
    # 读取最后写入的文件内容
    lines = f.readlines()
    for line in lines:
        print(line, end="")

# 需求 2：在原有内容的基础上，再追加 10行内容“一天是不良人，一辈子都是”
with open("/Users/mac/刘创创/write.txt", "a+", encoding="utf-8") as f:
    # 追加文件内容
    for _ in range(10):
        f.write("一天是不良人，一辈子都是\n")
    # 重置文件指针
    f.seek(0)
    # 读取文件内容
    for line in f.readlines():
        print(line, end="")

