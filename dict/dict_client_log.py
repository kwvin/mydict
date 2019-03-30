#dict project register model
import getpass


def log(s):
    while True:
        user = input('请输入用户名:')
        # passwd = getpass.getpass()    pycharm 中无法使用
        passwd = input("请输入密码:")
        msg = '2,' + user + ',' + passwd
        s.send(msg.encode())
        msg = s.recv(1024).decode()
        if msg == 'ok':
            print('登录成功')
            return user
        print("登录失败")
        return False