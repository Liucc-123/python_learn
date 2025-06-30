
with  open("/Users/mac/刘创创/hello.txt", encoding="utf-8") as f:
    # 读取方式一：一次性读取 file 对象的全部内容
    # content = f.read()
    # print(f"content: {content}")
    # 读取方式二：读取单行数据
    # while True:
    #     content = f.readline() # 自带换行
    #     if not content:
    #         break
    #     print(content, end="") # 这里就不需要 print 默认的换行效果了
    # 读取方式三：遍历 file 对象获取内容
    # for line in f:
    #     print(line, end="")
    # 读取方式四：以列表形式读取 file 对象的所有行
    # lines = f.readlines()
    lines = list(f)
    for line in lines:
        print(line, end="")
