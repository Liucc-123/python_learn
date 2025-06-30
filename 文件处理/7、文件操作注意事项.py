# 文件操作有以下几点注意事项：
# 1. file.flush()：强制刷新缓冲区的内容写入到磁盘文件里
import time
# with open("/Users/mac/刘创创/hi.txt", "w+", encoding="utf-8") as f:
#     print("开始写入～")
#     for _ in range(10):
#         f.write("你欲何为？让天下大同\n")
#     f.flush() # 刷新缓冲区内容到磁盘文件中
#     time.sleep(100000)
#     print("写入end～")

# 2. file.close()方法内部自带 flush()功能，因此之前的案例中不需要手动调用 flush()方法
# 3. 在with 语句里打开 file 对象，会自动close文件对象资源，也即不需要我们手动调用file.close()方法进行关闭了。
# with open("/Users/mac/刘创创/bird.txt", "r", encoding="utf-8") as f:
#     for readline in f.readlines():
#         print(readline, end="")
# # 文件是否关闭
# print()
# print(f"文件是否关闭 -> {f.closed}")
