#判断  代码块 缩进
# a = 1
# b = 2
# if a == 1:
#     print("hhh")



# if a > b:
#     print("a比b大")
# else:
#     print("a比b小")

# age =int( input("请输入你的年龄："))
# if age > 60:
#     print("你应该退修了")
# elif age > 30:
#     print("家庭的责任重大")
# elif age > 20:
#     print("一定要好好规划你的未来")
# else:
#     print("一定要好好学习")
     # if   elif    else    有区别的
#----------------------------------------------
#   in的用法
# a = "你好"
# if a  in "你好，今天你吃了吗":
#     print("OK")
# else:
#     print("NO")
#----------------------------------------------
# a = input("请输入：")
# if a == "":
#      print("不能为空！")
#      exit()
# if a in "0123456789":
#     a = int(a)
# else:
#      print("请重新输入：")
#      exit()
# if a > 5:
#      print("大")
# else:
#      print("小")
#----------------------------------------------
# a = 10
# if type(a) is int:
#      print("是数字！")
# elif type(a) is  str:
#      print("是字符串")
# else:
#      print("其他")
#----------------------------------------------
# a = 1
# while a < 10:
#      print("憨憨",a)
#      a = a + 2

#   遍历
# a = "你好，今天你吃了吗？"
# for i in a:
#      print(i)
# a=["zhangsan"]
# for i in a:
#      print(i)
# # b = list(range(0,100,2)) # 自动生成了一个数列,步长/步进
# # print(b)
# for i in range(10):
#      print(i)
# for i in range(1,10):
#      for j in range(1,i+1):
#          print(i,"X",j,"=",i*j,end="  ")
#      print()
# for i in range(10):
#      if i == 4:
#       continue
#      print(i)

#方法/函数 

def checkname(username):
     """
     自动的判断账号的长度是5-8位，并且账号是小写     
     """
     if len(username) >=5 and len(username) <=8:
        if username[0] in "qazwsxedcrfvtgbyhnujmiklop":
          print()
        else:
          print("账号的首字母必须小写字母开头")
     else:
      print("账号不符合规范")
# def 方法的声明
# checkname 方法的名字
# username  方法的参数
#""""方法的说明""""
# 方法的逻辑代码
def jiafa(a,b):
     """
     方法的作用是数字相加
     """
     if type(a) is int and type(b) is int:# typy()   查询数据类似    is   和某个数据类型一样
         return a+b
     else:
          return "输入的数据类型不正确"
"""
返回值，返回后我们可以对这个值进行其他操作
而，print不行
"""
# try:
#     print(1+"a")
# except Exception as e:
#      print("上面代码错了",e)
#异常类 包>类>方法>变量
username=input("请输入:")
print(checkname)
