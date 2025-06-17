# 题目： 编写一个名为 make_counter() 的函数。这个函数初始化一个计数器 count 为 0，并定义并返回另一个名为 counter() 的内部函数。
# 每次调用 counter() 时，它使 count 增加 1 并返回新的 count 值。count 应该在 make_counter 的多次调用之间保持独立状态。
def make_counter():
    """Create a counter function that maintains its state across calls."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter
c1 = make_counter()
print(c1())
print(c1())
print(c1())