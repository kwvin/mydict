# dict project client
import sys
import time
from socket import *

from dict_page import *
from dict_client_find import *
from dict_client_register import register
from dict_client_log import log


host = "192.168.5.12"
port = 8888
ADDR = (host, port)


def two_main(s, name):
    while True:
        page_two()
        n = input("请选择:")
        if n == "1":
            dict_find(s, name)
        elif n == "2":
            dict_hist(s, name)
        elif n == 'q':
            return 0
        else:
            print('命令有误，重新选择')


def main():
    """创建TCP套接字"""
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    try:
        s.connect(ADDR)
    except Exception:
        print('服务器连接失败，请重试.....')
        sys.exit(0)

    while True:
        page_one()
        n = input("请选择:")
        if n == "1":
            name = register(s)
            if not name:
                continue
            two_main(s, name)
        elif n == "2":
            name = log(s)
            if not name:
                continue
            two_main(s, name)
        elif n == 'q':
            print('系统即将退出')
            s.send(b'Q')
            time.sleep(1)
            s.close()
            sys.exit(0)
        else:
            print('命令有误，重新选择')


if __name__ == "__main__":
    main()