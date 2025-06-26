# 方式一：直接导入包中的模块
# import myPackage.module01
# import myPackage.module02
# myPackage.module01.sayHello()
# myPackage.module02.sayHi()

# 方式二：使用 from ... import ... 导入包中的模块
# from myPackage import module01, module02
# # 使用导入的模块中的函数
# module01.sayHello()
# module02.sayHi()
# 方式三：导入包的模块的指定功能
from myPackage import *
# 使用导入的函数
module01.sayHello()
# module02.sayHi()