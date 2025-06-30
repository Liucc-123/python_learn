# 常见目录操作
# 1. 获取当前工作目录
import os
import shutil
from pathlib import Path

# current_dir = os.getcwd()
current_dir = Path.cwd()  # pathlib 方式
print(f"当前工作目录: {current_dir}")

# 2. 创建目录
# 2.1 创建单个目录
create_dir = "/Users/mac/刘创创/aaa"
if os.path.exists(create_dir):
    print("文件已存在，无法创建")
else:
    os.mkdir(create_dir)  # 创建单个目录（父目录需存在）

## 2.2 递归创建目录
create_dirs = "/Users/mac/刘创创/bbb/ccc"
os.makedirs(create_dirs, exist_ok=True) # 目录存在时，不报错

# 3. 删除目录
# 3.1 删除空目录
# os.rmdir("empty_dir")  # 目录必须为空
# os.rmdir("/Users/mac/刘创创/bbb") # OSError: [Errno 66] Directory not empty: '/Users/mac/刘创创/bbb'
# 3.2 递归删除非空目录
# import shutil
# shutil.rmtree("non_empty_dir")  # 删除目录及所有内容
# shutil.rmtree("/Users/mac/刘创创/bbb")


