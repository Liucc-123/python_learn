# Filename: say_hello.py
# 只有sayHello函数对外暴露
__all__ = ['sayHello']
def sayHello():
    print("Hello, world!")

def sayHi():
    print("Hi, there!")

if __name__ == '__main__':
    # 测试代码
    sayHello()

print("__name__:", __name__)