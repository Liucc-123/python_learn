# 题目： 编写一个名为 average() 的函数，它使用 *args 接收任意数量的数字参数。
# 函数计算并返回这些数字的平均值（浮点数）。如果未传入任何参数，返回 None 或 0（自行选择）。
def average(*args) -> float:
    """Calculate the average of given numbers.

    Args:
        *args: Variable length argument list of numbers.

    Returns:
        float: The average of the numbers, or None if no numbers are provided.
    """
    if not args:
        return None  # or return 0 if preferred

    total = sum(args)
    count = len(args)
    return total / count
print(average(1, 2, 3))