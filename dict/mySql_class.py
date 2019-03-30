from pymysql import *

class mysqlPython:
    def __init__(self, database,
                 host = 'localhost',
                 user = 'root',
                 password = "19921013",
                 port = 3306,
                 charset = "utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.database = database


    def open(self):
        # 初始化连接
        self.db = connect(host = self.host,
                          port = self.port,
                          user = self.user,
                          password = self.password,
                          database = self.database,
                          charset = self.charset)
        self.cur = self.db.cursor()


    def close(self):
            self.cur.close()
            self.db.close()


    def execute(self, sql, L = None):
        if L is None:
            L = []
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            print("ok")
        except Exception as e:
            self.db.rollback()
            print("failed:",e)
            self.close()
            return False
        self.close()
        return True


    def myselect(self,sql,L = None):
        if L is None:
            L = []
        try:
            self.open()
            self.cur.execute(sql,L)
            result = self.cur.fetchall()
            self.db.commit()
            print("ok")
        except Exception as e:
            self.db.rollback()
            print("failed:",e)
            self.close()
            return False
        self.close()
        return result