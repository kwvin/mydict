#dict project register model

def register(s):
    while True:
        user = input('请输入用户名:')
        msg = '1,' + user + ',1#'
        s.send(msg.encode())
        msg = s.recv(1024).decode()
        if msg == 'repeat name':
            print('用户名已占用，请更换')
        else:
            break

    while True:
        psd1 = input('请输入密码:')
        passwd = input('请再次输入:')
        if psd1 == passwd:
            break

    msg = '1,' + user + ',' + passwd
    s.send(msg.encode())
    msg = s.recv(1024).decode()
    if msg == 'ok':
        print('注册成功')
        return user
    print("注册失败")
    return False