from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

@logit()
def myfunc():
    pass
# myfunc()

class email_logit(logit):
    """一个 logit 的实现版本，可以在函数调用时发送邮件给管理员"""
    def __init__(self, email="2511241@qq.com", *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 这里可以添加发送邮件的逻辑
        print(f"Sending email to {self.email} about the function call.")
        # 实际上，这里应该调用一个发送邮件的函数
        # send_email(self.email, "Function called", "The function was called successfully.")

@email_logit()
def myfunc2():
    pass