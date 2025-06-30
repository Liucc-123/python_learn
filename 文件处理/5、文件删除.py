# 使用 os模块的 remove 方法进行文件删除
# 需求：如果/Users/mac/刘创创/aa.txt文件存在，则删除之；否则给出提示：文件不存在，无法删除
import os.path

file = "/Users/mac/刘创创/aa.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print("文件不存在，无法删除")