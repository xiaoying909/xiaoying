# a = ["黑寡妇","绿巨人","灭霸"]
# a.append("小影")  
# a.extend(["好大鹅","雷神"])
# print(a)     
# s = [1,2,3,4,5]
# a = [1,2,3,4,5]
# for i in range(len(a)):
#     a[i] = a[i] * 2
# print(a)
# a=[i * 2 for i in a]
# print(a)
# x = [i * 2 for i in range(1,6)]
# print(x)
# b = [[1,3,5],[2,4,6],[6,9,10]]
# c = [a[1] for a in b]        
# d= [ b[i][2-i] for i in range(len(b))]    # i = 0,1,2   分别对应，  b[1][2]
# print(d) 
# S = [[0]*3 for i in range(3)]
# print(S)
# p = [i for i in range(10) if i % 2 ==0]# 先for 语句 在if语句  最后  i 这边的语句
# print(p)
words = ["Fy","f","F11","66666","九星","F"]
l = [w for w in words if w[0] == "F" ]    #   定义w属于  words里   然后运行  循环运行if   找到w下标 0 等于‘F’的元素，输入到 l 中并输出
print(l)
a=[x + y for x in "fishc" for y in "FISHC"]
print(a)
b=[[x,y] for x in range(10) if x % 2 ==0 for y in range(10) if y %3 ==0]
print(b)
