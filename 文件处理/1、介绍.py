# -*- coding: utf-8 -*-
# open() 返回一个 file object ，最常使用的是两个位置参数和一个关键字参数：open(filename, mode, encoding=None)
# 如果文件无法被打开，就会抛出一个错误：OSError
# 注意：使用 open 打开对象使用完成之后，一定要记住调用 close 方法关闭资源
# 语法格式（通常是接收两个参数）：
# open(file, mode='r')
# 完整的语法格式：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 参数说明：
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# mode 参数有：https://docs.python.org/zh-cn/3.13/library/functions.html#open

# 注意：在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常也可以。
# 而且，使用 with 相比等效的 try-finally 代码块要简短得多：
with open('/Users/mac/刘创创/bird.txt', "r", encoding="utf-8") as f:
    read_data = f.read()
print(read_data)
