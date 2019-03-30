import sys
import os
import re

from mySql_class import *


def create_table(db):
    #在数据库中建立数据表user，hist，words。
    sql_1 = "create table user (id int primary key auto_increment,name varchar(32) not null,passwd varchar(16) default '000000');"
    sql_2 = "create table hist (id int primary key auto_increment,name varchar(32) not null,word varchar(32) not null,time varchar(64));"
    sql_3 = "create table words (id int primary key auto_increment,word varchar(32) not null,interpret text not null);"
    L = [sql_1, sql_2, sql_3]
    for i in L:
            db.execute(i)
    return 0


def insert_info(db):
    with open("dict.txt") as f:
        while True:
            data = f.readline()
            if not data:
                break
            Mylist = re.split("\s+",data)
            msg = " ".join(Mylist[1:])
            sql = "insert into words(word,interpret) VALUES(%s,%s)"
            db.execute(sql,[Mylist[0], msg])
    return 0


def main(argc,argv,envp):
    db = mysqlPython("dict")
    # create_table(db)
    # insert_info(db)
    db.close()

    return 0


if __name__ =="__main__":
    sys.exit(main(len(sys.argv), sys.argv, os.environ))