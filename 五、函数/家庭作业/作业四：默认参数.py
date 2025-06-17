# 题目：编写一个名为 create_greeting() 的函数，它接收一个必选参数 name 和一个可选参数 greeting_word（默认值为 "Hello"）。
# 函数返回一个组合的问候字符串 "[greeting_word], [name]!"。
def create_greeting(name: str, greeting_word: str = "Hello") -> str:
    return f"{greeting_word}, {name}!"

print(create_greeting("Alice"))
print(create_greeting("Bob", "Hi"))