# a = input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try:
#     if int(b)> 18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确的年龄")
import time
import random
import pymysql
db=pymysql.connect(host="192.168.1.4",user="root",passwd="123456",db="testdb")
cur = db.cursor()
try:
    cur.execute("select * from class;")
    res = cur.fetchall()
    print(res)
except:
    print("错误")