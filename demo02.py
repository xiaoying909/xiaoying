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
for i in range(1,10):
     for j in range(1,i+1):
         print(i,"X",j,"=",i*j,end="  ")
     print()
