

def decorate(func):
    def inner():
        print("-----------------------------------------------")
        func()
        print("-----------------------------------------------")
    return inner

@decorate
def page_one():
    print("     <--  1.注册    2.登录    q.退出   -->     ")


@decorate
def page_two():
    print("     <--  1.查询    2.记录    q.退出   -->     ")


# 用于测试
if __name__ == "__main__":
    page_one()
    page_two()