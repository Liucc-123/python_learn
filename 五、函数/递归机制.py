# 分析下面代码的执行流程
def test(n):
    if n > 2:
        test(n - 1)
    print("n =", n)


# test(4)

# 阶乘问题
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(4))


## 斐波那契数列 1,1,2,3,5,8,13…
# f(0)=1, f(1) = 1, f(n) = f(n-1) + f(n-2) (n >= 2)
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5))

## 题目二：猴子吃桃问题：有一堆桃子，猴子第一天吃了其中的一半，并再多吃了一个。以后每天猴子都吃其中的一半，然后再多吃一个。
# 当到第 10 天时，想再吃时（即还没吃），发现只有 1 个桃子了。问最初共多少个桃子？
"""
第 10天还有 1 个桃子
第9天还有：(1 + 1) * 2 = 4 个
第 8 天还有：(4 + 1) * 2 = 10 个
第 7 天还有：(10 + 1) * 2 = 22 个
...
"""


def eatPeach(day: int) -> int:
    """
    查询这一天还剩多少个桃子
    :param day: 第几天
    :return: 这天还剩下几个桃子
    """
    if day == 10:
        return 1
    return (eatPeach(day + 1) + 1) * 2


# 第一天还有多少个桃子，也即最初有多少个桃子
# print(eatPeach(1))


## 题目三：求函数值，已知 f(1) = 3; f(n)= 2*f(n-1)+1；请使用递归的思想，求出 f(n)的值？
def f(n: int) -> int:
    if n == 1:
        return 3
    return 2 * f(n - 1) + 1


# print(f(2))


## 题目四：汉诺塔: 给定盘子的数量 num，有三个塔 a, b, c，打印出 num 个盘子从 a 塔移动到 c 塔的移动顺序
def hanoi_tower(num, a, b, c):
    """
    打印指定数量 num 个盘子的移动顺序
    :param num: 盘子的数量
    :param a: 原始位置
    :param b: 中间借助位置
    :param c: 目标移动位置
    :return:
    """
    if num == 1:
        # 只有一个盘，将其移动到 C 塔
        print(f"第1个盘：{a} -> {c}")
    else:
        # 多个盘情况：我们认为两个盘，即最下面的盘和上面所有盘
        # 1.先将上面所有盘移动到 B 塔，这时需要借助 C 塔来完成移动
        hanoi_tower(num - 1, a, c, b)
        # 2.然后移动最底下的盘
        print(f"第{num}个盘：{a} -> {c}")
        # 3.最后把剩余盘从 B 塔移动到 C 塔，这时需要借助 A 塔来完成移动
        hanoi_tower(num - 1, b, a, c)

# 3个汉诺塔的移动顺序
hanoi_tower(3, "A", "B", "C")

