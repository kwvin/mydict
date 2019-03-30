
def dict_find(s, name):
    while True:
        word = input('请输入单词:')
        msg = '3,' + word + ',' +name
        s.send(msg.encode())
        msg = s.recv(1024).decode()
        if msg == 'False':
            print('未查到{}单词'.format(word))
            return 0
        print("{0} : {1}".format(word, msg))
        return 0

def dict_hist(s, name):
    L = []
    while True:
        msg = '4,' + name
        s.send(msg.encode())
        while True:
            msg = s.recv(1024).decode()
            if not msg:
                print('查询失败')
                return 0
            elif msg == '##':
                break
            else:
                word, time = msg.split(',')
                L.append((name, word, time))
        for i in L:
            print("用户:{0},查词:{1},时间:{2}".format(i[0], i[1], i[2]))
        return 0