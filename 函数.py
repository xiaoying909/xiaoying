
def hanshu():
    print("123546")
def he(a,b):  
    '计算a+b的方法'              #定义   he()为一个加法函数
    return a+b
print(he(3,4))
def power(x=3,y=2):
    '这个计算x的y次幂的方法 '
    a=x**y
    return a 
print(power(3,9))
# 在方法中可以导入默认参数，当输出无值时便是由默认参数代替
def text(*params):   #   *变量名，则变为了一个收集参数
     print("参数的长度是：",len(params))
     print("第二个参数是：",params[1])
text(1,'小影',5,'abc',6,8.7)    # 此时不是用return返回则无需使用 print 直接text（）
def Narcissus():
    '定义一个寻找水仙花数的方法'
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp%10) ** 3
            temp = temp // 10  # 注意这里用地板除

        if sum == each:
            print(each, end='\t')

def hello():
    return("hello world!")                #这里用print则是直接输出hello world  当a=hello（）这个方法时则会直接输出，用print（a）
                                         #则不会输出值，但是用return给予返回值后，使用到print（a）即可以输出hello world
a=hello()
print(a)
def back():
    return 1,"xiaoy",2

print(back())

def discounts(price,rate):
    '定义一个打折的方法'
    final_price = price*rate        #在函数里定义的参数，称之为局部变量   在全局中是找不到的。
    return final_price
# old_price = float(input("请输入价格："))
# rate = float(input("请输入折扣："))
# new_price=discounts(old_price,rate)
# print("打折后的价格是",new_price)
count=5
def MyFun():
    global count
    count = 10
    print(10)
print(count)
def fun1():
    print("funl正在被调用")       #   先定义fun1在  定义fun2方法  嵌套在fun1中
    def fun2():
        print("fun2正在被调用")
    fun2()
fun1()

def FunX(x):
    def FunY(y):
        return x*y
    return FunY                #返回方法Funy  执行  x*y    导出该值，
print(FunX(8)(5))             #在FunX()中给予他两个值，一个运行一层

def Fun1():                           #函数内嵌
    x = 5
    def Fun2():
        nonlocal x                  #global 方法时 得x放前面变成全局变量
        x *= x                      # 使用nonlocal 可以局部变量进行修改 从来使得程序不会报错
        return x
    return Fun2()
print(Fun1())
g = lambda x : x * 2 + 1               #lambda表达式   直接定义函数关系式   (lambda  变量  :    变量关系式) 
print(g(2))
#   filter（） 筛选器 的用法
def add(x):
    return x % 2
temp = range(10)
show = filter(add,temp)
print(list(show))
w=list(filter(lambda x : x%2,range(10)))     # 两式子完全相等   filter（）中有两变量，第一个是判定筛选的关系式，一个是筛选的范围
print(w)
#   map()  映射   的用法
q = list(map((lambda x: x * 2),range(10)))     # map()   前面也是变量关系式，后面是范围，但是将范围内的每一个值都强制性进行映射
print(q)
#   递归  函数调用自身
def factorial(n):    #普通的定义方法,利用for循环进行数值换算
    '普通定义的阶乘方法'
    result = n
    for i in range(1,n):
        result *= i          #这是局部变量   result
    return result   
number = int(input("请输入数字："))
result = factorial(number)    #这是全局变量  result
print(result,"是",number,"的阶乘")       #直接输出
print("%d是%d的阶乘"%(result,number))    #制定函数的位置用%d   可以在后面对%d进行指定参数

def factorial2(n):      #递归定义方法    一定要注意结束值！！！！！！   1.调用自身   2.正确的返回值
    '递归的阶乘方法'
    if n ==1:
        return 1
    else:
        return n * factorial2(n-1)      #一直循环   例如   6*(5*(4*(3*(2*1))))   
number2 = int(input("请输入一个正整数："))
print(factorial2(number2))