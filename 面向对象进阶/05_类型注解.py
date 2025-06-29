## 为什么需要类型注解？
# 类型注解可以帮助我们在编写代码时更清晰地表达变量的预期类型
def print_str(a: str):
    for item in a:
        print(item, end="\t")


print_str("100")

## 1. 变量的类型注解
# 基本语法：变量名: 类型 = 值
# 1.1 基础数据类型的类型注解
num1: int = 100


# 1.2 对象类型的类型注解
class Cat:
    pass


cat: Cat = Cat()
# 1.3 容器类型的类型注解
my_list: list = [1, 2, 3]  # 对my_list进行类型注解，标注my_list类型为list。
my_tuple: tuple = ("run", "sing", "fly")
my_set: set = {1, 2, 3}
my_dict: dict = {"name": "Tom", "age": 22}
# 1.4 容器详细类型注解
my_list: list[str] = ["apple", "banana", "cherry"]  # 列表中的元素类型为str
# 1.5 在注释中使用类型注解
num = 20  # type: int

## 2. 函数/方法的类型注解
# 基本语法
"""
    def 函数名(参数: 参数类型) -> 返回值类型:
        # 函数体
"""
def add(a: int, b: int) -> int:
    return a + b
# 注意：类型注解是提示性的，并不是强制性的，如果你给的类型和指定/标注的类型不一致，IDE 只会给出黄色警告，但是仍然可以运行。

## 3. Union 联合类型
from typing import Union
# 形参列表可以接收 int 或 str 类型的数据
def process_data(data: Union[int, str]) -> str:
    """
    处理数据，根据数据类型返回不同的字符串描述
    :param data:
    :return:
    """
    if isinstance(data, int):
        return f"处理整数: {data}"
    elif isinstance(data, str):
        return f"处理字符串: {data}"
    else:
        raise ValueError("数据类型不支持")