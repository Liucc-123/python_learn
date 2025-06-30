## 需求
# 1. 实现登录验证，如果用户名是列表中的元素["smith", "tim", "jerry", "bruth"]，且密码是 888，那么就登录成功，否则登录失败
# 2. 不管登录成功失败与否，都需要记录登录日志到文件中
# 3. 登录成功，可以看到相应的菜单提示信息，请实现相应的功能。
# 登录成功后：
"""
30个=请选择操作30个=
15个空格1 查 看 当 前 登 录 用 户
15个空格2 查 看 登 录 日 志
15个空格3 退出系统
"""
import datetime


## 查看当前登录用户
# 打印当前用户名即可
## 日志格式
# {用户名}登录{登录状态}登录时间是{登录时间}
## 退出系统
# 输出“已退出系统，再见～”
def login(username: str) -> bool:
    """
    用户登录验证
    :param: username 用户名
    :return: 登录成功与否
    """
    database = ["smith", "tim", "jerry", "bruth"]
    if username not in database:
        print("用户名或密码错误！")
        login_log(username, "失败")
        return False
    # 记录登录日志
    login_log(username, "成功")
    return True


def login_log(username: str, status: str):
    """
    记录登录日志
    :param username:
    :param status 成功/失败
    :return:
    """
    # 在当前系统目录下创建 login.log文件，追加模式
    with open("./login.log", "a+", encoding="utf-8") as f_login:
        # 当前系统时间
        cur_time = datetime.datetime.now()
        formatted_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
        f_login.write(f"{username}登录{status}，登录时间为 {formatted_time}\n")


if __name__ == '__main__':
    username = input("请输入您的用户名：")
    if login(username):
        # 跳转系统菜单页
        while(True):
            print("=" * 15 + "请选择操作" + "=" * 15)
            print(" " * 15 + "1 查 看 当 前 登 录 用 户")
            print(" " * 15 + "2 查 看 登 录 日 志")
            print(" " * 15 + "3 退出系统")
            u_input = int(input(""))
            if 1 == u_input:  # 查看当前登录用户
                print(f"当前登录用户是 {username}")

            elif 2 == u_input:  # 查看登录日志
                with open("./login.log", "r", encoding="utf-8") as f_read:
                    for line in f_read:
                        print(line, end="")

            elif 3 == u_input: # 退出系统
                print("已退出系统，再见～")
                break
            else:
                print("请输入合法操作（1-3）:")



# 测试
# cur_time = datetime.datetime.now()
# print(cur_time.strftime("%Y-%m-%d %H:%M:%S"))
# login("tim")
