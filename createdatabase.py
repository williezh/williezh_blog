#coding:utf-8
import os
import time
import pymysql
from williezh_blog.local_settings import DATABASES 

dbconf=DATABASES.get('default')
config={'host':dbconf.get('HOST'),
    'user':dbconf.get('USER'),
    'passwd':dbconf.get('PASSWORD'),
    'port':dbconf.get('PORT'),
    'charset':'utf8mb4',
    }
database=dbconf.get('NAME')

try:
    conn=pymysql.connect(**config)
    cur=conn.cursor()
    
    cur.execute('drop database {}'.format(database))
    cur.execute('create database if not exists {}'.format(database))
    #conn.select_db(database)
    conn.commit()    

    cur.close()
    conn.close()
except Exception as e:
     print("SQL Error: {}".format(e))

    
