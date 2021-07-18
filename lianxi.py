"""
# 练习：
# 假设现在有10个学生的成绩，需要录入系统。
# 这些人分别是，张三，李四，王麻子，小影，亚索，梦魇，刀妹，剑姬,皇子，王子
# 并且名字和成绩对应上
# 而且大于60和小于60的分开存放
"""
#----------------------------------------------------------------------------
"""
# gao = {}                   #定义一个空字典，储存大于60分的人
# di = {}                    #定义一个空字典，储存小于60分的人
# xuesheng = ["张三","李四","王麻子","小影","亚索","梦魇","刀妹","剑姬","皇子","王子"]   #定义一个数组，储存人物姓名
# a = 0                       #定义了一个变量，用来控制数组的下标变化
# while a < len(xuesheng):     #因为所有人的向欧盟西欧的录入，都要用到input，所有写了循环，len判断数组了数组的长度，总长度-1就是最大的下标
#      chengji = int(input("请输入"+xuesheng[a]+"的成绩:"))     #录入信息，为了方便判断，所以转换了格式
#      if chengji >= 60:    #判断分数
#           gao[xuesheng[a]] = chengji    #存在字典中
#      else: 
#           di[xuesheng[a]] = chengji 
#      a = a+1             #控制下标变化，每一次循环都+1
# print("大于60分的",gao)
# print("小于60分的",di )
"""



#   for循环

# gao = {}                   #定义一个空字典，储存大于60分的人
# di = {}                    #定义一个空字典，储存小于60分的人
# xuesheng = ["张三","李四","王麻子","小影","亚索","梦魇","刀妹","剑姬","皇子","王子"]   #定义一个数组，储存人物姓名
# for i in  xuesheng:     #因为所有人的向欧盟西欧的录入，都要用到input，所有写了循环，len判断数组了数组的长度，总长度-1就是最大的下标
#      chengji = int(input("请输入"+i+"的成绩:"))     #录入信息，为了方便判断，所以转换了格式
#      if chengji >= 60:    #判断分数
#           gao[i] = chengji    #存在字典中
#      else: 
#           di[i] = chengji 
# print("大于60分的",gao)
# print("小于60分的",di )




"""
练习：
输出一个九九乘法表
"""

# for i in range(1,10):
#    for j in range(1,i+1):
#        print(i,"X",j,"=",i*j,end="  ")
#      print()

"""
练习1
通过print打印,模拟一个红路灯的功能，红灯30次，绿灯35次，黄灯三次
练习2
使用代码实现一个注册功能，用户输入账号密码，要求账号长度是5-8位，密码6-16位，并且账号必须小写字母开头
并储存到字典中{username:password}
"""

#练习1
# i=1
# while i>0:
#      a=30
#      while a>0 and a<=30:
#          print("红灯还有",a,"秒关闭") 
#          a=a-1
#      b=35
#      while b>0 and b<=35:
#          print("绿灯还有",b,"秒关闭")
#          b=b-1
#      c=3
#      while c>0 and c<=3:
#          print("黄灯还有",c,"秒关闭")
#          c=c-1
#      i=i-1
#      print("循环结束")

#练习2
# a=input("请输入账号：")
# b=input("请输入密码：")
# c={a:b}
# if len(a) >= 5 and len(a) <= 8:
#      if len(b) >=6 and len(b) <=16:
#           print("注册成功！")
#           print(c)
#      else:
#           print("密码不符合规范")
# else:
#      print("账号不符合规范")
#练习1  老师版
# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#          for j in range(light[i]):
#                print(i,"还有",light[i]-j,"秒关闭")
#练习2 老师版
# username = input("请输入账号：")
# password = input("请输入密码：")
# if len(username) >=5 and len(username) <=8:
#      if username[0] in "qazwsxedcrfvtgbyhnujmiklop":
#           if len(password) >=8 and len(password) <=16:
#                print("注册成功",{username:password})
#           else:
#                print("密码不符合规范")
#      else:
#           print("账号的首字母必须小写字母开头")
# else:
#      print("密码不符合规范")

"""
练习：
定义一个方法判断用户输入的方法是否符合规范
"""
# def xy(name,password):
#     if len(name) >=6 and len(name) <=9:
#         if len(password) >= 7 and len(password):
#                 print("注册成功") 
#         else:
#                 print("密码不规范")
#     else:
#         print("账号不规范")
# name=input("请输入账号:")
# password=input("请输入密码")
# print(xy(name,password))

#老师的代码
def checkname(username,password):
     """
     自动的判断账号的长度是5-8位，并且账号是小写     
     """
     if len(username) >=5 and len(username) <=8:
        if username[0] in "qazwsxedcrfvtgbyhnujmiklop":
            if len(password) >= 8 and len(password) <=16:
                
              return True
            else :
                return "密码不符合规范"
        else:
          return "账号的首字母必须小写字母开头"
     else:
      return "账号不符合规范"
username = input("请输入账号：")
password = input("请输入密码")
print(checkname(username,password))
