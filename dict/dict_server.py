# dict project server
import signal
import sys
import time
from socket import *
import multiprocessing as mp

from mySql_class import mysqlPython

host = "0.0.0.0"
port = 8888
ADDR = (host, port)


def do_register(c, L, db):
    #注册函数
    if L[1] == "1#":
        sql = "select count(*) from user where name = %s;"
        n = db.myselect(sql, [L[0]])[0][0]
        if n > 0:
            c.send(b'repeat name')
        else:
            c.send(b'usable', )
    else:
        sql = "insert into user(name, passwd) values(%s, %s);"
        if not db.execute(sql, L):
            c.send(b'false')
            return 0
        c.send(b'ok')


def do_log(c,  L, db):
    # 登录函数
    sql = "select passwd from user where name = %s;"
    passwd = db.myselect(sql, [L[0]])[0][0]
    if passwd == L[1]:
        c.send(b'ok')
    else:
        c.send(b'false')


def do_select(c, L, db):
    # 单词查询函数
    sql = "select interpret from words where word = %s;"
    data = db.myselect(sql, [L[0]])
    if not data:
        c.send(b'False')
    else:
        interpret = data[0][0]
        c.send(interpret.encode())

    sql = "insert into hist(name, word, time) values(%s, %s, %s);"
    ti = time.ctime(time.time())
    l = [L[1], L[0], ti]
    db.execute(sql, l)


def do_hist(c, L, db):
    # 历史查询函数
    sql = "select word, time from hist where name = %s;"
    hists = db.myselect(sql, [L[0]])
    if not hists:
        c.send(b'False')
    else:
        for hist in hists:
            msg = ','.join(hist)
            c.send(msg.encode())
            time.sleep(0.2)
        c.send(b'##')



def do_child(c):
    print("进入子进程，处理请求 ")
    db = mysqlPython("dict")
    while True:
        data = c.recv(1024).decode().split(",")
        print(data)
        if data[0] == "1":
            do_register(c, data[1:], db)
        elif data[0] == "2":
            do_log(c, data[1:], db)
        elif data[0] == "3":
            do_select(c, data[1:], db)
        elif data[0] == "4":
            do_hist(c, data[1:], db)
        elif data[0] == "Q":
            c.close()
            sys.exit()


def main():
    """创建TCP套接字，连接接入后，创建子进程处理
    客户端请求，自身循环接收客户端连接"""
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGINT ,signal.SIG_IGN)

    while True:
        print("Wait for......")
        c, addr = s.accept()
        print("connect for :", addr)
        try:
            p = mp.Process(target = do_child, args = (c,))
            p.start()
        except Exception:
            pass



if __name__ == "__main__":
    main()
