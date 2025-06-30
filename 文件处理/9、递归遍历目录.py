# 遍历某个文件夹，判断他们分别是目录还是文件
"""
    思路分析：
    1. 获取指定目录下的所有条目（文件 or 目录）
    2. 判断是文件还是目录，输出对应的信息
    3. 如果是目录，递归调用做进一步的判断
    4. 如果是文件，输出信息，结束
"""
import os.path

# 先判断单级目录的情况
dir_path = "/Users/mac/刘创创"
# dir_all_list = os.listdir(dir_path)
# # print(dir_all_list)
# for ele in dir_all_list:
#     # 组装 file 的全路径
#     child_path = dir_path + "/" + ele
#     if os.path.isdir(child_path):
#         print(f"目录: {child_path}")
#     else:
#         print(f"文件: {child_path}")


# 考虑多级目录的情况
def get_dir_all_content(dir_path):
    """
    获取指定目录下的所有条目，并判断是文件还是目录
    :param dir_path: 指定目录路径
    :return:
    """
    dir_all_list = os.listdir(dir_path)
    # print(dir_all_list)
    for ele in dir_all_list:
        # 组装 file 的全路径
        child_path = dir_path + "/" + ele
        if os.path.isdir(child_path):
            print(f"目录: {child_path}")
            get_dir_all_content(child_path)
        else:
            print(f"文件: {child_path}")

# 测试
get_dir_all_content(dir_path)
