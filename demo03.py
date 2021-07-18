# a = input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try:
#     if int(b)> 18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确的年龄")
# import time
# import random
# import pymysql
# db=pymysql.connect(host="192.168.1.4",user="root",passwd="123456",db="testdb")
# cur = db.cursor()
# try:
#     cur.execute("select * from class;")
#     res = cur.fetchall()
#     print(res)
# except:
#     print("错误")
"""
class 声明类的名字
然后类的名字首字母必须大写
面向对象编程
类里面所有的方法，都需要传一个参数，叫self
"""
from typing import no_type_check_decorator


class GirlFriend():
    """
    女朋友
    """
    def __init__(self):
        self.sex = "女"
        self.high = "170cm"
        self.weight = "55kg"
        self.hair = "大波浪"
        self.age = "18岁"
    def caiyi(self,num):
        """
        才艺表演
        """
        if num == 1:
            print("胸口碎大石！")
        elif num == 2:
            print("唱跳RAP篮球")
        else:
            print("单手开瓶盖！")
    def chuyi(self):
        """
        厨艺
        """
        print("精通八大菜系！中外联合！啥都会做！")
    def work(self):
        """
        工作赚钱
        """
        print("司机")
#   类的实例化
zhangsan = GirlFriend
zhangsan.caiyi(0,1)
zhangsan.chuyi(0)
class Car():
    def __init__(self,pinpai,yanse,neishi,jilun):
        self.pinpai = pinpai
        self.yanse = yanse
        self.neishi = neishi
        self.jilun = jilun 
    def bianxin(self):
        print("车子变身金刚喜洋洋")
    def fly(self):
        print("车子开始起飞！")
        
        

        


