# -*- coding: utf-8 -*-
__author__ = 'Administrator'

'''
第 0002 题：
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
import mysql.connector


def getData(filename):
    data=[]
    with open(filename,'r') as f:
        for line in f.readlines():
            line=line.replace('\n','')
            data.append(line)
    return data


def writetoDatabase(data):
    conn=mysql.connector.connect(user='root',password='dongchen',database='test')
    cursor=conn.cursor()

    sql_create="CREATE TABLE test2(\
    num char(100) not NULL\
    );"
    #cursor.execute(sql_create)

    for line in data:
        sql_insert="insert into test2 values('{0}')".format(line)
        cursor.execute(sql_insert)
    conn.commit()
    cursor.close()
    conn.close()



if __name__=="__main__":
    l=getData('data.txt')
    writetoDatabase(l)

