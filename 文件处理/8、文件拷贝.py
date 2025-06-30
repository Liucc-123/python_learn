# 需求：将图片从目录拷贝到另一个目录中，使用 read 和 write 原生方法实现。
import os.path

source_path = "/Users/mac/刘创创/test.png"
target_path = "/Users/mac/刘创创/aaa/bbb/ccc/test.png"
"""
    思路分析：
    1. 检查源文件是否存在
    2. 检查目标文件是否存在，如果不存在，则创建之
    3. 以二进制读写模式创建 file 对象，写入到目标文件中
"""
# 初始资源检查及准备
if not os.path.exists(source_path):
    raise RuntimeError("原始图片不存在，无法拷贝～")
if not os.path.exists(target_path):
    # 创建其父目录
    target_dir = os.path.dirname(target_path)
    os.makedirs(target_dir, exist_ok=True)
else:
    print("目标文件存在，不需要创建～")

# # 读取图片资源，并写入
# with open(source_path, "rb") as source_file:
#     bin_content = source_file.read()
# print("读取完毕～")
# with open(target_path, "wb") as target_file:
#     # content = str(bin_content)
#     target_file.write(bin_content)
# print("写入完毕～")

## 上面这种方式是一次性读取全部内容，才写入到目标文件。这在大文件情况下，对内存的压力是很大的。
with open(source_path, "rb") as f_source:
    with open(target_path, "wb") as f_target:
        for line in f_source:
            f_target.write(line)
print("写入完成～")

