""""
print("hello world！")   #字符串
print(2333)     #整数
print(2.3333)      #小数
print(True)              #布尔值 Ture False
print(())             #元组
print({})             #字典
print([])           #数组
print("憨憨"+"嘻嘻")#字符串的拼接
print("憨憨"*100)
print(1+2)
print(2<3)
name = "张三"                #将张三这个值赋值给了变量a（变量是小写字母）
print(name)
"""""
# a = str(input("请输入："))
# b = str(input("请输入："))
# print("inpurt获取的值",len(a+b))
# #数据格式的转换
# # type(数据) 
# print(2241)
# 3333
# 元组,小标，从0开始编号.
# a = (1,2,3,4,"憨憨","憨憨","笨比",True,False)
# print(a[4])
#切片
# print(a[0:4])   #左闭右开
# print(a[4:9])
# print(a[9:])


# print(a.index("憨憨"))#  index()   查找数据下标
# print(a.count("憨憨"))#  count()   统计某个值的数量      都只针对一层
#二维元组
# b = (a,"憨憨","嘻嘻")
# print(b[0][3])             #值中值，并列[]
# a = [1,2,3,4,"憨憨","笨比",True,False]
# a.append("append")   #append()   往数组里添加数据   增删改查
# print(a)
# # 区别：元组一定写好以后不可以修改，而数组是可以修改的。
# a.insert(0,"insert")
# print(a)
# b = a.pop(5)       #剪切
# print(a)
# print(b)
# # a.clear()     #清空数组
# # print(a)
# xx = ["你好","不好"]
# #a.extend(xx)       #添加多行数据
# print(a)
# a.remove("笨比")   #删除某个值
# print(a)
# # 下标不要超出范围 = 越界
# xx = [0,1,2,3,4]
"""
python的语法
所有的方法都是小括号结尾.比如：print(),input(),len()
元组、数组、字典的取值，都是使用中括号，比如a[0]
元组、数组、字典的定义，分别是(),[],{}
"""

"""
1.字典中的值是没有顺序的
2.字典的结构必须是键值对的结构.   key:value
3.字典的去找，是通过key取这个value
"""
# a = {"name":"张三",0:"憨憨","age":25}
# # 取值
# print(a["name"])
# # 新增
# a["high"] = "183cm"
# print(a)
# # 修改
# a["high"] = "186cm"
# print(a)
# b = a.get("name")
# print(b)
# b = a.pop("name")
# print(a)
# a.update(name=1111)   #update   存在即修改，不存在即新增
# print(a)
# print("---------------------------------------------------------")
# print(a.get("name"))
# print(a["name"])

# #   数组和字典的删除
# del a["name"]
# print(a)
""""
练习：
获取用户的个人信息，并存储到字典中。
个人信息包括，name,age,sex

方法1:
a = str(input("请输入name："))
b = str(input("请输入age："))
c = str(input("请输入sex："))
d ={"name":a,"age":b,"sex":c}
print(d)

改进版：
a = {"name":input("请输入:"),"age":input("请输入:"),"sex":input("请输入：")}
print(a)
"""
小影 = 588
print(小影)






